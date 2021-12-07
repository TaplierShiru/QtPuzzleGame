from PySide6.QtCore import QObject, Signal


class SignalSenderPreview(QObject):
    #               indx
    preview = Signal(int)
