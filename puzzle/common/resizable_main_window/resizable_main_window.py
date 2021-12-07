from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow,  QSizePolicy
from puzzle.common.signals.signal_change_size_form import SignalSenderChangeSizeWidget
from puzzle.common.menu_controller_base import MenuControllerBase


class ResizableMainWindow(QMainWindow):

    def __init__(self, menu_controller_type: callable(MenuControllerBase), allow_exit_button: bool = False):
        super().__init__()
        signal_change_size = SignalSenderChangeSizeWidget()
        signal_change_size.signal.connect(self.change_widget)
        self._menu_controller = menu_controller_type(signal_change_size=signal_change_size)
        self.setCentralWidget(self._menu_controller)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.center()
        # Disable hide/expand/close buttons from window
        if allow_exit_button:
            self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        else:
            self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
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
