from PySide6.QtCore import QObject, Signal


class SignalSenderChooseImage(QObject):
    signal = Signal(str) # Id of image in DataBase


