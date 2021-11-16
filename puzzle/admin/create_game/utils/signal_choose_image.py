from PySide6.QtCore import QObject, Signal


class SignalSenderChooseImage(QObject):
    signal = Signal(int) # Id of image in DataBase


