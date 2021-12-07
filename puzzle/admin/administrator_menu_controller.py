from PySide6.QtCore import QRect, QSize
from PySide6.QtWidgets import QGridLayout

from .menu import QAdminMenuWidget
from puzzle.common.about_creators import QAboutCreatorsWidget
from .gallery import QGalleryWidget
from .create_game import QCreateGameWidget
from .setup_level import QSetupLevelWidget

from puzzle.common.signals import SignalSenderBackToMenu, SignalSenderChangePage
from puzzle.common.signals.signal_change_size_form import SignalSenderChangeSizeWidget
from puzzle.admin.utils import (SIGNAL_ABOUT_CREATORS_INDX, SIGNAL_GALLERY_INDX, SIGNAL_SETUP_LEVEL_INDX,
                                SIGNAL_MENU_INDX, SIGNAL_CREATE_GAME_INDX)

from puzzle.common.qdynamic_size_stacked_widget import QDynamicSizeStackedWidget
from puzzle.common.menu_controller_base import MenuControllerBase


class AdministratorMenuController(MenuControllerBase):

    def __init__(self, signal_change_size: SignalSenderChangeSizeWidget):
        super().__init__(signal_change_size=signal_change_size)
        # Setup signal if need back to menu
        self.signal_back_to_menu = SignalSenderBackToMenu()
        self.signal_back_to_menu.signal.connect(lambda: self._stacked_widget.setCurrentIndex(0))

        self.signal_change_page = SignalSenderChangePage()
        self.signal_change_page.signal.connect(self.change_page)
        self.setupUI(signal_change_size=signal_change_size)

    def setupUI(self, signal_change_size):
        grid = QGridLayout()
        stacked_widget = QDynamicSizeStackedWidget(signal_change_size)
        # Init menu, 0
        menu = QAdminMenuWidget(signal_change_page=self.signal_change_page)
        stacked_widget.addWidget(menu, fixed_size=QSize(QAdminMenuWidget.SIZE_WINDOW_W, QAdminMenuWidget.SIZE_WINDOW_H))
        # Init gallery, 1
        gallery = QGalleryWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(gallery, fixed_size=QSize(QGalleryWidget.SIZE_WINDOW_W, QGalleryWidget.SIZE_WINDOW_H))
        # Init change level, 2
        setup_level = QSetupLevelWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(setup_level, fixed_size=QSize(QSetupLevelWidget.SIZE_WINDOW_W, QSetupLevelWidget.SIZE_WINDOW_H))
        # Init create game, 3
        create_game = QCreateGameWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(create_game, fixed_size=QSize(QCreateGameWidget.SIZE_WINDOW_W, QCreateGameWidget.SIZE_WINDOW_H))
        # Init about system, 4
        # Init about creators, 5
        about_creators = QAboutCreatorsWidget(signal_back_to_menu=self.signal_back_to_menu)
        stacked_widget.addWidget(about_creators, fixed_size=QSize(QAboutCreatorsWidget.SIZE_WINDOW_W, QAboutCreatorsWidget.SIZE_WINDOW_H))

        self.num_to_widget_dict = {
            str(SIGNAL_MENU_INDX)           : menu,
            str(SIGNAL_GALLERY_INDX)        : gallery,
            str(SIGNAL_SETUP_LEVEL_INDX)    : setup_level,
            str(SIGNAL_CREATE_GAME_INDX)    : create_game,
            str(SIGNAL_ABOUT_CREATORS_INDX) : about_creators,
        }
        stacked_widget.setCurrentIndex(0)
        self._stacked_widget = stacked_widget
        grid.addWidget(stacked_widget, 0, 0)
        self.setLayout(grid)

    def change_page(self, target_page: int):
        self.num_to_widget_dict[str(target_page)].update()
        self._stacked_widget.setCurrentIndex(target_page)

