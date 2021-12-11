from typing import Tuple

import numpy as np
from PySide6 import QtGui
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QGridLayout, QMessageBox
from skimage import io
from PIL import ImageQt, Image

from puzzle.common.qmess_boxes import return_qmess_box_connect_db_error
from puzzle.utils import cut_image_into_rectangles
from puzzle.user.game.new_game.puzzle_game.common.signals.signal_send_data_image import SignalSenderSendDataImage
from .qclicked_drop_label import QClickedDropLabel

from puzzle.database import DatabaseController


class OnFieldRectangleFrame(QFrame):

    LINE_THICK = 3

    def __init__(
            self, original_image_path: str,
            size_block_w: int, size_block_h: int,
            game_config: str = None):
        super().__init__()
        self.setAcceptDrops(True)
        self._qmess_box: QMessageBox = None

        if game_config is None:
            puzzles_position = list(range(size_block_h * size_block_w))
        else:
            # Parse config
            puzzles_position = DatabaseController.parse_rectangle_config(game_config=game_config)

            if puzzles_position is None:
                self._qmess_box = return_qmess_box_connect_db_error()
                self._qmess_box.show()
                return

        self._size_block_w = size_block_w
        self._size_block_h = size_block_h

        self.signal_sender_send_data_image = SignalSenderSendDataImage()
        self.signal_sender_send_data_image.signal.connect(self._update_certain_label)
        self._choosen_pease_frame = None
        self._original_image = io.imread(original_image_path)
        self._original_image_path = original_image_path
        self._origin_h, self._origin_w = self._original_image.shape[:-1]
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
                s_label = QClickedDropLabel(
                    signal_sender_send_data_image=self.signal_sender_send_data_image,
                    indx=counter, current_indx=puzzles_position[counter]
                )
                s_label.setFixedWidth(puzzle_size_w)
                s_label.setFixedHeight(puzzle_size_h)
                w_label_list.append(s_label)
                counter += 1
            labels_list.append(w_label_list)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(0)
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)
        self._labels_list = labels_list
        self._init_labels(self._original_image, puzzles_position)
        self.setLayout(grid)

    def _update_certain_label(self, indx_origin: int, indx_current: int, pixmap: QPixmap):
        for elem_list in self._labels_list:
            for elem in elem_list:
                if elem.indx == indx_origin:
                    elem.current_index = indx_current
                    elem.setPixmap(pixmap)
                    break
        self.update()

    def _init_labels(self, source_img: np.ndarray, puzzles_position: list):
        size = source_img.shape
        peases_list = cut_image_into_rectangles(
            source_img=source_img,
            size_block_w=self._size_block_w, size_block_h=self._size_block_h,
            thick_of_border_line=OnFieldRectangleFrame.LINE_THICK
        )
        step_w = int(size[1] // self._size_block_w)
        step_h = int(size[0] // self._size_block_h)
        counter = 0

        for i in range(self._size_block_h):
            for j in range(self._size_block_w):
                qlabel_s = self._labels_list[i][j]
                self._grid.addWidget(qlabel_s, i, j)
                qimage = peases_list[puzzles_position[counter]]
                qlabel_s.setPixmap(QPixmap(qimage))
                counter += 1

    def get_game_info(self) -> list:
        indx_position = []
        for i in range(self._size_block_h):
            for j in range(self._size_block_w):
                indx_position.append(self._labels_list[i][j].current_index)
        return indx_position

    def get_all_num_and_bad_placeses(self) -> Tuple[int, int]:
        bad_placed = 0
        counter = 0
        for i in range(self._size_block_h):
            for j in range(self._size_block_w):
                if self._labels_list[i][j].current_index != counter:
                    bad_placed += 1
                counter += 1
        return counter, bad_placed
