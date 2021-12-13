# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_creators.ui'
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
        Form.resize(448, 299)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 431, 281))
        self.about_creators_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.about_creators_gridLayout.setObjectName(u"about_creators_gridLayout")
        self.about_creators_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(100, 24))
        self.label.setAlignment(Qt.AlignCenter)

        self.about_creators_gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.about_creators_label = QLabel(self.gridLayoutWidget)
        self.about_creators_label.setObjectName(u"about_creators_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.about_creators_label.sizePolicy().hasHeightForWidth())
        self.about_creators_label.setSizePolicy(sizePolicy1)
        self.about_creators_label.setAlignment(Qt.AlignCenter)
        self.about_creators_label.setWordWrap(True)

        self.about_creators_gridLayout.addWidget(self.about_creators_label, 1, 0, 1, 4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.about_creators_gridLayout.addItem(self.horizontalSpacer_3, 3, 1, 1, 1)

        self.back_pushButton = QPushButton(self.gridLayoutWidget)
        self.back_pushButton.setObjectName(u"back_pushButton")

        self.about_creators_gridLayout.addWidget(self.back_pushButton, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.about_creators_gridLayout.addItem(self.horizontalSpacer, 3, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.about_creators_gridLayout.addWidget(self.label_2, 2, 0, 1, 3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041e \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u0445", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u0445", None))
        self.about_creators_label.setText(QCoreApplication.translate("Form", u"\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0439 \u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0443\u043c \u043f\u043e \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u0435: \"\u0422\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f\"\n"
"\u0422\u0435\u043c\u0430: \"\u0418\u0433\u0440\u0430 \"Puzzle\" \u0441 \u0444\u0443\u043d\u043a\u0446\u0438\u044f\u043c\u0438 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430\"\n"
"\n"
"\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0438 c\u0442\u0443\u0434\u0435\u043d\u0442\u044b \u0433\u0440\u0443\u043f\u043f\u044b 6401-090301D:\n"
"\u0413\u0440\u0438\u0431\u0430\u043d\u043e\u0432 \u0414\u0430\u043d\u0438\u043b\n"
"\u0413\u0443\u0441\u0435\u0432 \u0413\u0440\u0438\u0433\u043e\u0440\u0438\u0439\n"
"\n"
"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c:\n"
"\u0417\u0435"
                        "\u043b\u0435\u043d\u043a\u043e \u041b\u0430\u0440\u0438\u0441\u0430 \u0421\u0435\u0440\u0433\u0435\u0435\u0432\u043d\u0430", None))
        self.back_pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0421\u0430\u043c\u0430\u0440\u0441\u043a\u0438\u0439 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442 2021", None))
    # retranslateUi

