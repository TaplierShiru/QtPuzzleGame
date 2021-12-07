import PySide6
import numpy as np
from PySide6.QtCore import QRect, QPoint
from PySide6.QtGui import QPixmap, Qt, QPainter, QImage
from PySide6.QtWidgets import QLabel

from puzzle.user.game.new_game.puzzle_game.common.signals import SignalSenderSendDataImageTriangle
from .qdrag_triangle_frame import DragTriangleFrame

from puzzle.user.game.new_game.puzzle_game.common.constants import TOP_ELEMENT, BOTTOM_ELEMENT


class QClickedDropTriangleLabel(QLabel):

    def __init__(
            self, signal_sender_send_data_image: SignalSenderSendDataImageTriangle,
            indx_top: int, indx_bot: int, mask: np.ndarray = None,
            current_indx_top: int = -1, current_indx_bot: int = -1,
            pixmap_top: QPixmap = None, pixmap_bot: QPixmap = None, **kwargs):
        super().__init__(**kwargs)
        self.setAcceptDrops(True)
        self.indx_top = indx_top
        self.indx_bot = indx_bot
        self.mask = mask
        self.current_indx_top = current_indx_top
        self.current_indx_bot = current_indx_bot

        self.pixmap_top = pixmap_top
        self.pixmap_bot = pixmap_bot
        self.combine_pixmap()

        self.w, self.h = None, None

        self._drag_elem = None
        self.signal_sender_send_data_image = signal_sender_send_data_image

    def combine_pixmap(self):
        if self.pixmap_top is None or self.pixmap_bot is None:
            return

        if self.w is None or self.h is None:
            return

        combine = QImage(self.w, self.h, self.pixmap_top.toImage().format())
        p = QPainter(combine)
        p.setCompositionMode(QPainter.CompositionMode_SourceOver)
        p.drawImage(QRect(QPoint(0, 0), combine.size()), self.pixmap_top.toImage())
        p.drawImage(QRect(QPoint(0, 0), combine.size()), self.pixmap_bot.toImage())
        p.end()
        self.setPixmap(QPixmap(combine))

    def mousePressEvent(self, ev:PySide6.QtGui.QMouseEvent) -> None:
        if ev.button() == Qt.LeftButton:
            x,y = int(ev.position().x()), int(ev.position().y())
            print(f"x:{x} y:{y}")
            print(self.mask[y, x])
            if self.mask[y, x] == 0:
                pixmap = self.pixmap_top.copy()
                indx_pressed, current_indx = self.indx_top, self.current_indx_top
                type_puzzle = TOP_ELEMENT
            else:
                pixmap = self.pixmap_bot.copy()
                indx_pressed, current_indx = self.indx_bot, self.current_indx_bot
                type_puzzle = BOTTOM_ELEMENT
            print(f'Start move with indx={indx_pressed}!')
            self._drag_elem = DragTriangleFrame(
                right_indx=indx_pressed,
                current_indx=current_indx,
                pixmap=pixmap,
                type=type_puzzle
            )
            self._drag_elem.dragMoveEvent(None)

    def dragEnterEvent(self, event: PySide6.QtGui.QDragEnterEvent) -> None:
        event.accept()

    def dragMoveEvent(self, event: PySide6.QtGui.QDragMoveEvent) -> None:
        if self._drag_elem is not None and event.buttons() == Qt.LeftButton:
            self._drag_elem.dragMoveEvent(event)

    def dropEvent(self, event: PySide6.QtGui.QDropEvent) -> None:
        print('READY TO DROP')
        # Where drop was performed
        x, y = int(event.position().x()), int(event.position().y())
        print(f"x:{x} y:{y}")
        print(self.mask[y, x])
        if self.mask[y, x] == 0:
            pixmap_current = self.pixmap_top.copy()
            indx_origin, indx_current = self.indx_top, self.current_indx_top
            type_set_to_puzzle = TOP_ELEMENT
        else:
            pixmap_current = self.pixmap_bot.copy()
            indx_origin, indx_current = self.indx_bot, self.current_indx_bot
            type_set_to_puzzle = BOTTOM_ELEMENT
        # Take indx which label was clicked first
        type_drop_puzzle, indx_clicked_origin, indx_clicked_current = event.mimeData().text().split('_')
        indx_clicked_origin, indx_clicked_current = int(indx_clicked_origin), int(indx_clicked_current)
        if type_set_to_puzzle == type_drop_puzzle and type_drop_puzzle == BOTTOM_ELEMENT:
            self.pixmap_bot = QPixmap(event.mimeData().imageData())
            self.current_indx_bot = indx_clicked_current
        elif type_set_to_puzzle == type_drop_puzzle and type_drop_puzzle == TOP_ELEMENT:
            self.pixmap_top = QPixmap(event.mimeData().imageData())
            self.current_indx_top = indx_clicked_current
        else:
            return # Deny drop
        self.combine_pixmap()
        # indx origin/current/data
        self.signal_sender_send_data_image.signal.emit(
            indx_clicked_origin, indx_current,
            type_drop_puzzle, pixmap_current
        )
        event.setDropAction(Qt.MoveAction)
        event.accept()
        self.update()

