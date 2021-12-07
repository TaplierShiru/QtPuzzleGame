# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'score_table.ui'
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
        Form.resize(400, 300)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 381, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.count_to_label = QLabel(self.gridLayoutWidget)
        self.count_to_label.setObjectName(u"count_to_label")

        self.gridLayout.addWidget(self.count_to_label, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.type_score_comboBox = QComboBox(self.gridLayoutWidget)
        self.type_score_comboBox.setObjectName(u"type_score_comboBox")

        self.gridLayout.addWidget(self.type_score_comboBox, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.back_to_menu_pushButton = QPushButton(self.gridLayoutWidget)
        self.back_to_menu_pushButton.setObjectName(u"back_to_menu_pushButton")

        self.gridLayout.addWidget(self.back_to_menu_pushButton, 2, 0, 1, 1)

        self.top10_tableWidget = QTableWidget(self.gridLayoutWidget)
        self.top10_tableWidget.setObjectName(u"top10_tableWidget")

        self.gridLayout.addWidget(self.top10_tableWidget, 1, 0, 1, 4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u043b\u0438\u0434\u0435\u0440\u043e\u0432", None))
        self.count_to_label.setText(QCoreApplication.translate("Form", u"\u0423\u0447\u0438\u0442\u044b\u0432\u0430\u0442\u044c \u0440\u0435\u0439\u0442\u0438\u043d\u0433 \u043f\u043e:", None))
        self.back_to_menu_pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

