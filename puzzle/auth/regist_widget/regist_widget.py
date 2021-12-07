from PySide6.QtWidgets import QWidget

from .regist import Ui_registWidget
from ..signal_reg_auth import SignalSenderAuth
from ...database import DatabaseController


class QRegistWidget(QWidget):

    SIZE_WINDOW_W = 400
    SIZE_WINDOW_H = 400

    def __init__(self, signal_auth: SignalSenderAuth):
        super().__init__()
        self.ui = Ui_registWidget()
        self.ui.setupUi(self)
        self.signal_auth = signal_auth

        # Buttons
        self.ui.ok_pushButton.clicked.connect(self.ok)
        self.ui.back_pushButton.clicked.connect(self.back)

        # Other settings
        self.setLayout(self.ui.registWidgetGridLayout)

    def back(self):
        self.signal_auth.signal.emit()

    def ok(self):
        if self.ui.password_lineEdit.text() == self.ui.confirmPassword_lineEdit.text():
            DatabaseController.add_user(self.ui.loginLineEdit.text(), self.ui.password_lineEdit.text())
        self.signal_auth.signal.emit()
