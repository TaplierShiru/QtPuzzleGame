import os

import numpy as np
from PIL import Image, ImageDraw, ImageQt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QFrame, QGridLayout
from skimage import io, draw

from puzzle.utils import cut_image_into_triangles
from puzzle.user.game.new_game.puzzle_game.common.signals import SignalSenderSendDataImage
from .qclicked_drop_triangle_label import QClickedDropTriangleLabel


class OnFieldTriangleFrame(QFrame):

    LINE_THICK = 5

    def __init__(
            self, original_image_path: str,
            size_block_w: int, size_block_h: int):
        super().__init__()
        self.setAcceptDrops(True)

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
                s_label = QClickedDropTriangleLabel(
                    signal_sender_send_data_image=self.signal_sender_send_data_image,
                    indx_top=counter+1, current_indx_top=counter+1,
                    indx_bot=counter, current_indx_bot=counter
                )
                s_label.setFixedWidth(puzzle_size_w)
                s_label.setFixedHeight(puzzle_size_h)
                w_label_list.append(s_label)
                counter += 2
            labels_list.append(w_label_list)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(0)
        self._labels_list = labels_list
        self._update_labels(self._original_image)
        self.setLayout(grid)

    def _update_certain_label(self, indx_origin: int, indx_current: int, pixmap: QPixmap):
        if indx_origin % 2 == 1:
            # top
            for elem_list in self._labels_list:
                for elem in elem_list:
                    if elem.indx_top == indx_origin:
                        elem.current_indx_top = indx_current
                        elem.pixmap_top = pixmap
                        elem.combine_pixmap()
                        break
        else:
            # bot
            for elem_list in self._labels_list:
                for elem in elem_list:
                    if elem.indx_bot == indx_origin:
                        elem.current_indx_bot = indx_current
                        elem.pixmap_bot = pixmap
                        elem.combine_pixmap()
                        break
        self.update()

    def _update_labels(self, source_img: np.ndarray):
        size = source_img.shape
        triangles_top_list, triangles_bottom_list, mask = cut_image_into_triangles(
            source_img=source_img,
            size_block_w=self._size_block_w, size_block_h=self._size_block_h,
            thick_of_border_line=OnFieldTriangleFrame.LINE_THICK
        )
        step_w = int(size[1] // self._size_block_w)
        step_h = int(size[0] // self._size_block_h)
        counter = 0

        for i in range(self._size_block_h):
            for j in range(self._size_block_w):
                qlabel_s = self._labels_list[i][j]
                self._grid.addWidget(qlabel_s, i, j)

                image_top, image_bot = triangles_top_list[counter], triangles_bottom_list[counter]
                qlabel_s.pixmap_top = QPixmap(image_top)
                qlabel_s.pixmap_bot = QPixmap(image_bot)
                qlabel_s.mask = mask.copy()
                qlabel_s.w, qlabel_s.h = step_w, step_h
                qlabel_s.combine_pixmap()
                counter += 1

    def _game_status(self):
        game_status = self._check_status_game()
        if game_status:
            print('all good! Game over...')
        else:
            print("Somewhere wrong peases lias!")

    def _check_status_game(self) -> bool:
        pass
