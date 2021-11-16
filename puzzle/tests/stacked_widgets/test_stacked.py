# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_stacked.ui'
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
        Form.resize(441, 419)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 421, 401))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.menu_page = QWidget()
        self.menu_page.setObjectName(u"menu_page")
        self.verticalLayoutWidget = QWidget(self.menu_page)
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

        self.stackedWidget.addWidget(self.menu_page)
        self.gallery_page = QWidget()
        self.gallery_page.setObjectName(u"gallery_page")
        self.gridLayoutWidget_2 = QWidget(self.gallery_page)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 411, 391))
        self.gallery_gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.gallery_gridLayout.setObjectName(u"gallery_gridLayout")
        self.gallery_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.add_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setMinimumSize(QSize(0, 0))
        self.add_pushButton.setMaximumSize(QSize(100, 24))

        self.gallery_gridLayout.addWidget(self.add_pushButton, 2, 1, 1, 1)

        self.delete_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.delete_pushButton.setObjectName(u"delete_pushButton")
        self.delete_pushButton.setMaximumSize(QSize(100, 24))

        self.gallery_gridLayout.addWidget(self.delete_pushButton, 2, 2, 1, 1)

        self.back_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.back_pushButton.setObjectName(u"back_pushButton")
        self.back_pushButton.setMaximumSize(QSize(100, 24))

        self.gallery_gridLayout.addWidget(self.back_pushButton, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(self.gridLayoutWidget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 358, 357))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 321, 351))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gallery_gridLayout.addWidget(self.scrollArea, 1, 0, 1, 3)

        self.stackedWidget.addWidget(self.gallery_page)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gallery_pushButton.setText(QCoreApplication.translate("Form", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0433\u0430\u043b\u0435\u0440\u0435\u0435\u0439", None))
        self.level_control_pushButton.setText(QCoreApplication.translate("Form", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0443\u0440\u043e\u0432\u043d\u044f\u043c\u0438", None))
        self.create_game_pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0438\u0433\u0440\u044b", None))
        self.about_system_pushButton.setText(QCoreApplication.translate("Form", u"\u041e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.about_creators_pushButton.setText(QCoreApplication.translate("Form", u"\u041e \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u0445", None))
        self.exit_pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.add_pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.back_pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

