import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from .user_menu import Ui_Form
from puzzle.common.signals import SignalSenderChangePage
from puzzle.user.utils import (SIGNAL_MENU_INDX, SIGNAL_NEW_GAME_INDX, SIGNAL_ABOUT_CREATORS_INDX,
                               SIGNAL_LOAD_GAME_INDX, SIGNAL_SCORE_TABLE_INDX)


class QUserMenuWidget(QWidget):

    def __init__(self, signal_change_page: SignalSenderChangePage):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.signal_change_page = signal_change_page
        # Buttons
        self.ui.new_game_pushButton.clicked.connect(self.clicked_new_game)
        self.ui.load_game_pushButton.clicked.connect(self.clicked_load_game)
        self.ui.leader_board_pushButton.clicked.connect(self.clicked_score_table)
        self.ui.about_creators_pushButton.clicked.connect(self.clicked_about_creators)
        self.ui.exit_pushButton.clicked.connect(lambda: sys.exit(-1))
        # Other settings
        self.ui.user_menu_verticalLayout.setAlignment(Qt.AlignHCenter)
        self.setLayout(self.ui.user_menu_verticalLayout)

    def clicked_new_game(self):
        self.signal_change_page.signal.emit(SIGNAL_NEW_GAME_INDX)

    def clicked_about_creators(self):
        self.signal_change_page.signal.emit(SIGNAL_ABOUT_CREATORS_INDX)

    def clicked_load_game(self):
        self.signal_change_page.signal.emit(SIGNAL_LOAD_GAME_INDX)

    def clicked_score_table(self):
        self.signal_change_page.signal.emit(SIGNAL_SCORE_TABLE_INDX)

