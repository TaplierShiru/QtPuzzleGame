# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regist.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_registWidget(object):
    def setupUi(self, registWidget):
        if not registWidget.objectName():
            registWidget.setObjectName(u"registWidget")
        registWidget.resize(592, 461)
        self.gridLayoutWidget = QWidget(registWidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 571, 421))
        self.registWidgetGridLayout = QGridLayout(self.gridLayoutWidget)
        self.registWidgetGridLayout.setObjectName(u"registWidgetGridLayout")
        self.registWidgetGridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.registWidgetGridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer4 = QSpacerItem(60, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.registWidgetGridLayout.addItem(self.verticalSpacer4, 15, 3, 1, 1)

        self.ok_pushButton = QPushButton(self.gridLayoutWidget)
        self.ok_pushButton.setObjectName(u"ok_pushButton")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ok_pushButton.setFont(font)

        self.registWidgetGridLayout.addWidget(self.ok_pushButton, 17, 4, 1, 1)

        self.confirmPassword_label = QLabel(self.gridLayoutWidget)
        self.confirmPassword_label.setObjectName(u"confirmPassword_label")
        self.confirmPassword_label.setFont(font)
        self.confirmPassword_label.setAlignment(Qt.AlignCenter)

        self.registWidgetGridLayout.addWidget(self.confirmPassword_label, 13, 3, 1, 1)

        self.verticalSpacer2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.registWidgetGridLayout.addItem(self.verticalSpacer2, 7, 3, 1, 1)

        self.back_pushButton = QPushButton(self.gridLayoutWidget)
        self.back_pushButton.setObjectName(u"back_pushButton")
        self.back_pushButton.setMinimumSize(QSize(0, 0))
        self.back_pushButton.setFont(font)

        self.registWidgetGridLayout.addWidget(self.back_pushButton, 17, 2, 1, 1)

        self.horizontalSpacer3 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.registWidgetGridLayout.addItem(self.horizontalSpacer3, 22, 5, 1, 1)

        self.loginLineEdit = QLineEdit(self.gridLayoutWidget)
        self.loginLineEdit.setObjectName(u"loginLineEdit")

        self.registWidgetGridLayout.addWidget(self.loginLineEdit, 6, 3, 1, 1)

        self.password_label = QLabel(self.gridLayoutWidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMinimumSize(QSize(215, 20))
        self.password_label.setMaximumSize(QSize(16777215, 20))
        self.password_label.setFont(font)
        self.password_label.setAlignment(Qt.AlignCenter)

        self.registWidgetGridLayout.addWidget(self.password_label, 9, 3, 1, 1, Qt.AlignHCenter)

        self.password_lineEdit = QLineEdit(self.gridLayoutWidget)
        self.password_lineEdit.setObjectName(u"password_lineEdit")

        self.registWidgetGridLayout.addWidget(self.password_lineEdit, 11, 3, 1, 1)

        self.login_label = QLabel(self.gridLayoutWidget)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setMinimumSize(QSize(215, 20))
        self.login_label.setMaximumSize(QSize(16777215, 20))
        self.login_label.setFont(font)
        self.login_label.setAlignment(Qt.AlignCenter)

        self.registWidgetGridLayout.addWidget(self.login_label, 4, 3, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer1 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.registWidgetGridLayout.addItem(self.verticalSpacer1, 2, 3, 1, 1)

        self.verticalSpacer5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.registWidgetGridLayout.addItem(self.verticalSpacer5, 22, 3, 1, 1)

        self.horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.registWidgetGridLayout.addItem(self.horizontalSpacer2, 17, 3, 1, 1)

        self.horizontalSpacer1 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.registWidgetGridLayout.addItem(self.horizontalSpacer1, 22, 0, 1, 1)

        self.regTitle_label = QLabel(self.gridLayoutWidget)
        self.regTitle_label.setObjectName(u"regTitle_label")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.regTitle_label.setFont(font1)
        self.regTitle_label.setScaledContents(False)
        self.regTitle_label.setAlignment(Qt.AlignCenter)
        self.regTitle_label.setMargin(0)

        self.registWidgetGridLayout.addWidget(self.regTitle_label, 1, 3, 1, 1)

        self.confirmPassword_lineEdit = QLineEdit(self.gridLayoutWidget)
        self.confirmPassword_lineEdit.setObjectName(u"confirmPassword_lineEdit")

        self.registWidgetGridLayout.addWidget(self.confirmPassword_lineEdit, 14, 3, 1, 1)

        self.verticalSpacer3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.registWidgetGridLayout.addItem(self.verticalSpacer3, 12, 3, 1, 1)


        self.retranslateUi(registWidget)

        QMetaObject.connectSlotsByName(registWidget)
    # setupUi

    def retranslateUi(self, registWidget):
        registWidget.setWindowTitle(QCoreApplication.translate("registWidget", u"\u041e\u043a\u043d\u043e \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438", None))
        self.ok_pushButton.setText(QCoreApplication.translate("registWidget", u"\u041e\u041a", None))
        self.confirmPassword_label.setText(QCoreApplication.translate("registWidget", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.back_pushButton.setText(QCoreApplication.translate("registWidget", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.password_label.setText(QCoreApplication.translate("registWidget", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.login_label.setText(QCoreApplication.translate("registWidget", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.regTitle_label.setText(QCoreApplication.translate("registWidget", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

