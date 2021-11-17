from PySide6.QtWidgets import QWidget
from .auth import Ui_authWidget
from ..signal_reg_auth import SignalSenderReg
from ...database import DatabaseController


class QAuthWidget(QWidget):

    def __init__(self, signal_reg: SignalSenderReg):
        super().__init__()
        self.ui = Ui_authWidget()
        self.ui.setupUi(self)
        self.signal_reg = signal_reg

        # Buttons
        self.ui.reg_pushButton.clicked.connect(self.reg)
        self.ui.login_pushButton.clicked.connect(self.login)

        # Other settings
        self.setLayout(self.ui.authWidgetGridLayout)

    def login(self):
        if DatabaseController.find_user(self.ui.login_lineEdit.text(), self.ui.password_lineEdit.text()):
            print('login in game')
        else:
            print('Wrong!!')

    def reg(self):
        self.signal_reg.signal.emit()
