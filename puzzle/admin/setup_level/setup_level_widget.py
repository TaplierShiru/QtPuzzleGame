from PySide6.QtWidgets import QWidget

from .setup_level import Ui_Form
from ..core import BackToMenu
from puzzle.utils import DIFFIC_LIST, NUM_FRAGMENTS, TYPE_PUZZLES, TYPE_BUILD_PUZZLE
from puzzle.database import DatabaseController
from ..core.signals import SignalSenderBackToMenu


class QSetupLevelWidget(QWidget, BackToMenu):

    def __init__(self, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self.ui = Ui_Form()
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
        DatabaseController.update_diff(
            diff=diff, frag_h=frag_h, frag_v=frag_v,
            type_build=type_build, type_puzzle=type_puzzle
        )
