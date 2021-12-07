# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choose_image.ui'
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
        Form.resize(435, 413)
        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 411, 391))
        self.choose_image_gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.choose_image_gridLayout.setObjectName(u"choose_image_gridLayout")
        self.choose_image_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.choose_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.choose_pushButton.setObjectName(u"choose_pushButton")
        self.choose_pushButton.setMinimumSize(QSize(0, 0))
        self.choose_pushButton.setMaximumSize(QSize(100, 24))

        self.choose_image_gridLayout.addWidget(self.choose_pushButton, 2, 1, 1, 1)

        self.scrollArea = QScrollArea(self.gridLayoutWidget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 407, 357))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 391, 341))
        self.image_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.image_gridLayout.setObjectName(u"image_gridLayout")
        self.image_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.choose_image_gridLayout.addWidget(self.scrollArea, 1, 0, 1, 3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u043e\u0440 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.choose_pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

