import PySide6
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPixmap

from puzzle.common.signals import SignalSenderPicked, SignalSenderPreview
from .qlabel_picked_image import QLabelPickedImage


class QLabelPickedAndPreviewImage(QLabelPickedImage):

    def __init__(
            self, indx: int, path_to_img: str, img_id: int,
            signal_sender_picked: SignalSenderPicked, signal_preview: SignalSenderPreview):
        super().__init__(
            indx=indx, path_to_img=path_to_img,
            img_id=img_id, signal_sender_picked=signal_sender_picked
        )
        self.signal_preview = signal_preview

    def mousePressEvent(self, ev:PySide6.QtGui.QMouseEvent) -> None:
        if ev.button() == Qt.RightButton:
            self.signal_preview.preview.emit(self.indx)
            print("Show!")
