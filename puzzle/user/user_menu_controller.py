from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QStackedWidget, QGridLayout

from .menu import QUserMenuWidget
from .game import QNewGameWidget, QLoadGameWidget
from .score_table import QScoreTableWidget
from puzzle.common.about_creators import QAboutCreatorsWidget

from puzzle.common.signals import SignalSenderBackToMenu, SignalSenderChangePage
from puzzle.common.signals.signal_change_size_form import SignalSenderChangeSizeWidget
from puzzle.user.utils import (SIGNAL_MENU_INDX, SIGNAL_NEW_GAME_INDX, SIGNAL_ABOUT_CREATORS_INDX,
                               SIGNAL_LOAD_GAME_INDX, SIGNAL_SCORE_TABLE_INDX)

from puzzle.common.qdynamic_size_stacked_widget import QDynamicSizeStackedWidget
from puzzle.common.menu_controller_base import MenuControllerBase


class UserMenuController(MenuControllerBase):

    def __init__(self, user_login: str, signal_change_size: SignalSenderChangeSizeWidget):
        super().__init__(signal_change_size=signal_change_size)
        # Setup signal if need back to menu
        self.signal_back_to_menu = SignalSenderBackToMenu()
        self.signal_back_to_menu.signal.connect(lambda: self._stacked_widget.setCurrentIndex(0))

        self.signal_change_page = SignalSenderChangePage()
        self.signal_change_page.signal.connect(self.change_page)
        self.setupUI(user_login=user_login, signal_change_size=signal_change_size)

    def setupUI(self, user_login: str, signal_change_size: SignalSenderChangeSizeWidget):
        grid = QGridLayout()
        stacked_widget = QDynamicSizeStackedWidget(signal_change_size=signal_change_size)
        # TODO: Define size window W/H constants
        # Init menu, 0
        menu = QUserMenuWidget(signal_change_page=self.signal_change_page)
        stacked_widget.addWidget(menu, fixed_size=QSize(QUserMenuWidget.SIZE_WINDOW_W, QUserMenuWidget.SIZE_WINDOW_H))
        # Init new game, 1
        new_game = QNewGameWidget(user_login=user_login, signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(new_game, fixed_size=QSize(QNewGameWidget.SIZE_WINDOW_W, QNewGameWidget.SIZE_WINDOW_H))
        # Init load game, 2
        load_game = QLoadGameWidget(user_login=user_login, signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(load_game, fixed_size=QSize(QLoadGameWidget.SIZE_WINDOW_W, QLoadGameWidget.SIZE_WINDOW_H))
        # Init score table, 3
        score_table = QScoreTableWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(score_table, fixed_size=QSize(QScoreTableWidget.SIZE_WINDOW_W, QScoreTableWidget.SIZE_WINDOW_H))
        # Init about system, 4
        # Init about creators, 5
        about_creators = QAboutCreatorsWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(about_creators, fixed_size=QSize(QAboutCreatorsWidget.SIZE_WINDOW_W, QAboutCreatorsWidget.SIZE_WINDOW_H))

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
