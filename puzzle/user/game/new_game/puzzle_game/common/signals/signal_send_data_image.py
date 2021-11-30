from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QPixmap


class SignalSenderSendDataImage(QObject):
    signal = Signal(int, int, QPixmap) # indx origin/current/data

