from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QMessageBox

from .score_table import Ui_Form
from puzzle.database import DatabaseController
from puzzle.common.signals import SignalSenderBackToMenu
from puzzle.common.back_to_menu import BackToMenu
from puzzle.utils import TYPE_SCORE, SCORE_TIME, SCORE_POINTS
from ...common.qmess_boxes import return_qmess_box_connect_db_error


class QScoreTableWidget(QWidget, BackToMenu):

    SIZE_WINDOW_W = 80
    SIZE_WINDOW_H = 200

    def __init__(self, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self._qmess_box: QMessageBox = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_back_to_menu_signal(signal_back_to_menu=signal_back_to_menu)

        self.ui.type_score_comboBox.addItems(TYPE_SCORE)
        # Buttons
        self.ui.back_to_menu_pushButton.clicked.connect(self.emit_signal_back_to_menu)

        self.ui.type_score_comboBox.currentTextChanged.connect(self.update_table)

        # Table widget
        # Headers
        self.ui.top10_tableWidget.setColumnCount(3)
        self.ui.top10_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        qtwi = QTableWidgetItem("Логин", QTableWidgetItem.Type)
        self.ui.top10_tableWidget.setHorizontalHeaderItem(0, qtwi)
        self.ui.top10_tableWidget.setColumnWidth(0, 60)

        qtwi = QTableWidgetItem("Сложность", QTableWidgetItem.Type)
        self.ui.top10_tableWidget.setHorizontalHeaderItem(1, qtwi)
        self.ui.top10_tableWidget.setColumnWidth(2, 60)
        self.setLayout(self.ui.gridLayout)
        self.update()

    def update_table(self):
        self.ui.top10_tableWidget.setRowCount(0)
        current_type = self.ui.type_score_comboBox.currentText()
        if current_type == SCORE_TIME:
            self._header_time = QTableWidgetItem("Время", QTableWidgetItem.Type)
            self.ui.top10_tableWidget.setHorizontalHeaderItem(2, self._header_time)
        elif current_type == SCORE_POINTS:
            self._header_points = QTableWidgetItem("Очки", QTableWidgetItem.Type)
            self.ui.top10_tableWidget.setHorizontalHeaderItem(2, self._header_points)
        else:
            raise TypeError()

        data_to_print = DatabaseController.get_all_records(current_type)

        if data_to_print is None:
            self._qmess_box = return_qmess_box_connect_db_error()
            self._qmess_box.show()
            return

        for row_i, single_data in enumerate(data_to_print):
            self.ui.top10_tableWidget.setRowCount(
                self.ui.top10_tableWidget.rowCount()+1
            )
            self.ui.top10_tableWidget.setRowHeight(
                self.ui.top10_tableWidget.rowCount()-1,
                30
            )
            login_item = QTableWidgetItem(single_data.login)
            login_item.setTextAlignment(Qt.AlignCenter)
            self.ui.top10_tableWidget.setItem(row_i, 0, login_item)
            diff_item = QTableWidgetItem(single_data.diff, QTableWidgetItem.Type)
            diff_item.setTextAlignment(Qt.AlignCenter)
            self.ui.top10_tableWidget.setItem(row_i, 1, diff_item)
            score_value = QTableWidgetItem(str(single_data.score_value), QTableWidgetItem.Type)
            score_value.setTextAlignment(Qt.AlignCenter)
            self.ui.top10_tableWidget.setItem(row_i, 2, score_value)

    def update(self) -> None:
        super().update()
        self.update_table()

