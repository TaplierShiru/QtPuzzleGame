from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QGridLayout

from .auth_widget import QAuthWidget
from .regist_widget import QRegistWidget
from .signal_reg_auth import SignalSenderAuth, SignalSenderReg

from puzzle.common.menu_controller_base import MenuControllerBase
from puzzle.common.qdynamic_size_stacked_widget import QDynamicSizeStackedWidget
from puzzle.common.signals.signal_change_size_form import SignalSenderChangeSizeWidget


class AuthRegController(MenuControllerBase):

    def __init__(self, signal_change_size: SignalSenderChangeSizeWidget):
        super().__init__(signal_change_size=signal_change_size)

        self.signal_auth = SignalSenderAuth()
        self.signal_reg = SignalSenderReg()

        self.signal_auth.signal.connect(self.show_auth)
        self.signal_reg.signal.connect(self.show_reg)

        self.setupUI(signal_change_size=signal_change_size)

    def setupUI(self, signal_change_size: SignalSenderChangeSizeWidget):
        grid = QGridLayout()
        stacked_widget = QDynamicSizeStackedWidget(signal_change_size=signal_change_size)

        # Init auth, 0
        auth = QAuthWidget(signal_reg=self.signal_reg)
        stacked_widget.addWidget(auth, fixed_size=QSize(QAuthWidget.SIZE_WINDOW_W, QAuthWidget.SIZE_WINDOW_H))

        # Init regist, 1
        regist = QRegistWidget(signal_auth=self.signal_auth)
        stacked_widget.addWidget(regist, fixed_size=QSize(QRegistWidget.SIZE_WINDOW_W, QRegistWidget.SIZE_WINDOW_H))

        stacked_widget.setCurrentIndex(0)
        self._stacked_widget = stacked_widget
        grid.addWidget(stacked_widget, 0, 0)
        self.setLayout(grid)

    def show_auth(self):
        self._stacked_widget.setCurrentIndex(0)

    def show_reg(self):
        self._stacked_widget.setCurrentIndex(1)
