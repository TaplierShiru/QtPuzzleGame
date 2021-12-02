import PySide6
from PySide6.QtCore import QPoint, Qt, QMimeData
from PySide6.QtGui import QDrag, QPixmap
from PySide6.QtWidgets import QLabel

from ..utils import FROM_FIELD, FROM_SCROLL


class DragLentaFrame(QLabel):

    def __init__(
            self, right_indx: int, current_indx: int,
            pixmap: QPixmap = None, size_scale: tuple = None, type: str = None):
        super().__init__()
        self._right_indx = right_indx
        self._current_indx = current_indx
        self._type = type
        self.setup(pixmap, size_scale)

    def setup(self, pixmap: QPixmap, size_scale):
        self._original_pixmap = pixmap.copy()
        if size_scale is not None:
            pixmap = pixmap.scaled(size_scale[0], size_scale[1])
        self.pixmap = pixmap

    def dragMoveEvent(self, event: PySide6.QtGui.QDragMoveEvent) -> None:
        mimeData = QMimeData()
        if self._type == FROM_SCROLL:
            text = f'{FROM_SCROLL}_{self._right_indx}_{self._current_indx}'
        elif self._type == FROM_FIELD:
            text = f'{FROM_FIELD}_{self._right_indx}_{self._current_indx}'
        else:
            text = f'{self._right_indx}_{self._current_indx}'
        mimeData.setText(text)
        mimeData.setImageData(self._original_pixmap.toImage())
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(self.pixmap)
        drag.setHotSpot(QPoint(20, 20))#- self.rect().topLeft())
        dragAction = drag.exec(Qt.MoveAction)

