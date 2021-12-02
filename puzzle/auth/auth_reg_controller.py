from PySide6.QtWidgets import QWidget, QGridLayout, QStackedWidget

from .auth_widget import QAuthWidget
from .regist_widget import QRegistWidget
from .signal_reg_auth import SignalSenderAuth, SignalSenderReg

class AuthRegController(QWidget):

    def __init__(self):
        super().__init__()

        self.signal_auth = SignalSenderAuth()
        self.signal_reg = SignalSenderReg()

        self.signal_auth.signal.connect(self.show_auth)
        self.signal_reg.signal.connect(self.show_reg)

        self.setupUI()

    def setupUI(self):
        grid = QGridLayout()
        stacked_widget = QStackedWidget()

        # Init auth, 0
        auth = QAuthWidget(signal_reg=self.signal_reg)
        stacked_widget.addWidget(auth)

        # Init regist, 1
        regist = QRegistWidget(signal_auth=self.signal_auth)
        stacked_widget.addWidget(regist)

        stacked_widget.setCurrentIndex(0)
        self._stacked_widget = stacked_widget
        grid.addWidget(stacked_widget, 0, 0)
        self.setLayout(grid)

    def show_auth(self):
        self._stacked_widget.setCurrentIndex(0)

    def show_reg(self):
        self._stacked_widget.setCurrentIndex(1)
