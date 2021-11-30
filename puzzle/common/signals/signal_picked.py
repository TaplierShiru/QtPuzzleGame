from PySide6.QtCore import QObject, Signal


class SignalSenderPicked(QObject):
    signal = Signal(int) # indx picked
