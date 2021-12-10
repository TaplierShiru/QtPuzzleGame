from PySide6.QtWidgets import QWidget, QMessageBox
from .auth import Ui_authWidget
from ..signal_reg_auth import SignalSenderReg
from ...common.qmess_boxes import return_qmess_box_connect_db_error
from ...database import DatabaseController


class QAuthWidget(QWidget):

    SIZE_WINDOW_W = 400
    SIZE_WINDOW_H = 400

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

        # Additional variables
        self._qmess_box: QMessageBox = None

    def login(self):
        result = DatabaseController.find_user(self.ui.login_lineEdit.text(), self.ui.password_lineEdit.text())

        if result is None:
            self._qmess_box = return_qmess_box_connect_db_error()
            self._qmess_box.show()
            return

        if result:
            print('login in game')
            role = DatabaseController.get_role_user(self.ui.login_lineEdit.text())

            if role is None:
                self._qmess_box = return_qmess_box_connect_db_error()
                self._qmess_box.show()
                return
        else:
            print('Wrong!!')

    def reg(self):
        self.signal_reg.signal.emit()
