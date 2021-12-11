from PySide6.QtWidgets import QWidget

from puzzle.common.signals import SignalSenderShutDown
from puzzle.common.signals.signal_change_size_form import SignalSenderChangeSizeWidget


class ResizableMainWindowInitBase(QWidget):

    def __init__(self, signal_change_size: SignalSenderChangeSizeWidget, **kwargs):
        super().__init__()
        self.__signal_change_size = signal_change_size
        self.__signal_shut_down: SignalSenderShutDown = None

    def set_shut_down_signal(self, signal_shut_down: SignalSenderShutDown):
        self.__signal_shut_down = signal_shut_down

    def close(self) -> bool:
        res = super().close()
        if self.__signal_shut_down is not None:
            self.__signal_shut_down.signal.emit()
        return res
