from PySide6.QtWidgets import QWidget

from .score_table import Ui_Form
from puzzle.database import DatabaseController
from puzzle.common.signals import SignalSenderBackToMenu
from puzzle.common.back_to_menu import BackToMenu
from puzzle.utils import TYPE_SCORE


class QScoreTableWidget(QWidget, BackToMenu):

    def __init__(self, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_back_to_menu_signal(signal_back_to_menu=signal_back_to_menu)

        self.ui.type_score_comboBox.addItems(TYPE_SCORE)
        # Buttons
        self.ui.back_to_menu_pushButton.clicked.connect(self.emit_signal_back_to_menu)
        self.setLayout(self.ui.gridLayout)

