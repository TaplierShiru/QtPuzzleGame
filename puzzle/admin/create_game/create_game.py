# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_game.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_CreateGame(object):
    def setupUi(self, CreateGame):
        if not CreateGame.objectName():
            CreateGame.setObjectName(u"CreateGame")
        CreateGame.resize(865, 475)
        self.gridLayoutWidget = QWidget(CreateGame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 844, 451))
        self.create_game_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.create_game_gridLayout.setObjectName(u"create_game_gridLayout")
        self.create_game_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.create_game_gridLayout.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.save_pushButton = QPushButton(self.gridLayoutWidget)
        self.save_pushButton.setObjectName(u"save_pushButton")

        self.create_game_gridLayout.addWidget(self.save_pushButton, 5, 5, 1, 1)

        self.diff_comboBox = QComboBox(self.gridLayoutWidget)
        self.diff_comboBox.setObjectName(u"diff_comboBox")

        self.create_game_gridLayout.addWidget(self.diff_comboBox, 0, 3, 1, 1)

        self.shuffle_pushButton = QPushButton(self.gridLayoutWidget)
        self.shuffle_pushButton.setObjectName(u"shuffle_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shuffle_pushButton.sizePolicy().hasHeightForWidth())
        self.shuffle_pushButton.setSizePolicy(sizePolicy)

        self.create_game_gridLayout.addWidget(self.shuffle_pushButton, 3, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 26, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.create_game_gridLayout.addItem(self.verticalSpacer, 4, 4, 1, 1)

        self.shuffle_image_label = QLabel(self.gridLayoutWidget)
        self.shuffle_image_label.setObjectName(u"shuffle_image_label")

        self.create_game_gridLayout.addWidget(self.shuffle_image_label, 1, 4, 1, 1)

        self.back_pushButton = QPushButton(self.gridLayoutWidget)
        self.back_pushButton.setObjectName(u"back_pushButton")

        self.create_game_gridLayout.addWidget(self.back_pushButton, 5, 0, 1, 1)

        self.source_image_label = QLabel(self.gridLayoutWidget)
        self.source_image_label.setObjectName(u"source_image_label")

        self.create_game_gridLayout.addWidget(self.source_image_label, 1, 1, 1, 1)

        self.choose_image_pushButton = QPushButton(self.gridLayoutWidget)
        self.choose_image_pushButton.setObjectName(u"choose_image_pushButton")

        self.create_game_gridLayout.addWidget(self.choose_image_pushButton, 3, 1, 1, 1)

        self.diff_label = QLabel(self.gridLayoutWidget)
        self.diff_label.setObjectName(u"diff_label")

        self.create_game_gridLayout.addWidget(self.diff_label, 0, 2, 1, 1)

        self.source_image_label_placeholder = QLabel(self.gridLayoutWidget)
        self.source_image_label_placeholder.setObjectName(u"source_image_label_placeholder")

        self.create_game_gridLayout.addWidget(self.source_image_label_placeholder, 2, 1, 1, 1)

        self.shuffle_image_label_placeholder = QLabel(self.gridLayoutWidget)
        self.shuffle_image_label_placeholder.setObjectName(u"shuffle_image_label_placeholder")

        self.create_game_gridLayout.addWidget(self.shuffle_image_label_placeholder, 2, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.create_game_gridLayout.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)


        self.retranslateUi(CreateGame)

        QMetaObject.connectSlotsByName(CreateGame)
    # setupUi

    def retranslateUi(self, CreateGame):
        CreateGame.setWindowTitle(QCoreApplication.translate("CreateGame", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0438\u0433\u0440\u044b", None))
        self.save_pushButton.setText(QCoreApplication.translate("CreateGame", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.shuffle_pushButton.setText(QCoreApplication.translate("CreateGame", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0448\u0430\u0442\u044c", None))
        self.shuffle_image_label.setText(QCoreApplication.translate("CreateGame", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0448\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u0437\u043b\u044b", None))
        self.back_pushButton.setText(QCoreApplication.translate("CreateGame", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.source_image_label.setText(QCoreApplication.translate("CreateGame", u"\u0418\u0441\u0445\u043e\u0434\u043d\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.choose_image_pushButton.setText(QCoreApplication.translate("CreateGame", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.diff_label.setText(QCoreApplication.translate("CreateGame", u"\u0421\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.source_image_label_placeholder.setText("")
        self.shuffle_image_label_placeholder.setText("")
    # retranslateUi

