from typing import Tuple

import numpy as np
from PySide6 import QtGui
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QGridLayout
from skimage import io

from puzzle.database import DatabaseController
from puzzle.utils import cut_image_into_triangles
from puzzle.user.game.new_game.puzzle_game.common.signals import SignalSenderSendDataImageTriangle

from .qclicked_drop_triangle_lenta_label import QClickedDropTriangleLentaLabel
from puzzle.user.game.new_game.puzzle_game.common.constants import TOP_ELEMENT, BOTTOM_ELEMENT


class OnLentaTriangleFrame(QFrame):

    LINE_THICK = 3

    def __init__(
            self, original_image_path: str,
            size_block_w: int, size_block_h: int,
            signal_sender_on_scroll: SignalSenderSendDataImageTriangle,
            game_config: str = None):
        super().__init__()
        self.setAcceptDrops(True)

        if game_config is None:
            puzzles_top_position, puzzles_bottom_position = (
                    [-1] * (size_block_h * size_block_w), # -1 - empty spot
                    [-1] * (size_block_h * size_block_w)  # -1 - empty spot
            )
        else:
            puzzles_top_position, puzzles_bottom_position = DatabaseController.parse_lenta_frame_triangle_config(game_config)

        self._size_block_w = size_block_w
        self._size_block_h = size_block_h

        self.signal_sender_on_scroll = signal_sender_on_scroll
        self._choosen_pease_frame = None
        self._original_image = io.imread(original_image_path)
        self._original_image_path = original_image_path
        self._origin_h, self._origin_w = self._original_image.shape[:-1]

        self.signal_sender_send_data_image = SignalSenderSendDataImageTriangle()
        self.signal_sender_send_data_image.signal.connect(self._update_certain_label)

        grid = QGridLayout()
        self._grid = grid
        labels_list = []
        puzzle_size_w = self._origin_w // self._size_block_w
        puzzle_size_h = self._origin_h // self._size_block_h
        self._puzzle_size_h = puzzle_size_h
        self._puzzle_size_w = puzzle_size_w
        counter = 0
        for i in range(self._size_block_h):
            w_label_list = []
            for j in range(self._size_block_w):
                s_label = QClickedDropTriangleLentaLabel(
                    signal_sender_on_scroll=self.signal_sender_on_scroll,
                    signal_sender_send_data_image=self.signal_sender_send_data_image,
                    indx_top=counter, current_indx_top=puzzles_top_position[counter],
                    indx_bot=counter, current_indx_bot=puzzles_bottom_position[counter]
                )
                s_label.setFixedWidth(puzzle_size_w)
                s_label.setFixedHeight(puzzle_size_h)
                w_label_list.append(s_label)
                counter += 1
            labels_list.append(w_label_list)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(0)
        self._labels_list = labels_list
        self._copy_pixmap = None
        self._update_labels(self._original_image, puzzles_top_position, puzzles_bottom_position)
        self.setLayout(grid)

    def _update_certain_label(self, indx_origin: int, indx_current: int, type_puzzle: str, pixmap: QPixmap):

        if pixmap.isNull():
            pixmap = None

        if type_puzzle == TOP_ELEMENT:
            # top
            for elem_list in self._labels_list:
                for elem in elem_list:
                    if elem.indx_top == indx_origin:
                        elem.current_indx_top = indx_current
                        elem.pixmap_top = pixmap
                        elem.combine_pixmap()
                        break
        elif type_puzzle == BOTTOM_ELEMENT:
            # bot
            for elem_list in self._labels_list:
                for elem in elem_list:
                    if elem.indx_bot == indx_origin:
                        elem.current_indx_bot = indx_current
                        elem.pixmap_bot = pixmap
                        elem.combine_pixmap()
                        break
        self.update()

    def _update_labels(self, source_img: np.ndarray, puzzles_top_position: list, puzzles_bottom_position: list):
        size = source_img.shape
        triangles_top_list, triangles_bottom_list, mask = cut_image_into_triangles(
            source_img=source_img,
            size_block_w=self._size_block_w, size_block_h=self._size_block_h,
            thick_of_border_line=OnLentaTriangleFrame.LINE_THICK
        )
        step_w = int(size[1] // self._size_block_w)
        step_h = int(size[0] // self._size_block_h)
        self._is_empty = []
        counter = 0
        for i in range(self._size_block_h):
            for j in range(self._size_block_w):
                qlabel_s = self._labels_list[i][j]
                self._grid.addWidget(qlabel_s, i, j)
                if puzzles_top_position[counter] != -1:
                    image_top = triangles_top_list[puzzles_top_position[counter]]
                    qlabel_s.pixmap_top = QPixmap.fromImage(image_top)

                if puzzles_bottom_position[counter] != -1:
                    image_bot = triangles_bottom_list[puzzles_bottom_position[counter]]
                    qlabel_s.pixmap_bot = QPixmap.fromImage(image_bot)

                qlabel_s.w, qlabel_s.h = step_w, step_h
                qlabel_s.mask = mask.copy()
                qlabel_s.combine_pixmap()
                self._is_empty.append(True)
                counter += 1

    def get_game_info(self) -> Tuple[list, list]:
        position_top_indx = []
        position_bottom_indx = []

        for i in range(self._size_block_h):
            for j in range(self._size_block_w):
                position_top_indx.append(self._labels_list[i][j].current_indx_top)
                position_bottom_indx.append(self._labels_list[i][j].current_indx_bot)

        return position_top_indx, position_bottom_indx

    def get_all_num_and_bad_placeses(self) -> Tuple[int, int]:
        bad_placed = 0
        counter = 0
        for i in range(self._size_block_h):
            for j in range(self._size_block_w):
                if self._labels_list[i][j].current_indx_top != counter:
                    bad_placed += 1

                if self._labels_list[i][j].current_indx_bot != counter:
                    bad_placed += 1
                counter += 2
        return counter, bad_placed

    def _game_status(self):
        game_status = self._check_status_game()
        if game_status:
            print('all good! Game over...')
        else:
            print("Somewhere wrong peases lias!")

    def _check_status_game(self) -> bool:
        pass

