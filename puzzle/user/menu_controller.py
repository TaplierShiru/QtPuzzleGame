from PySide6.QtWidgets import QWidget, QStackedWidget, QGridLayout

from .menu import QUserMenuWidget
from .game import QNewGameWidget, QLoadGameWidget
from .score_table import QScoreTableWidget
from puzzle.common.about_creators import QAboutCreatorsWidget

from puzzle.common.signals import SignalSenderBackToMenu, SignalSenderChangePage
from puzzle.user.utils import (SIGNAL_MENU_INDX, SIGNAL_NEW_GAME_INDX, SIGNAL_ABOUT_CREATORS_INDX,
                               SIGNAL_LOAD_GAME_INDX, SIGNAL_SCORE_TABLE_INDX)


class MenuController(QWidget):

    def __init__(self):
        super().__init__()
        # Setup signal if need back to menu
        self.signal_back_to_menu = SignalSenderBackToMenu()
        self.signal_back_to_menu.signal.connect(lambda: self._stacked_widget.setCurrentIndex(0))

        self.signal_change_page = SignalSenderChangePage()
        self.signal_change_page.signal.connect(self.change_page)
        self.setupUI()

    def setupUI(self):
        grid = QGridLayout()
        stacked_widget = QStackedWidget()
        # Init menu, 0
        menu = QUserMenuWidget(signal_change_page=self.signal_change_page)
        stacked_widget.addWidget(menu)
        # Init new game, 1
        new_game = QNewGameWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(new_game)
        # Init load game, 2
        load_game = QLoadGameWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(load_game)
        # Init score table, 3
        score_table = QScoreTableWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(score_table)
        # Init about system, 4
        # Init about creators, 5
        about_creators = QAboutCreatorsWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(about_creators)

        self.num_to_widget_dict = {
            str(SIGNAL_MENU_INDX)           : menu,
            str(SIGNAL_NEW_GAME_INDX)       : new_game,
            str(SIGNAL_LOAD_GAME_INDX)      : load_game,
            str(SIGNAL_SCORE_TABLE_INDX)    : score_table,
            str(SIGNAL_ABOUT_CREATORS_INDX) : about_creators,
        }
        stacked_widget.setCurrentIndex(0)
        self._stacked_widget = stacked_widget
        grid.addWidget(stacked_widget, 0, 0)
        self.setLayout(grid)

    def change_page(self, target_page: int):
        self.num_to_widget_dict[str(target_page)].update()
        self._stacked_widget.setCurrentIndex(target_page)

