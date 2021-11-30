from PySide6.QtWidgets import QWidget

from .load_game import Ui_Form
from puzzle.database import DatabaseController
from puzzle.common.signals import SignalSenderBackToMenu
from puzzle.common.back_to_menu import BackToMenu


class QLoadGameWidget(QWidget, BackToMenu):

    def __init__(self, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_back_to_menu_signal(signal_back_to_menu=signal_back_to_menu)

        # Buttons
        self.ui.back_to_menu_pushButton.clicked.connect(self.emit_signal_back_to_menu)
        self.setLayout(self.ui.gridLayout)

