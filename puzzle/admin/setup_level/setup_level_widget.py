from PySide6.QtWidgets import QWidget, QMessageBox

from .setup_level import Ui_SetupLevel
from puzzle.utils import DIFFIC_LIST, NUM_FRAGMENTS, TYPE_PUZZLES, TYPE_BUILD_PUZZLE
from puzzle.database import DatabaseController
from puzzle.common.signals import SignalSenderBackToMenu
from puzzle.common.back_to_menu import BackToMenu
from ...common.qmess_boxes import return_qmess_box_connect_db_error


class QSetupLevelWidget(QWidget, BackToMenu):

    SIZE_WINDOW_W = 300
    SIZE_WINDOW_H = 350

    def __init__(self, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self.__qmess_box: QMessageBox = None
        self.ui = Ui_SetupLevel()
        self.ui.setupUi(self)
        self.setup_back_to_menu_signal(signal_back_to_menu=signal_back_to_menu)

        self.ui.back_pushButton.clicked.connect(self.emit_signal_back_to_menu)
        self.ui.save_pushButton.clicked.connect(self.save_setup)
        self.setLayout(self.ui.setup_level_gridLayout)

        self.ui.diffic_comboBox.addItems(DIFFIC_LIST)
        self.ui.diffic_comboBox.currentTextChanged.connect(self.diff_changed)
        self.ui.num_frag_h_comboBox.addItems(NUM_FRAGMENTS)
        self.ui.num_frag_v_comboBox.addItems(NUM_FRAGMENTS)
        self.ui.type_build_comboBox.addItems(TYPE_BUILD_PUZZLE)
        self.ui.type_puzle_comboBox.addItems(TYPE_PUZZLES)
        self.diff_changed(DIFFIC_LIST[0])

    def diff_changed(self, name: str):
        frag_h, frag_v, type_build, type_puzzle = DatabaseController.get_diff_params(name)
        if frag_h is None:
            self.__qmess_box = return_qmess_box_connect_db_error()
            self.__qmess_box.show()
            return

        self.ui.num_frag_h_comboBox.setCurrentIndex(NUM_FRAGMENTS.index(str(frag_h)))
        self.ui.num_frag_v_comboBox.setCurrentIndex(NUM_FRAGMENTS.index(str(frag_v)))
        self.ui.type_build_comboBox.setCurrentIndex(TYPE_BUILD_PUZZLE.index(type_build))
        self.ui.type_puzle_comboBox.setCurrentIndex(TYPE_PUZZLES.index(type_puzzle))

    def save_setup(self):
        diff = self.ui.diffic_comboBox.currentText()
        frag_h = self.ui.num_frag_h_comboBox.currentText()
        frag_v = self.ui.num_frag_v_comboBox.currentText()
        type_build = self.ui.type_build_comboBox.currentText()
        type_puzzle = self.ui.type_puzle_comboBox.currentText()
        print(diff, frag_h, frag_v, type_build, type_puzzle)
        result = DatabaseController.update_diff(
            diff=diff, frag_h=frag_h, frag_v=frag_v,
            type_build=type_build, type_puzzle=type_puzzle
        )

        if not result:
            self.__qmess_box = return_qmess_box_connect_db_error()
            self.__qmess_box.show()
            return

        qmess = QMessageBox()
        qmess.setWindowTitle("??????????????????")
        qmess.setText("?????????????????? ?????? ???????????? ?????????????? ??????????????????.")
        qmess.setIcon(QMessageBox.Icon.Information)
        qmess.show()
        self.__qmess_box = qmess
