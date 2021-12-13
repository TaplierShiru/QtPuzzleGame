import PySide6
from PySide6.QtCore import QPoint, Qt, QMimeData
from PySide6.QtGui import QDrag, QPixmap
from PySide6.QtWidgets import QLabel

from puzzle.user.game.new_game.puzzle_game.common.constants import (FROM_SCROLL_BOTTOM_ELEMENT, FROM_SCROLL_TOP_ELEMENT,
                                                                    TOP_ELEMENT, BOTTOM_ELEMENT)


class DragTriangleLentaFrame(QLabel):

    def __init__(
            self, right_indx: int, current_indx: int,
            pixmap: QPixmap = None, pixmap_drag: QPixmap = None,
            size_scale: tuple = None, type: str = None):
        super().__init__()
        self._right_indx = right_indx
        self._current_indx = current_indx
        self._type = type

        if pixmap_drag is None:
            pixmap_drag = pixmap

        self.setup(pixmap, pixmap_drag, size_scale)

    def setup(self, pixmap: QPixmap, pixmap_drag: QPixmap, size_scale):
        self._original_pixmap = pixmap
        if size_scale is not None:
            pixmap_drag = pixmap_drag.scaled(size_scale[0], size_scale[1])
        self.pixmap = pixmap_drag

    def dragMoveEvent(self, event: PySide6.QtGui.QDragMoveEvent) -> None:
        mimeData = QMimeData()
        if self._type == FROM_SCROLL_BOTTOM_ELEMENT or self._type == FROM_SCROLL_TOP_ELEMENT or \
                self._type == TOP_ELEMENT or self._type == BOTTOM_ELEMENT:
            text = f'{self._type}_{self._right_indx}_{self._current_indx}'
        else:
            text = f'{self._right_indx}_{self._current_indx}'
        mimeData.setText(text)
        mimeData.setImageData(self._original_pixmap.toImage())
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(self.pixmap)
        drag.setHotSpot(QPoint(20, 20))#- self.rect().topLeft())
        dragAction = drag.exec(Qt.MoveAction)

