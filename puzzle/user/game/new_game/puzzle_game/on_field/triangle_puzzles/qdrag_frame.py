import PySide6
from PySide6.QtCore import QMimeData, QPoint, Qt
from PySide6.QtGui import QPixmap, QDrag
from PySide6.QtWidgets import QLabel


class DragFrame(QLabel):

    def __init__(
            self, right_indx: int, current_indx: int,
            pixmap: QPixmap = None, size_scale: tuple = None, type: str = None):
        super().__init__()
        self._right_indx = right_indx
        self._current_indx = current_indx
        self._type = type
        self.pixmap: QPixmap = None
        self.setup(pixmap, size_scale)

    def setup(self, pixmap: QPixmap, size_scale):
        self._original_pixmap = pixmap.copy()
        if size_scale is not None:
            pixmap = pixmap.scaled(size_scale[0], size_scale[1])
        self.pixmap: QPixmap = pixmap

    def dragMoveEvent(self, event: PySide6.QtGui.QDragMoveEvent) -> None:
        mimeData = QMimeData()
        text = f'{self._right_indx}_{self._current_indx}'
        mimeData.setText(text)
        mimeData.setImageData(self._original_pixmap.toImage())
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(self.pixmap)
        drag.setHotSpot(QPoint(20, 20))#- self.rect().topLeft())
        dragAction = drag.exec(Qt.MoveAction)
