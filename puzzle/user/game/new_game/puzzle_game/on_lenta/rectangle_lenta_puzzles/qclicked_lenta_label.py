import PySide6
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QLabel
from ..utils import FROM_SCROLL

from .qdrag_lenta_frame import DragLentaFrame


class QClickedLentaLabel(QLabel):

    def __init__(
            self, indx: int, current_indx: int = -1, **kwargs):
        super().__init__(**kwargs)
        self.setAcceptDrops(True)
        self.indx = indx
        self.current_index = current_indx
        self._drag_elem = None

    def mousePressEvent(self, ev:PySide6.QtGui.QMouseEvent) -> None:
        if ev.button() == Qt.LeftButton:
            indx_pressed, current_indx = self.indx, self.current_index
            print(f'Start move with indx={indx_pressed}!')
            self._drag_elem = DragLentaFrame(
                right_indx=indx_pressed,
                current_indx=current_indx,
                pixmap=self.pixmap().copy(),
                type=FROM_SCROLL
            )
            self._drag_elem.dragMoveEvent(None)

