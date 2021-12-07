from puzzle.common.signals.signal_change_size_form import SignalSenderChangeSizeWidget
from PySide6.QtWidgets import QWidget


class MenuControllerBase(QWidget):

    def __init__(self, signal_change_size: SignalSenderChangeSizeWidget, **kwargs):
        super().__init__()
        self.signal_change_size = signal_change_size



