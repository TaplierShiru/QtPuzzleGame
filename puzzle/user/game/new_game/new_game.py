# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_game.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_NewGame(object):
    def setupUi(self, NewGame):
        if not NewGame.objectName():
            NewGame.setObjectName(u"NewGame")
        NewGame.resize(490, 370)
        self.gridLayoutWidget = QWidget(NewGame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 471, 351))
        self.new_game_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.new_game_gridLayout.setObjectName(u"new_game_gridLayout")
        self.new_game_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.type_res_comboBox = QComboBox(self.gridLayoutWidget)
        self.type_res_comboBox.setObjectName(u"type_res_comboBox")
        self.type_res_comboBox.setMinimumSize(QSize(150, 0))

        self.new_game_gridLayout.addWidget(self.type_res_comboBox, 3, 5, 1, 2)

        self.choose_image_pushButton = QPushButton(self.gridLayoutWidget)
        self.choose_image_pushButton.setObjectName(u"choose_image_pushButton")

        self.new_game_gridLayout.addWidget(self.choose_image_pushButton, 11, 4, 1, 1)

        self.back_to_menu_pushButton = QPushButton(self.gridLayoutWidget)
        self.back_to_menu_pushButton.setObjectName(u"back_to_menu_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_to_menu_pushButton.sizePolicy().hasHeightForWidth())
        self.back_to_menu_pushButton.setSizePolicy(sizePolicy)
        self.back_to_menu_pushButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.back_to_menu_pushButton.setLayoutDirection(Qt.LeftToRight)

        self.new_game_gridLayout.addWidget(self.back_to_menu_pushButton, 11, 0, 1, 1)

        self.level_diff_comboBox = QComboBox(self.gridLayoutWidget)
        self.level_diff_comboBox.setObjectName(u"level_diff_comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.level_diff_comboBox.sizePolicy().hasHeightForWidth())
        self.level_diff_comboBox.setSizePolicy(sizePolicy1)
        self.level_diff_comboBox.setMinimumSize(QSize(150, 0))
        self.level_diff_comboBox.setMaximumSize(QSize(160000, 16777215))

        self.new_game_gridLayout.addWidget(self.level_diff_comboBox, 1, 5, 1, 2)

        self.type_res_label = QLabel(self.gridLayoutWidget)
        self.type_res_label.setObjectName(u"type_res_label")

        self.new_game_gridLayout.addWidget(self.type_res_label, 3, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(142, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.new_game_gridLayout.addItem(self.horizontalSpacer, 3, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.new_game_gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 4)

        self.level_diff_label = QLabel(self.gridLayoutWidget)
        self.level_diff_label.setObjectName(u"level_diff_label")

        self.new_game_gridLayout.addWidget(self.level_diff_label, 1, 0, 1, 4)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.new_game_gridLayout.addItem(self.verticalSpacer_3, 10, 0, 1, 1)

        self.start_game_pushButton = QPushButton(self.gridLayoutWidget)
        self.start_game_pushButton.setObjectName(u"start_game_pushButton")
        sizePolicy.setHeightForWidth(self.start_game_pushButton.sizePolicy().hasHeightForWidth())
        self.start_game_pushButton.setSizePolicy(sizePolicy)
        self.start_game_pushButton.setLayoutDirection(Qt.LeftToRight)

        self.new_game_gridLayout.addWidget(self.start_game_pushButton, 11, 6, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.new_game_gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 4)

        self.choose_image_label = QLabel(self.gridLayoutWidget)
        self.choose_image_label.setObjectName(u"choose_image_label")

        self.new_game_gridLayout.addWidget(self.choose_image_label, 8, 0, 1, 4)

        self.choosen_image_lineEdit = QLineEdit(self.gridLayoutWidget)
        self.choosen_image_lineEdit.setObjectName(u"choosen_image_lineEdit")

        self.new_game_gridLayout.addWidget(self.choosen_image_lineEdit, 8, 5, 1, 2)

        self.new_game_label = QLabel(self.gridLayoutWidget)
        self.new_game_label.setObjectName(u"new_game_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.new_game_label.sizePolicy().hasHeightForWidth())
        self.new_game_label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.new_game_label.setFont(font)
        self.new_game_label.setAlignment(Qt.AlignCenter)

        self.new_game_gridLayout.addWidget(self.new_game_label, 0, 0, 1, 7)


        self.retranslateUi(NewGame)

        QMetaObject.connectSlotsByName(NewGame)
    # setupUi

    def retranslateUi(self, NewGame):
        NewGame.setWindowTitle(QCoreApplication.translate("NewGame", u"\u041d\u043e\u0432\u0430\u044f \u0438\u0433\u0440\u0430", None))
        self.choose_image_pushButton.setText(QCoreApplication.translate("NewGame", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.back_to_menu_pushButton.setText(QCoreApplication.translate("NewGame", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.type_res_label.setText(QCoreApplication.translate("NewGame", u"\u0421\u043f\u043e\u0441\u043e\u0431 \u043f\u043e\u0434\u0441\u0447\u0435\u0442\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
        self.level_diff_label.setText(QCoreApplication.translate("NewGame", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.start_game_pushButton.setText(QCoreApplication.translate("NewGame", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.choose_image_label.setText(QCoreApplication.translate("NewGame", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435:", None))
        self.new_game_label.setText(QCoreApplication.translate("NewGame", u"\u041d\u0430\u0447\u0430\u043b\u043e \u043d\u043e\u0432\u043e\u0439 \u0438\u0433\u0440\u044b", None))
    # retranslateUi

