import PySide6
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtWidgets import QLabel, QGraphicsColorizeEffect, QSizePolicy

from ..signals import SignalSenderPicked


class QLabelPickedImage(QLabel):

    def __init__(
            self, indx: int, path_to_img: str, img_name: str,
            img_id: int, signal_sender_picked: SignalSenderPicked):
        super().__init__()
        self.indx = indx
        self.path_to_img = path_to_img
        self.img_id = img_id
        self.signal_sender_picked = signal_sender_picked
        self.img_name = img_name
        pixmap = QPixmap(path_to_img)
        pixmap = pixmap.scaled(120, 120, aspectMode=Qt.IgnoreAspectRatio)
        self.setPixmap(pixmap)
        self.setFixedWidth(120)
        self.setFixedHeight(120)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(120, 120)

        effect = QGraphicsColorizeEffect()
        effect.setColor(QColor(255, 0, 0))
        self.setGraphicsEffect(effect)
        self.graphicsEffect()

        self.effect = effect
        self.is_pressed = True
        self.switch_effect()

    def mouseDoubleClickEvent(self, event:PySide6.QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.switch_effect()
            self.signal_sender_picked.signal.emit(self.indx)
            print('Click, indx: ', self.indx)

    def switch_effect(self):
        self.is_pressed = not self.is_pressed
        self.effect.setEnabled(self.is_pressed)
