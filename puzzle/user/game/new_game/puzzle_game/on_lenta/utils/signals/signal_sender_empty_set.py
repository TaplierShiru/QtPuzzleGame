from PySide6.QtCore import QObject, Signal


class SignalSenderEmptySet(QObject):
    signal = Signal(int) # Indx set
