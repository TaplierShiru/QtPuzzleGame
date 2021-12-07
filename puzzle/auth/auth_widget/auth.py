# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_authWidget(object):
    def setupUi(self, authWidget):
        if not authWidget.objectName():
            authWidget.setObjectName(u"authWidget")
        authWidget.resize(592, 461)
        self.gridLayoutWidget = QWidget(authWidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 571, 421))
        self.authWidgetGridLayout = QGridLayout(self.gridLayoutWidget)
        self.authWidgetGridLayout.setObjectName(u"authWidgetGridLayout")
        self.authWidgetGridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.authWidgetGridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer1 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.authWidgetGridLayout.addItem(self.verticalSpacer1, 2, 3, 1, 1)

        self.password_lineEdit = QLineEdit(self.gridLayoutWidget)
        self.password_lineEdit.setObjectName(u"password_lineEdit")

        self.authWidgetGridLayout.addWidget(self.password_lineEdit, 11, 3, 1, 1)

        self.puzzleTitle_label = QLabel(self.gridLayoutWidget)
        self.puzzleTitle_label.setObjectName(u"puzzleTitle_label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.puzzleTitle_label.setFont(font)
        self.puzzleTitle_label.setScaledContents(False)
        self.puzzleTitle_label.setAlignment(Qt.AlignCenter)
        self.puzzleTitle_label.setMargin(0)

        self.authWidgetGridLayout.addWidget(self.puzzleTitle_label, 1, 3, 1, 1)

        self.horizontalSpacer2 = QSpacerItem(262, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.authWidgetGridLayout.addItem(self.horizontalSpacer2, 14, 3, 1, 1)

        self.horizontalSpacer1 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.authWidgetGridLayout.addItem(self.horizontalSpacer1, 19, 0, 1, 1)

        self.verticalSpacer4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.authWidgetGridLayout.addItem(self.verticalSpacer4, 19, 3, 1, 1)

        self.reg_pushButton = QPushButton(self.gridLayoutWidget)
        self.reg_pushButton.setObjectName(u"reg_pushButton")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.reg_pushButton.setFont(font1)

        self.authWidgetGridLayout.addWidget(self.reg_pushButton, 14, 4, 1, 1)

        self.password_label = QLabel(self.gridLayoutWidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMinimumSize(QSize(0, 0))
        self.password_label.setMaximumSize(QSize(16777215, 20))
        self.password_label.setFont(font1)
        self.password_label.setAlignment(Qt.AlignCenter)

        self.authWidgetGridLayout.addWidget(self.password_label, 9, 3, 1, 1, Qt.AlignHCenter)

        self.login_pushButton = QPushButton(self.gridLayoutWidget)
        self.login_pushButton.setObjectName(u"login_pushButton")
        self.login_pushButton.setMinimumSize(QSize(0, 0))
        self.login_pushButton.setFont(font1)

        self.authWidgetGridLayout.addWidget(self.login_pushButton, 14, 2, 1, 1)

        self.verticalSpacer2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.authWidgetGridLayout.addItem(self.verticalSpacer2, 7, 3, 1, 1)

        self.verticalSpacer3 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.authWidgetGridLayout.addItem(self.verticalSpacer3, 12, 3, 1, 1)

        self.login_lineEdit = QLineEdit(self.gridLayoutWidget)
        self.login_lineEdit.setObjectName(u"login_lineEdit")

        self.authWidgetGridLayout.addWidget(self.login_lineEdit, 6, 3, 1, 1)

        self.login_label = QLabel(self.gridLayoutWidget)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setMinimumSize(QSize(0, 0))
        self.login_label.setMaximumSize(QSize(16777215, 20))
        self.login_label.setFont(font1)
        self.login_label.setAlignment(Qt.AlignCenter)

        self.authWidgetGridLayout.addWidget(self.login_label, 4, 3, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer3 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.authWidgetGridLayout.addItem(self.horizontalSpacer3, 19, 5, 1, 1)


        self.retranslateUi(authWidget)

        QMetaObject.connectSlotsByName(authWidget)
    # setupUi

    def retranslateUi(self, authWidget):
        authWidget.setWindowTitle(QCoreApplication.translate("authWidget", u"\u041e\u043a\u043d\u043e \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.puzzleTitle_label.setText(QCoreApplication.translate("authWidget", u"Puzzle", None))
        self.reg_pushButton.setText(QCoreApplication.translate("authWidget", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.password_label.setText(QCoreApplication.translate("authWidget", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.login_pushButton.setText(QCoreApplication.translate("authWidget", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.login_label.setText(QCoreApplication.translate("authWidget", u"\u041b\u043e\u0433\u0438\u043d", None))
    # retranslateUi

