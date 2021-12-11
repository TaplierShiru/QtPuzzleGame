from PySide6.QtWidgets import QWidget, QMessageBox
from .auth import Ui_authWidget
from ..signal_reg_auth import SignalSenderReg
from ...common.qmess_boxes import return_qmess_box_connect_db_error
from ...common.qmess_boxes.qmess_box import return_qmess_box
from ...database import DatabaseController

from puzzle.global_controllers.menu_controller import MenuController
from puzzle.utils import ROLE_USER, ROLE_ADMIN


class QAuthWidget(QWidget):

    SIZE_WINDOW_W = 400
    SIZE_WINDOW_H = 400

    def __init__(self, signal_reg: SignalSenderReg):
        super().__init__()
        self.ui = Ui_authWidget()
        self.ui.setupUi(self)
        self.signal_reg = signal_reg

        # Buttons
        self.ui.reg_pushButton.clicked.connect(self.clicked_reg)
        self.ui.login_pushButton.clicked.connect(self.clicked_login)

        # Other settings
        self.setLayout(self.ui.authWidgetGridLayout)

        # Additional variables
        self.__qmess_box: QMessageBox = None
        self.__menu_widget = None

    def clicked_login(self):
        login = self.ui.login_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        result = DatabaseController.find_user(login, password)

        if result is None:
            self.__qmess_box = return_qmess_box_connect_db_error()
            self.__qmess_box.show()
            return

        if result:
            role = DatabaseController.get_role_user(login)

            if role is None:
                self.__qmess_box = return_qmess_box_connect_db_error()
                self.__qmess_box.show()
                return

            menu_widget = MenuController.get_widget_by_role(user_login=login, role=role)
            if menu_widget is None:
                self.__qmess_box = return_qmess_box("Ошибка входа", "Ошибка создания формы.",
                                                    QMessageBox.Icon.Warning)
                self.__qmess_box.show()
                return
            menu_widget.show()
            self.__menu_widget = menu_widget

        else:
            self.__qmess_box = return_qmess_box("Ошибка входа", "Неправильный логин/пароль.",
                                                QMessageBox.Icon.Warning)
            self.__qmess_box.show()

    def clicked_reg(self):
        self.signal_reg.signal.emit()
