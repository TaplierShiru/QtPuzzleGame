from PySide6.QtWidgets import QWidget, QMessageBox

from .regist import Ui_registWidget
from ..signal_reg_auth import SignalSenderAuth
from ...common.qmess_boxes import return_qmess_box_connect_db_error
from ...common.qmess_boxes.qmess_box import return_qmess_box
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
        self.ui.ok_pushButton.clicked.connect(self.clicked_ok)
        self.ui.back_pushButton.clicked.connect(self.clicked_back)

        # Other settings
        self.setLayout(self.ui.registWidgetGridLayout)

        # Additional variables
        self.__qmess_box: QMessageBox = None

    def clicked_back(self):
        self.signal_auth.signal.emit()

    def clicked_ok(self):
        if (len(self.ui.loginLineEdit.text()) < 2) | (len(self.ui.loginLineEdit.text()) > 8):
            self.__qmess_box = return_qmess_box("Ошибка регистрации", "Длина логина должна быть в "
                                                                      "пределах [2-8].",
                                                QMessageBox.Icon.Warning)
            self.__qmess_box.show()
        elif (len(self.ui.password_lineEdit.text()) < 4) | (len(self.ui.password_lineEdit.text()) > 12):
            self.__qmess_box = return_qmess_box("Ошибка регистрации", "Длина пароля должна быть в "
                                                                      "пределах [4-12].",
                                                QMessageBox.Icon.Warning)
            self.__qmess_box.show()
        else:
            if self.ui.password_lineEdit.text() == self.ui.confirmPassword_lineEdit.text():
                result = DatabaseController.add_user(self.ui.loginLineEdit.text(), self.ui.password_lineEdit.text())

                if not result:
                    self.__qmess_box = return_qmess_box("Ошибка регистрации", "Такой пользователь "
                                                                              "уже "
                                                                              "зарегистрирован!",
                                                        QMessageBox.Icon.Warning)
                    self.__qmess_box.show()
                    return
                if result is None:
                    self.__qmess_box = return_qmess_box_connect_db_error()
                    self.__qmess_box.show()
                    return

                self.__qmess_box = return_qmess_box("Сообщение", "Регистрация "
                                                                 "прошла "
                                                                 "успешно!",
                                                    QMessageBox.Icon.Information)
                self.__qmess_box.show()
                self.signal_auth.signal.emit()

            else:
                self.__qmess_box = return_qmess_box("Ошибка регистрации", "Пароли не совпадают!",
                                                    QMessageBox.Icon.Warning)
                self.__qmess_box.show()
