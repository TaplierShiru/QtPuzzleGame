from PySide6.QtCore import QObject, Signal


class SignalSenderShutDown(QObject):
    signal = Signal()
