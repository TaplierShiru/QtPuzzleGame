# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_AdminMenu(object):
    def setupUi(self, AdminMenu):
        if not AdminMenu.objectName():
            AdminMenu.setObjectName(u"AdminMenu")
        AdminMenu.resize(409, 400)
        self.verticalLayoutWidget = QWidget(AdminMenu)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 391, 381))
        self.menu_vlayout = QVBoxLayout(self.verticalLayoutWidget)
        self.menu_vlayout.setObjectName(u"menu_vlayout")
        self.menu_vlayout.setContentsMargins(0, 0, 0, 0)
        self.gallery_pushButton = QPushButton(self.verticalLayoutWidget)
        self.gallery_pushButton.setObjectName(u"gallery_pushButton")
        self.gallery_pushButton.setMaximumSize(QSize(200, 16777215))

        self.menu_vlayout.addWidget(self.gallery_pushButton)

        self.level_control_pushButton = QPushButton(self.verticalLayoutWidget)
        self.level_control_pushButton.setObjectName(u"level_control_pushButton")
        self.level_control_pushButton.setMaximumSize(QSize(200, 16777215))

        self.menu_vlayout.addWidget(self.level_control_pushButton)

        self.create_game_pushButton = QPushButton(self.verticalLayoutWidget)
        self.create_game_pushButton.setObjectName(u"create_game_pushButton")
        self.create_game_pushButton.setMaximumSize(QSize(200, 16777215))

        self.menu_vlayout.addWidget(self.create_game_pushButton)

        self.about_system_pushButton = QPushButton(self.verticalLayoutWidget)
        self.about_system_pushButton.setObjectName(u"about_system_pushButton")
        self.about_system_pushButton.setMaximumSize(QSize(200, 16777215))

        self.menu_vlayout.addWidget(self.about_system_pushButton)

        self.about_creators_pushButton = QPushButton(self.verticalLayoutWidget)
        self.about_creators_pushButton.setObjectName(u"about_creators_pushButton")
        self.about_creators_pushButton.setMaximumSize(QSize(200, 16777215))

        self.menu_vlayout.addWidget(self.about_creators_pushButton)

        self.exit_pushButton = QPushButton(self.verticalLayoutWidget)
        self.exit_pushButton.setObjectName(u"exit_pushButton")
        self.exit_pushButton.setMaximumSize(QSize(200, 16777215))

        self.menu_vlayout.addWidget(self.exit_pushButton)


        self.retranslateUi(AdminMenu)

        QMetaObject.connectSlotsByName(AdminMenu)
    # setupUi

    def retranslateUi(self, AdminMenu):
        AdminMenu.setWindowTitle(QCoreApplication.translate("AdminMenu", u"\u041c\u0435\u043d\u044e \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.gallery_pushButton.setText(QCoreApplication.translate("AdminMenu", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0433\u0430\u043b\u0435\u0440\u0435\u0435\u0439", None))
        self.level_control_pushButton.setText(QCoreApplication.translate("AdminMenu", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0443\u0440\u043e\u0432\u043d\u044f\u043c\u0438", None))
        self.create_game_pushButton.setText(QCoreApplication.translate("AdminMenu", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0438\u0433\u0440\u044b", None))
        self.about_system_pushButton.setText(QCoreApplication.translate("AdminMenu", u"\u041e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.about_creators_pushButton.setText(QCoreApplication.translate("AdminMenu", u"\u041e \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u0445", None))
        self.exit_pushButton.setText(QCoreApplication.translate("AdminMenu", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

