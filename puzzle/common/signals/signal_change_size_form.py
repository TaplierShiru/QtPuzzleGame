from PySide6.QtCore import Signal, QObject


class SignalSenderChangeSizeWidget(QObject):
    signal = Signal(int, int, str) # W/H/Window title

