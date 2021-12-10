# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_UserMenu(object):
    def setupUi(self, UserMenu):
        if not UserMenu.objectName():
            UserMenu.setObjectName(u"UserMenu")
        UserMenu.resize(400, 300)
        self.verticalLayoutWidget = QWidget(UserMenu)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 381, 281))
        self.user_menu_verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.user_menu_verticalLayout.setObjectName(u"user_menu_verticalLayout")
        self.user_menu_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.new_game_pushButton = QPushButton(self.verticalLayoutWidget)
        self.new_game_pushButton.setObjectName(u"new_game_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_game_pushButton.sizePolicy().hasHeightForWidth())
        self.new_game_pushButton.setSizePolicy(sizePolicy)
        self.new_game_pushButton.setMaximumSize(QSize(200, 16777215))
        self.new_game_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.new_game_pushButton.setAutoFillBackground(False)
        self.new_game_pushButton.setAutoDefault(False)

        self.user_menu_verticalLayout.addWidget(self.new_game_pushButton)

        self.load_game_pushButton = QPushButton(self.verticalLayoutWidget)
        self.load_game_pushButton.setObjectName(u"load_game_pushButton")
        sizePolicy.setHeightForWidth(self.load_game_pushButton.sizePolicy().hasHeightForWidth())
        self.load_game_pushButton.setSizePolicy(sizePolicy)
        self.load_game_pushButton.setMaximumSize(QSize(200, 16777215))
        self.load_game_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.load_game_pushButton.setAutoFillBackground(False)
        self.load_game_pushButton.setAutoDefault(False)

        self.user_menu_verticalLayout.addWidget(self.load_game_pushButton)

        self.leader_board_pushButton = QPushButton(self.verticalLayoutWidget)
        self.leader_board_pushButton.setObjectName(u"leader_board_pushButton")
        sizePolicy.setHeightForWidth(self.leader_board_pushButton.sizePolicy().hasHeightForWidth())
        self.leader_board_pushButton.setSizePolicy(sizePolicy)
        self.leader_board_pushButton.setMaximumSize(QSize(200, 16777215))
        self.leader_board_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.leader_board_pushButton.setAutoFillBackground(False)
        self.leader_board_pushButton.setAutoDefault(False)

        self.user_menu_verticalLayout.addWidget(self.leader_board_pushButton)

        self.about_system_pushButton = QPushButton(self.verticalLayoutWidget)
        self.about_system_pushButton.setObjectName(u"about_system_pushButton")
        sizePolicy.setHeightForWidth(self.about_system_pushButton.sizePolicy().hasHeightForWidth())
        self.about_system_pushButton.setSizePolicy(sizePolicy)
        self.about_system_pushButton.setMaximumSize(QSize(200, 16777215))
        self.about_system_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.about_system_pushButton.setAutoFillBackground(False)
        self.about_system_pushButton.setAutoDefault(False)

        self.user_menu_verticalLayout.addWidget(self.about_system_pushButton)

        self.about_creators_pushButton = QPushButton(self.verticalLayoutWidget)
        self.about_creators_pushButton.setObjectName(u"about_creators_pushButton")
        sizePolicy.setHeightForWidth(self.about_creators_pushButton.sizePolicy().hasHeightForWidth())
        self.about_creators_pushButton.setSizePolicy(sizePolicy)
        self.about_creators_pushButton.setMaximumSize(QSize(200, 16777215))
        self.about_creators_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.about_creators_pushButton.setAutoFillBackground(False)
        self.about_creators_pushButton.setAutoDefault(False)

        self.user_menu_verticalLayout.addWidget(self.about_creators_pushButton)

        self.exit_pushButton = QPushButton(self.verticalLayoutWidget)
        self.exit_pushButton.setObjectName(u"exit_pushButton")
        sizePolicy.setHeightForWidth(self.exit_pushButton.sizePolicy().hasHeightForWidth())
        self.exit_pushButton.setSizePolicy(sizePolicy)
        self.exit_pushButton.setMaximumSize(QSize(200, 16777215))
        self.exit_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.exit_pushButton.setAutoFillBackground(False)
        self.exit_pushButton.setAutoDefault(False)

        self.user_menu_verticalLayout.addWidget(self.exit_pushButton)


        self.retranslateUi(UserMenu)

        self.new_game_pushButton.setDefault(False)
        self.load_game_pushButton.setDefault(False)
        self.leader_board_pushButton.setDefault(False)
        self.about_system_pushButton.setDefault(False)
        self.about_creators_pushButton.setDefault(False)
        self.exit_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(UserMenu)
    # setupUi

    def retranslateUi(self, UserMenu):
        UserMenu.setWindowTitle(QCoreApplication.translate("UserMenu", u"\u041c\u0435\u043d\u044e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.new_game_pushButton.setText(QCoreApplication.translate("UserMenu", u"\u041d\u043e\u0432\u0430\u044f \u0438\u0433\u0440\u0430", None))
        self.load_game_pushButton.setText(QCoreApplication.translate("UserMenu", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.leader_board_pushButton.setText(QCoreApplication.translate("UserMenu", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u043b\u0438\u0434\u0435\u0440\u043e\u0432", None))
        self.about_system_pushButton.setText(QCoreApplication.translate("UserMenu", u"\u041e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.about_creators_pushButton.setText(QCoreApplication.translate("UserMenu", u"\u041e \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u0445", None))
        self.exit_pushButton.setText(QCoreApplication.translate("UserMenu", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

