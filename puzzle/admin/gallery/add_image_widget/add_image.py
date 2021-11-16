# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_image.ui'
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
        Form.resize(398, 222)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 381, 201))
        self.add_image_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.add_image_gridLayout.setObjectName(u"add_image_gridLayout")
        self.add_image_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.path_lineEdit = QLineEdit(self.gridLayoutWidget)
        self.path_lineEdit.setObjectName(u"path_lineEdit")

        self.add_image_gridLayout.addWidget(self.path_lineEdit, 2, 0, 1, 1)

        self.name_image_lineEdit = QLineEdit(self.gridLayoutWidget)
        self.name_image_lineEdit.setObjectName(u"name_image_lineEdit")

        self.add_image_gridLayout.addWidget(self.name_image_lineEdit, 4, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.add_image_gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.add_image_gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.save_pushButton = QPushButton(self.gridLayoutWidget)
        self.save_pushButton.setObjectName(u"save_pushButton")

        self.add_image_gridLayout.addWidget(self.save_pushButton, 4, 1, 1, 1)

        self.choose_pushButton = QPushButton(self.gridLayoutWidget)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.add_image_gridLayout.addWidget(self.choose_pushButton, 2, 1, 1, 1)

        self.path_label = QLabel(self.gridLayoutWidget)
        self.path_label.setObjectName(u"path_label")

        self.add_image_gridLayout.addWidget(self.path_label, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.add_image_gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.save_pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.choose_pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.path_label.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u0434\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
    # retranslateUi

