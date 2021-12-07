from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QPixmap


class SignalSenderSendDataImageTriangle(QObject):
    signal = Signal(int, int, str, QPixmap) # indx origin/current/type/data

