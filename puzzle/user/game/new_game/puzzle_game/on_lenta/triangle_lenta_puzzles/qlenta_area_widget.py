from typing import Tuple

import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLayout, QMessageBox
from skimage import io

from puzzle.common.qmess_boxes import return_qmess_box_connect_db_error
from puzzle.user.game.new_game.puzzle_game.common.signals import SignalSenderSendDataImageTriangle
from .qclicked_triangle_lenta_label import QClickedTriangleLentaLabel

from puzzle.database import DatabaseController

from puzzle.utils import FRAME_H, FRAME_W, cut_image_into_triangles
from puzzle.user.game.new_game.puzzle_game.common.constants import FROM_SCROLL_BOTTOM_ELEMENT, FROM_SCROLL_TOP_ELEMENT


class ScrolledTriangleFrame(QFrame):

    LINE_THICK = 3

    def __init__(
            self, original_image_path: str,
            size_block_w: int, size_block_h: int,
            signal_sender_on_scroll: SignalSenderSendDataImageTriangle,
            game_config: str = None):
        super().__init__()
        self.setAcceptDrops(True)
        self._qmess_box: QMessageBox = None
        if game_config is None:
            puzzles_top_position, puzzles_bottom_position = (
                list(range(size_block_h * size_block_w)),
                list(range(size_block_h * size_block_w))
            )
        else:
            puzzles_top_position, puzzles_bottom_position = DatabaseController.parse_lenta_scroll_triangle_config(game_config)

            if puzzles_top_position is None or puzzles_bottom_position is None:
                self._qmess_box = return_qmess_box_connect_db_error()
                self._qmess_box.show()
                return


        len_puzzle_position = len(puzzles_top_position) + len(puzzles_bottom_position)

        self._size_block_w = size_block_w
        self._size_block_h = size_block_h

        self.signal_sender_on_scroll = signal_sender_on_scroll
        self.signal_sender_on_scroll.signal.connect(self._change_part_view)

        puzz_w, puzz_h = FRAME_W // self._size_block_w, FRAME_H // self._size_block_h
        puzz_scroll_h, puzz_scroll_w = puzz_h + 20, puzz_w

        hbox = QHBoxLayout()
        self._hbox = hbox
        labels_list = []
        is_top_now = True
        counter_top = 0
        counter_bottom = 0
        added_indxes = []
        added_types = []
        for _ in range(len_puzzle_position):
            if is_top_now:
                # top
                s_label = QClickedTriangleLentaLabel(
                    indx=puzzles_top_position[counter_top], current_indx=-1,
                    type_puzzle=FROM_SCROLL_TOP_ELEMENT
                )
                added_indxes.append(puzzles_top_position[counter_top])
                added_types.append(FROM_SCROLL_TOP_ELEMENT)
                counter_top += 1
                if counter_bottom < len(puzzles_bottom_position):
                    is_top_now = not is_top_now
            else:
                # bottom
                s_label = QClickedTriangleLentaLabel(
                    indx=puzzles_bottom_position[counter_bottom],
                    current_indx=-1,
                    type_puzzle=FROM_SCROLL_BOTTOM_ELEMENT
                )
                added_indxes.append(puzzles_bottom_position[counter_bottom])
                added_types.append(FROM_SCROLL_BOTTOM_ELEMENT)

                counter_bottom += 1
                if counter_top < len(puzzles_top_position):
                    is_top_now = not is_top_now

            s_label.setFixedWidth(puzz_scroll_w)
            s_label.setFixedHeight(puzz_scroll_h)
            s_label.setAlignment(Qt.AlignTop)
            labels_list.append(s_label)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSizeConstraint(QLayout.SetMaximumSize)
        hbox.setSpacing(10)
        self._labels_list = labels_list

        self._original_image = io.imread(original_image_path)
        self._original_image_path = original_image_path
        self._origin_h, self._origin_w = self._original_image.shape[:-1]
        self._update_labels(self._original_image, added_indxes, added_types)
        self.setLayout(hbox)

    def _update_labels(self, source_img: np.ndarray, added_indxes: list, added_types: list):
        size = source_img.shape
        puzz_w, puzz_h = FRAME_W // self._size_block_w, FRAME_H // self._size_block_h
        triangles_top_list, triangles_bottom_list, mask = cut_image_into_triangles(
            source_img=source_img,
            size_block_w=self._size_block_w, size_block_h=self._size_block_h,
            thick_of_border_line=ScrolledTriangleFrame.LINE_THICK
        )
        counter = 0
        for i in range(len(added_indxes)):
            qlabel_s = self._labels_list[i]
            self._hbox.addWidget(qlabel_s)
            if added_types[i] == FROM_SCROLL_TOP_ELEMENT:
                qimage = triangles_top_list[added_indxes[i]]
            else:
                qimage = triangles_bottom_list[added_indxes[i]]
            qlabel_s.setPixmap(QPixmap(qimage))

    def _delete_element_from_layout(self, indx_origin, type_puzzle):
        # Delete zone with indx origin
        # TODO: fix, rewrite this
        # Delete from layout
        found_indx = -1
        for i, elem in enumerate(self._labels_list):
            if elem.indx == indx_origin and elem.type_puzzle == type_puzzle:
                found_indx = i
                break

        if found_indx == -1:
            return

        item = self._hbox.takeAt(found_indx)
        widget = item.widget()
        widget.hide()
        if widget:
            del widget
        del item
        del self._labels_list[found_indx]
        #del self._copy_pixmap[indx_origin]

    def _change_part_view(
            self, indx_origin: int, indx_clicked_area: int, type_puzzle: int,
            pixmap: QPixmap):
        # indx_origin where click was performed - origin position on scroll
        # indx_clicked_area where drop on area was performed
        if indx_clicked_area == -1: # i.e. Empty
            self._delete_element_from_layout(indx_origin, type_puzzle)
        else:
            for elem in self._labels_list:
                if elem.indx == indx_origin and elem.type_puzzle == type_puzzle:
                    elem.setPixmap(pixmap)
                    elem.indx = indx_clicked_area
                    break
            #self._labels_list[indx_origin].setPixmap(pixmap)
        #self._update_possition_w_origin(indx_origin, indx_clicked_area)
        self.update()
        print('Change view on scroll')

    def get_game_info(self) -> Tuple[list, list]:
        position_top_indx = []
        position_bottom_indx = []

        for label_s in self._labels_list:
            if label_s.type_puzzle == FROM_SCROLL_TOP_ELEMENT:
                # top
                position_top_indx.append(label_s.indx)
            else:
                # bottom
                position_bottom_indx.append(label_s.indx)

        return position_top_indx, position_bottom_indx

    def update_layout(self):
        step_w = self._origin_w // self._size_block_w
        for i in range(len(self._labels_list)):
            qlabel_s = self._labels_list[i]
            self._hbox.addWidget(qlabel_s)

    def update(self) -> None:
        self.update_layout()
        super().update()

