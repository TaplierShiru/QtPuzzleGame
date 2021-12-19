from PySide6.QtCore import QObject, Signal


class SignalSenderAuth(QObject):
    signal = Signal()


class SignalSenderReg(QObject):
    signal = Signal()
    signal_close = Signal()

