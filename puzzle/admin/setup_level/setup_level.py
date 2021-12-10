# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup_level.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SetupLevel(object):
    def setupUi(self, SetupLevel):
        if not SetupLevel.objectName():
            SetupLevel.setObjectName(u"SetupLevel")
        SetupLevel.resize(376, 353)
        self.gridLayoutWidget = QWidget(SetupLevel)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 351, 331))
        self.setup_level_gridLayout = QGridLayout(self.gridLayoutWidget)
        self.setup_level_gridLayout.setObjectName(u"setup_level_gridLayout")
        self.setup_level_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.setup_level_gridLayout.addItem(self.horizontalSpacer, 5, 1, 1, 1)

        self.save_pushButton = QPushButton(self.gridLayoutWidget)
        self.save_pushButton.setObjectName(u"save_pushButton")

        self.setup_level_gridLayout.addWidget(self.save_pushButton, 5, 3, 1, 1)

        self.back_pushButton = QPushButton(self.gridLayoutWidget)
        self.back_pushButton.setObjectName(u"back_pushButton")

        self.setup_level_gridLayout.addWidget(self.back_pushButton, 5, 0, 1, 1)

        self.type_build_label = QLabel(self.gridLayoutWidget)
        self.type_build_label.setObjectName(u"type_build_label")

        self.setup_level_gridLayout.addWidget(self.type_build_label, 4, 0, 1, 1)

        self.type_puzle_label = QLabel(self.gridLayoutWidget)
        self.type_puzle_label.setObjectName(u"type_puzle_label")

        self.setup_level_gridLayout.addWidget(self.type_puzle_label, 3, 0, 1, 1)

        self.diffic_label = QLabel(self.gridLayoutWidget)
        self.diffic_label.setObjectName(u"diffic_label")

        self.setup_level_gridLayout.addWidget(self.diffic_label, 0, 0, 1, 1)

        self.num_frag_h_label = QLabel(self.gridLayoutWidget)
        self.num_frag_h_label.setObjectName(u"num_frag_h_label")
        self.num_frag_h_label.setWordWrap(True)

        self.setup_level_gridLayout.addWidget(self.num_frag_h_label, 2, 0, 1, 1)

        self.num_frag_v_label = QLabel(self.gridLayoutWidget)
        self.num_frag_v_label.setObjectName(u"num_frag_v_label")
        self.num_frag_v_label.setMaximumSize(QSize(100, 16777215))
        self.num_frag_v_label.setWordWrap(True)

        self.setup_level_gridLayout.addWidget(self.num_frag_v_label, 1, 0, 1, 1)

        self.type_puzle_comboBox = QComboBox(self.gridLayoutWidget)
        self.type_puzle_comboBox.setObjectName(u"type_puzle_comboBox")

        self.setup_level_gridLayout.addWidget(self.type_puzle_comboBox, 3, 2, 1, 2)

        self.num_frag_h_comboBox = QComboBox(self.gridLayoutWidget)
        self.num_frag_h_comboBox.setObjectName(u"num_frag_h_comboBox")

        self.setup_level_gridLayout.addWidget(self.num_frag_h_comboBox, 2, 2, 1, 2)

        self.num_frag_v_comboBox = QComboBox(self.gridLayoutWidget)
        self.num_frag_v_comboBox.setObjectName(u"num_frag_v_comboBox")

        self.setup_level_gridLayout.addWidget(self.num_frag_v_comboBox, 1, 2, 1, 2)

        self.diffic_comboBox = QComboBox(self.gridLayoutWidget)
        self.diffic_comboBox.setObjectName(u"diffic_comboBox")

        self.setup_level_gridLayout.addWidget(self.diffic_comboBox, 0, 2, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.setup_level_gridLayout.addItem(self.horizontalSpacer_2, 5, 2, 1, 1)

        self.type_build_comboBox = QComboBox(self.gridLayoutWidget)
        self.type_build_comboBox.setObjectName(u"type_build_comboBox")

        self.setup_level_gridLayout.addWidget(self.type_build_comboBox, 4, 2, 1, 2)


        self.retranslateUi(SetupLevel)

        QMetaObject.connectSlotsByName(SetupLevel)
    # setupUi

    def retranslateUi(self, SetupLevel):
        SetupLevel.setWindowTitle(QCoreApplication.translate("SetupLevel", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0443\u0440\u043e\u0432\u043d\u044f", None))
        self.save_pushButton.setText(QCoreApplication.translate("SetupLevel", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.back_pushButton.setText(QCoreApplication.translate("SetupLevel", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.type_build_label.setText(QCoreApplication.translate("SetupLevel", u"\u0412\u0438\u0434 \u0441\u0431\u043e\u0440\u043a\u0438", None))
        self.type_puzle_label.setText(QCoreApplication.translate("SetupLevel", u"\u0412\u0438\u0434 \u043f\u0430\u0437\u043b\u0430", None))
        self.diffic_label.setText(QCoreApplication.translate("SetupLevel", u"\u0421\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.num_frag_h_label.setText(QCoreApplication.translate("SetupLevel", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0444\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u043e\u0432 \u043f\u043e \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u0438", None))
        self.num_frag_v_label.setText(QCoreApplication.translate("SetupLevel", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0444\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u043e\u0432 \u043f\u043e \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u0438", None))
    # retranslateUi

