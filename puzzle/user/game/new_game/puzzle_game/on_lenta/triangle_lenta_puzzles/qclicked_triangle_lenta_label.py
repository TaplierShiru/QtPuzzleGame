import PySide6
from PySide6.QtGui import Qt, QPixmap
from PySide6.QtWidgets import QLabel

from puzzle.utils.image_cutter_tools import get_triangle_img_wo_border
from .qdrag_triangle_lenta_frame import DragTriangleLentaFrame
from ...common.constants import FROM_SCROLL_BOTTOM_ELEMENT


class QClickedTriangleLentaLabel(QLabel):

    def __init__(
            self, indx: int, current_indx: int, type_puzzle: str, pixmap_send: QPixmap = None, **kwargs):
        super().__init__(**kwargs)
        self.setAcceptDrops(True)
        self.indx = indx
        self.mask = None
        self.current_index = current_indx
        self.type_puzzle = type_puzzle
        self.pixmap_send = pixmap_send
        self._drag_elem = None

    def mousePressEvent(self, ev:PySide6.QtGui.QMouseEvent) -> None:
        if ev.button() == Qt.LeftButton:
            indx_pressed, current_indx = self.indx, self.current_index
            self._drag_elem = DragTriangleLentaFrame(
                right_indx=indx_pressed,
                current_indx=current_indx,
                pixmap=self.pixmap_send,
                pixmap_drag=self.pixmap().copy(),
                type=self.type_puzzle
            )
            self._drag_elem.dragMoveEvent(None)

    def update(self) -> None:
        assert self.pixmap_send is not None and self.mask is not None
        if self.type_puzzle == FROM_SCROLL_BOTTOM_ELEMENT:
            val = 1
        else:
            val = 0

        pixmap_drag = get_triangle_img_wo_border(self.mask.copy(), self.pixmap_send.copy(), val)
        self.setPixmap(pixmap_drag)

