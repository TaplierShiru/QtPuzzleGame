from PySide6.QtWidgets import QWidget
from .about_creators import Ui_Form
from puzzle.admin.core import BackToMenu
from ..core.signals import SignalSenderBackToMenu


class QAboutCreatorsWidget(QWidget, BackToMenu):

    def __init__(self, signal_back_to_menu: SignalSenderBackToMenu):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_back_to_menu_signal(signal_back_to_menu=signal_back_to_menu)
        self.ui.back_pushButton.clicked.connect(self.emit_signal_back_to_menu)
        self.setLayout(self.ui.about_creators_gridLayout)

