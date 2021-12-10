# -*- coding: utf-8 -*-

################################################################################
## GameBase generated from reading UI file 'game_on_field.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_GameBase(object):
    def setupUi(self, GameBase):
        if not GameBase.objectName():
            GameBase.setObjectName(u"GameBase")
        GameBase.resize(633, 482)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GameBase.sizePolicy().hasHeightForWidth())
        GameBase.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QWidget(GameBase)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 611, 461))
        self.game_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.game_gridLayout.setObjectName(u"game_gridLayout")
        self.game_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.game_gridLayout.addItem(self.horizontalSpacer, 0, 5, 1, 1)

        self.save_game_pushButton = QPushButton(self.gridLayoutWidget)
        self.save_game_pushButton.setObjectName(u"save_game_pushButton")

        self.game_gridLayout.addWidget(self.save_game_pushButton, 0, 0, 1, 1)

        self.score_label = QLabel(self.gridLayoutWidget)
        self.score_label.setObjectName(u"score_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.score_label.sizePolicy().hasHeightForWidth())
        self.score_label.setSizePolicy(sizePolicy1)
        self.score_label.setMinimumSize(QSize(100, 20))

        self.game_gridLayout.addWidget(self.score_label, 1, 2, 1, 1)

        self.look_full_image_pushButton = QPushButton(self.gridLayoutWidget)
        self.look_full_image_pushButton.setObjectName(u"look_full_image_pushButton")

        self.game_gridLayout.addWidget(self.look_full_image_pushButton, 0, 1, 1, 1)

        self.about_system_pushButton = QPushButton(self.gridLayoutWidget)
        self.about_system_pushButton.setObjectName(u"about_system_pushButton")

        self.game_gridLayout.addWidget(self.about_system_pushButton, 0, 2, 1, 1)

        self.exit_pushButton = QPushButton(self.gridLayoutWidget)
        self.exit_pushButton.setObjectName(u"exit_pushButton")

        self.game_gridLayout.addWidget(self.exit_pushButton, 0, 3, 1, 2)

        self.score_value_label = QLabel(self.gridLayoutWidget)
        self.score_value_label.setObjectName(u"score_value_label")
        sizePolicy1.setHeightForWidth(self.score_value_label.sizePolicy().hasHeightForWidth())
        self.score_value_label.setSizePolicy(sizePolicy1)
        self.score_value_label.setMinimumSize(QSize(100, 20))

        self.game_gridLayout.addWidget(self.score_value_label, 1, 3, 1, 2)

        self.game_widget = QWidget(self.gridLayoutWidget)
        self.game_widget.setObjectName(u"game_widget")
        self.game_widget.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.game_widget.sizePolicy().hasHeightForWidth())
        self.game_widget.setSizePolicy(sizePolicy2)

        self.game_gridLayout.addWidget(self.game_widget, 2, 0, 1, 6)


        self.retranslateUi(GameBase)

        QMetaObject.connectSlotsByName(GameBase)
    # setupUi

    def retranslateUi(self, GameBase):
        GameBase.setWindowTitle(QCoreApplication.translate("GameBase", u"\u041f\u0430\u0437\u043b", None))
        self.save_game_pushButton.setText(QCoreApplication.translate("GameBase", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.score_label.setText(QCoreApplication.translate("GameBase", u"Score:", None))
        self.look_full_image_pushButton.setText(QCoreApplication.translate("GameBase", u"\u041f\u0440\u0435\u0434\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.about_system_pushButton.setText(QCoreApplication.translate("GameBase", u"\u041e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.exit_pushButton.setText(QCoreApplication.translate("GameBase", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.score_value_label.setText(QCoreApplication.translate("GameBase", u"0", None))
    # retranslateUi

