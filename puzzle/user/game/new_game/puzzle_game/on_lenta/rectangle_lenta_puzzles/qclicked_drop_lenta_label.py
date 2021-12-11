import PySide6
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from puzzle.user.game.new_game.puzzle_game.common.signals import SignalSenderSendDataImage

from puzzle.user.game.new_game.puzzle_game.common.constants import FROM_SCROLL, FROM_FIELD

from .qdrag_lenta_frame import DragLentaFrame


class QClickedDropLentaLabel(QLabel):

    def __init__(
            self, signal_sender_on_scroll: SignalSenderSendDataImage,
            signal_sender_send_data_image: SignalSenderSendDataImage,
            indx: int, current_indx: int = -1, **kwargs):
        super().__init__(**kwargs)
        self.setAcceptDrops(True)
        self.indx = indx
        self.current_index = current_indx
        self._drag_elem = None
        self.signal_sender_on_scroll = signal_sender_on_scroll
        self.signal_sender_send_data_image = signal_sender_send_data_image

    def mousePressEvent(self, ev:PySide6.QtGui.QMouseEvent) -> None:
        if ev.button() == Qt.LeftButton:
            indx_pressed, current_indx = self.indx, self.current_index
            self._drag_elem = DragLentaFrame(
                right_indx=indx_pressed,
                current_indx=current_indx,
                pixmap=self.pixmap().copy(),
            )
            self._drag_elem.dragMoveEvent(None)

    def dragEnterEvent(self, event:PySide6.QtGui.QDragEnterEvent) -> None:
        event.accept()

    def dragMoveEvent(self, event:PySide6.QtGui.QDragMoveEvent) -> None:
        if self._drag_elem is not None and event.buttons() == Qt.LeftButton:
            self._drag_elem.dragMoveEvent(event)

    def dropEvent(self, event:PySide6.QtGui.QDropEvent) -> None:
        if FROM_SCROLL in event.mimeData().text():
            # Where drop was performed
            pixmap_sended = QPixmap(event.mimeData().imageData())
            indx_origin, indx_current = self.indx, self.current_index
            # Element from scroll area
            # We must swap elements
            # Coords where click from scroll area was performed
            _, indx_clicked_origin, _ = event.mimeData().text().split('_')
            indx_clicked_origin  = int(indx_clicked_origin)
            pixmap_current = self.pixmap().copy()
            self.setPixmap(pixmap_sended)
            if self.current_index == -1:
                indx_current = -1 # Mark as empty
            self.current_index = indx_clicked_origin
            self.signal_sender_on_scroll.signal.emit(indx_clicked_origin, indx_current, pixmap_current)
        else:
            # Where drop was performed
            indx_origin, indx_current = self.indx, self.current_index
            # Take indx which label was clicked first
            indx_clicked_origin, indx_clicked_current = event.mimeData().text().split('_')
            indx_clicked_origin, indx_clicked_current = int(indx_clicked_origin), int(indx_clicked_current)
            pixmap_current = self.pixmap().copy()
            self.setPixmap(QPixmap(event.mimeData().imageData()))
            self.current_index = indx_clicked_current
            # indx origin/current/data
            self.signal_sender_send_data_image.signal.emit(indx_clicked_origin, indx_current, pixmap_current)
        event.setDropAction(Qt.MoveAction)
        event.accept()
        self.update()

