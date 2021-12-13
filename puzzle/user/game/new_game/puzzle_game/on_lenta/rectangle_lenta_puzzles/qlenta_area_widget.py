import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLayout, QMessageBox
from skimage import io

from puzzle.common.qmess_boxes import return_qmess_box_connect_db_error
from puzzle.database import DatabaseController
from puzzle.user.game.new_game.puzzle_game.common.signals import SignalSenderSendDataImage
from puzzle.user.game.new_game.puzzle_game.on_lenta.rectangle_lenta_puzzles.qclicked_lenta_label import \
    QClickedLentaLabel

from puzzle.utils import FRAME_H, FRAME_W, cut_image_into_rectangles


class ScrolledRectangleFrame(QFrame):

    LINE_THICK = 3

    def __init__(
            self, original_image_path: str,
            size_block_w: int, size_block_h: int,
            signal_sender_on_scroll: SignalSenderSendDataImage,
            game_config: str = None):
        super().__init__()
        self.setAcceptDrops(True)
        self._qmess_box: QMessageBox = None

        if game_config is None:
            puzzles_position = list(range(size_block_h * size_block_w))
        else:
            # Parse config
            puzzles_position = DatabaseController.parse_lenta_scroll_rectangle_config(game_config)

            if puzzles_position is None:
                self._qmess_box = return_qmess_box_connect_db_error()
                self._qmess_box.show()
                return

        len_puzzle_position = len(puzzles_position)

        self._size_block_w = size_block_w
        self._size_block_h = size_block_h

        self.signal_sender_on_scroll = signal_sender_on_scroll
        self.signal_sender_on_scroll.signal.connect(self._change_part_view)

        puzz_w, puzz_h = FRAME_W // self._size_block_w, FRAME_H // self._size_block_h
        puzz_scroll_h, puzz_scroll_w = puzz_h + 20, puzz_w

        hbox = QHBoxLayout()
        self._hbox = hbox
        labels_list = []
        for i in range(len_puzzle_position):
            s_label = QClickedLentaLabel(indx=puzzles_position[i])
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
        self._update_labels(self._original_image, puzzles_position)
        self.setLayout(hbox)

    def _update_labels(self, source_img: np.ndarray, puzzles_position: list):
        puzz_w, puzz_h = FRAME_W // self._size_block_w, FRAME_H // self._size_block_h

        peases_list = cut_image_into_rectangles(
            source_img=source_img,
            size_block_w=self._size_block_w, size_block_h=self._size_block_h,
            thick_of_border_line=ScrolledRectangleFrame.LINE_THICK,
            resize_to=(puzz_h, puzz_w)
        )
        for i in range(len(puzzles_position)):
            qlabel_s = self._labels_list[i]
            self._hbox.addWidget(qlabel_s)
            qimage = peases_list[puzzles_position[i]]
            qlabel_s.setPixmap(QPixmap(qimage))

    def _delete_element_from_layout(self, indx_origin):
        # Delete zone with indx origin
        # Delete from layout
        found_indx = -1
        for i, elem in enumerate(self._labels_list):
            if elem.indx == indx_origin:
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

    def _change_part_view(
            self, indx_origin: int, indx_clicked_area: int,
            pixmap: QPixmap):
        # indx_origin where click was performed - origin position on scroll
        # indx_clicked_area where drop on area was performed
        if indx_clicked_area == -1: # i.e. Empty
            self._delete_element_from_layout(indx_origin)
        else:
            for elem in self._labels_list:
                if elem.indx == indx_origin:
                    elem.setPixmap(pixmap)
                    elem.indx = indx_clicked_area
                    break
        self.update()

    def get_game_info(self) -> list:
        indx_position = []
        for i in range(len(self._labels_list)):
                indx_position.append(self._labels_list[i].indx)
        return indx_position

    def update_layout(self):
        step_w = self._origin_w // self._size_block_w
        for i in range(len(self._labels_list)):
            qlabel_s = self._labels_list[i]
            self._hbox.addWidget(qlabel_s)

    def update(self) -> None:
        self.update_layout()
        super().update()

