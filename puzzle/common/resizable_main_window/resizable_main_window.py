from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow,  QSizePolicy
from puzzle.common.signals import SignalSenderChangeSizeWidget, SignalSenderShutDown
from .resizable_main_window_init_base import ResizableMainWindowInitBase


class ResizableMainWindow(QMainWindow):

    def __init__(
            self, resizable_init: callable(ResizableMainWindowInitBase),
            allow_exit_button: bool = False, **kwargs):
        super().__init__()
        signal_change_size = SignalSenderChangeSizeWidget()
        signal_change_size.signal.connect(self.change_widget)
        self.__widget_w_resizeble = resizable_init(signal_change_size=signal_change_size, **kwargs)
        self.setCentralWidget(self.__widget_w_resizeble)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.center()
        # Disable hide/expand/close buttons from window
        if allow_exit_button:
            self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        else:
            self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        # ShutDown connect
        signal_shut_down = SignalSenderShutDown()
        signal_shut_down.signal.connect(self.close)
        self.__widget_w_resizeble.set_shut_down_signal(signal_shut_down)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().geometry().center()
        qr.moveCenter(cp)

        self.move(qr.topLeft())

    def change_widget(self, w: int, h: int, window_title: str):
        self.setWindowTitle(str(window_title))
        self.resize(w, h)
        self.center()

