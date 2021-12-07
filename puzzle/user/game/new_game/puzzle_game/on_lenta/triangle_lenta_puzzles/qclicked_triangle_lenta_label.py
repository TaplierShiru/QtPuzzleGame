import PySide6
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QLabel

from .qdrag_triangle_lenta_frame import DragTriangleLentaFrame


class QClickedTriangleLentaLabel(QLabel):

    def __init__(
            self, indx: int, current_indx: int, type_puzzle: str, **kwargs):
        super().__init__(**kwargs)
        self.setAcceptDrops(True)
        self.indx = indx
        self.current_index = current_indx
        self.type_puzzle = type_puzzle
        self._drag_elem = None

    def mousePressEvent(self, ev:PySide6.QtGui.QMouseEvent) -> None:
        if ev.button() == Qt.LeftButton:
            indx_pressed, current_indx = self.indx, self.current_index
            print(f'Start move with indx={indx_pressed}!')
            self._drag_elem = DragTriangleLentaFrame(
                right_indx=indx_pressed,
                current_indx=current_indx,
                pixmap=self.pixmap().copy(),
                type=self.type_puzzle
            )
            self._drag_elem.dragMoveEvent(None)

