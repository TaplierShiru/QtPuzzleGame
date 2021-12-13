import PySide6
import numpy as np
from PySide6.QtCore import Qt, QRect, QPoint
from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtWidgets import QLabel

from puzzle.user.game.new_game.puzzle_game.common.signals import SignalSenderSendDataImageTriangle
from puzzle.utils.image_cutter_tools import get_triangle_img_wo_border
from .qdrag_triangle_lenta_frame import DragTriangleLentaFrame
from puzzle.user.game.new_game.puzzle_game.common.constants import (FROM_SCROLL_TOP_ELEMENT, FROM_SCROLL_BOTTOM_ELEMENT, \
                                                                    TOP_ELEMENT, BOTTOM_ELEMENT, FROM_SCROLL)


class QClickedDropTriangleLentaLabel(QLabel):

    def __init__(
            self, signal_sender_on_scroll: SignalSenderSendDataImageTriangle,
            signal_sender_send_data_image: SignalSenderSendDataImageTriangle,
            indx_top: int, indx_bot: int, mask: np.ndarray = None,
            current_indx_top: int = -1, current_indx_bot: int = -1,
            pixmap_top: QPixmap = None, pixmap_bot: QPixmap = None,
            pixmap_empty: QPixmap = None, **kwargs):
        super().__init__(**kwargs)
        self.setAcceptDrops(True)
        self.indx_top = indx_top
        self.indx_bot = indx_bot
        self.mask = mask
        self.pixmap_empty = pixmap_empty
        self.current_indx_top = current_indx_top
        self.current_indx_bot = current_indx_bot

        self.pixmap_top = pixmap_top
        self.pixmap_bot = pixmap_bot
        self.combine_pixmap()

        self.w, self.h = None, None

        self._drag_elem = None
        self.signal_sender_on_scroll = signal_sender_on_scroll
        self.signal_sender_send_data_image = signal_sender_send_data_image

    def combine_pixmap(self):
        if self.pixmap_top is None and self.pixmap_bot is None:
            self.setPixmap(self.pixmap_empty)
            return

        if self.w is None or self.h is None:
            return

        if self.pixmap_top is None and self.pixmap_bot is not None:
            self.setPixmap(self.pixmap_bot)
            return

        if self.pixmap_bot is None and self.pixmap_top is not None:
            self.setPixmap(self.pixmap_top)
            return

        combine = QImage(self.w, self.h, QImage.Format_ARGB32)
        p = QPainter(combine)
        p.setCompositionMode(QPainter.CompositionMode_SourceOver)
        if self.pixmap_bot is not None:
            p.drawImage(QRect(QPoint(0, 0), combine.size()), self.pixmap_bot.toImage().convertToFormat(QImage.Format_ARGB32))
        if self.pixmap_top is not None:
            p.drawImage(QRect(QPoint(0, 0), combine.size()), self.pixmap_top.toImage().convertToFormat(QImage.Format_ARGB32))
        p.end()
        self.setPixmap(QPixmap(combine))

    def mousePressEvent(self, ev:PySide6.QtGui.QMouseEvent) -> None:
        if ev.button() == Qt.LeftButton:
            x,y = int(ev.position().x()), int(ev.position().y())
            if self.mask[y, x] == 0:
                if self.pixmap_top is None:
                    return

                pixmap = self.pixmap_top.copy()
                indx_pressed, current_indx = self.indx_top, self.current_indx_top
                type_puzzle = TOP_ELEMENT
                val = 0
            else:
                if self.pixmap_bot is None:
                    return

                pixmap = self.pixmap_bot.copy()
                indx_pressed, current_indx = self.indx_bot, self.current_indx_bot
                type_puzzle = BOTTOM_ELEMENT
                val = 1
            pixmap_drag = get_triangle_img_wo_border(self.mask, pixmap, val)
            self._drag_elem = DragTriangleLentaFrame(
                right_indx=indx_pressed,
                current_indx=current_indx,
                pixmap=pixmap,
                pixmap_drag=pixmap_drag,
                type=type_puzzle
            )
            self._drag_elem.dragMoveEvent(None)

    def dragEnterEvent(self, event:PySide6.QtGui.QDragEnterEvent) -> None:
        event.accept()

    def dragMoveEvent(self, event:PySide6.QtGui.QDragMoveEvent) -> None:
        if self._drag_elem is not None and event.buttons() == Qt.LeftButton:
            self._drag_elem.dragMoveEvent(event)

    def dropEvent(self, event:PySide6.QtGui.QDropEvent) -> None:
        # Where drop was performed
        x, y = int(event.position().x()), int(event.position().y())
        if self.mask[y, x] == 0:
            type_set_to_puzzle = TOP_ELEMENT
        else:
            type_set_to_puzzle = BOTTOM_ELEMENT
        if FROM_SCROLL in event.mimeData().text():
            # Element from scroll area
            # We must swap elements
            # Coords where click from scroll area was performed
            type_drop_puzzle, indx_clicked_origin, _ = event.mimeData().text().split('_')
            indx_clicked_origin  = int(indx_clicked_origin)

            if type_set_to_puzzle == BOTTOM_ELEMENT and type_drop_puzzle == FROM_SCROLL_BOTTOM_ELEMENT:
                if self.pixmap_bot is None:
                    send_pixmap = None
                else:
                    send_pixmap = self.pixmap_bot.copy()
                self.pixmap_bot = QPixmap(event.mimeData().imageData())
                indx_current = self.current_indx_bot
                self.current_indx_bot = indx_clicked_origin
            elif type_set_to_puzzle == TOP_ELEMENT and type_drop_puzzle == FROM_SCROLL_TOP_ELEMENT:
                if self.pixmap_top is None:
                    send_pixmap = None
                else:
                    send_pixmap = self.pixmap_top.copy()
                self.pixmap_top = QPixmap(event.mimeData().imageData())
                indx_current = self.current_indx_top
                self.current_indx_top = indx_clicked_origin
            else:
                return  # Deny drop
            self.signal_sender_on_scroll.signal.emit(indx_clicked_origin, indx_current, type_drop_puzzle, send_pixmap)
        else:
            if self.mask[y, x] == 0:
                if self.pixmap_top is None:
                    pixmap_current = None
                else:
                    pixmap_current = self.pixmap_top.copy()
                indx_origin, indx_current = self.indx_top, self.current_indx_top
            else:
                if self.pixmap_bot is None:
                    pixmap_current = None
                else:
                    pixmap_current = self.pixmap_bot.copy()
                indx_origin, indx_current = self.indx_bot, self.current_indx_bot
            # Take indx which label was clicked first
            type_drop_puzzle, indx_clicked_origin, indx_clicked_current = event.mimeData().text().split('_')

            if indx_clicked_current == -1 and pixmap_current is None:
                return # Empty swap to empty

            indx_clicked_origin, indx_clicked_current = int(indx_clicked_origin), int(indx_clicked_current)
            if type_set_to_puzzle == type_drop_puzzle and type_drop_puzzle == BOTTOM_ELEMENT:
                self.pixmap_bot = QPixmap(event.mimeData().imageData())
                self.current_indx_bot = indx_clicked_current
            elif type_set_to_puzzle == type_drop_puzzle and type_drop_puzzle == TOP_ELEMENT:
                self.pixmap_top = QPixmap(event.mimeData().imageData())
                self.current_indx_top = indx_clicked_current
            else:
                return  # Deny drop
            # indx origin/current/data
            self.signal_sender_send_data_image.signal.emit(
                indx_clicked_origin, indx_current,
                type_drop_puzzle, pixmap_current
            )
        self.combine_pixmap()
        event.setDropAction(Qt.MoveAction)
        event.accept()
        self.update()

