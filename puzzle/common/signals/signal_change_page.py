from PySide6.QtCore import QObject, Signal


class SignalSenderChangePage(QObject):
    signal = Signal(int) # Number of page
