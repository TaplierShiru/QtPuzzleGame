# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gallery.ui'
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
        Form.resize(436, 413)
        self.gridLayoutWidget_2 = QWidget(Form)
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

        self.scrollArea = QScrollArea(self.gridLayoutWidget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 358, 357))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 321, 351))
        self.image_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.image_gridLayout.setObjectName(u"image_gridLayout")
        self.image_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gallery_gridLayout.addWidget(self.scrollArea, 1, 0, 1, 3)

        self.delete_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.delete_pushButton.setObjectName(u"delete_pushButton")
        self.delete_pushButton.setMaximumSize(QSize(100, 24))

        self.gallery_gridLayout.addWidget(self.delete_pushButton, 2, 2, 1, 1)

        self.back_pushButton = QPushButton(self.gridLayoutWidget_2)
        self.back_pushButton.setObjectName(u"back_pushButton")
        self.back_pushButton.setMaximumSize(QSize(100, 24))

        self.gallery_gridLayout.addWidget(self.back_pushButton, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0413\u0430\u043b\u0435\u0440\u0435\u044f", None))
        self.add_pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_pushButton.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.back_pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

