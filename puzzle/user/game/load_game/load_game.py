# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_game.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(602, 317)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 581, 301))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 2, 1, 1)

        self.saved_games_tableView = QTableView(self.gridLayoutWidget)
        self.saved_games_tableView.setObjectName(u"saved_games_tableView")

        self.gridLayout.addWidget(self.saved_games_tableView, 2, 0, 1, 7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 6, 1, 1)

        self.delete_game_pushButton = QPushButton(self.gridLayoutWidget)
        self.delete_game_pushButton.setObjectName(u"delete_game_pushButton")

        self.gridLayout.addWidget(self.delete_game_pushButton, 3, 4, 1, 1)

        self.load_game_pushButton = QPushButton(self.gridLayoutWidget)
        self.load_game_pushButton.setObjectName(u"load_game_pushButton")

        self.gridLayout.addWidget(self.load_game_pushButton, 3, 6, 1, 1)

        self.back_to_menu_pushButton = QPushButton(self.gridLayoutWidget)
        self.back_to_menu_pushButton.setObjectName(u"back_to_menu_pushButton")

        self.gridLayout.addWidget(self.back_to_menu_pushButton, 3, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 1, 1, 1)

        self.saved_games_label = QLabel(self.gridLayoutWidget)
        self.saved_games_label.setObjectName(u"saved_games_label")
        self.saved_games_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.saved_games_label, 0, 2, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0438\u0433\u0440\u044b", None))
        self.delete_game_pushButton.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.load_game_pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.back_to_menu_pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.saved_games_label.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u0435 \u0438\u0433\u0440\u044b", None))
    # retranslateUi

