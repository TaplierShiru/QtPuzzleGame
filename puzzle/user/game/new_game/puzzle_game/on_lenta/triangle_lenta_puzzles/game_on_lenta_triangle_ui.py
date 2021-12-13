# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_with_lenta.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_GameTriangleOnLenta(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 588)
        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 600, 571))
        self.game_gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.game_gridLayout.setObjectName(u"game_gridLayout")
        self.game_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.about_system_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.about_system_pushButton.setObjectName(u"about_system_pushButton")

        self.game_gridLayout.addWidget(self.about_system_pushButton, 0, 2, 1, 1)

        self.score_value_label = QLabel(self.gridLayoutWidget_2)
        self.score_value_label.setObjectName(u"score_value_label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.score_value_label.sizePolicy().hasHeightForWidth())
        self.score_value_label.setSizePolicy(sizePolicy)
        self.score_value_label.setMinimumSize(QSize(100, 20))

        self.game_gridLayout.addWidget(self.score_value_label, 1, 3, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.game_gridLayout.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.save_game_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.save_game_pushButton.setObjectName(u"save_game_pushButton")

        self.game_gridLayout.addWidget(self.save_game_pushButton, 0, 0, 1, 1)

        self.exit_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.exit_pushButton.setObjectName(u"exit_pushButton")

        self.game_gridLayout.addWidget(self.exit_pushButton, 0, 3, 1, 2)

        self.score_label = QLabel(self.gridLayoutWidget_2)
        self.score_label.setObjectName(u"score_label")
        sizePolicy.setHeightForWidth(self.score_label.sizePolicy().hasHeightForWidth())
        self.score_label.setSizePolicy(sizePolicy)
        self.score_label.setMinimumSize(QSize(100, 20))

        self.game_gridLayout.addWidget(self.score_label, 1, 2, 1, 1)

        """
        self.game_widget = QWidget(self.gridLayoutWidget_2)
        self.game_widget.setObjectName(u"game_widget")
        self.game_widget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.game_widget.sizePolicy().hasHeightForWidth())
        self.game_widget.setSizePolicy(sizePolicy1)

        self.game_gridLayout.addWidget(self.game_widget, 2, 0, 1, 6)
        """

        self.look_full_image_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.look_full_image_pushButton.setObjectName(u"look_full_image_pushButton")

        self.game_gridLayout.addWidget(self.look_full_image_pushButton, 0, 1, 1, 1)

        """
        self.lenta_widget = QWidget(self.gridLayoutWidget_2)
        self.lenta_widget.setObjectName(u"lenta_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lenta_widget.sizePolicy().hasHeightForWidth())
        self.lenta_widget.setSizePolicy(sizePolicy2)
        self.lenta_widget.setMinimumSize(QSize(0, 100))

        self.game_gridLayout.addWidget(self.lenta_widget, 3, 0, 1, 6)
        """

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041f\u0430\u0437\u043b", None))
        self.about_system_pushButton.setText(QCoreApplication.translate("Form", u"\u041e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.score_value_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.save_game_pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.exit_pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.score_label.setText(QCoreApplication.translate("Form", u"Score:", None))
        self.look_full_image_pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0435\u0434\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
    # retranslateUi

