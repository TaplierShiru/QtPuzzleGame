from typing import List

import PySide6
from PySide6.QtCore import SIGNAL, QRect, QSize
from PySide6.QtWidgets import QStackedWidget, QSizePolicy

from puzzle.common.signals.signal_change_size_form import SignalSenderChangeSizeWidget


class QDynamicSizeStackedWidget(QStackedWidget):

    def __init__(self, signal_change_size: SignalSenderChangeSizeWidget, **kwargs):
        super().__init__(**kwargs)
        self.indx2size: List[QSize] = []
        self.signal_change_size = signal_change_size

    def addWidget(self, w:PySide6.QtWidgets.QWidget, fixed_size: QSize) -> int:
        w.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.indx2size.append(fixed_size)
        super().addWidget(w)

    def setCurrentIndex(self, index:int) -> None:
        if self.currentWidget() is not None:
            self.currentWidget().setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        super().setCurrentIndex(index)
        self.currentWidget().setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.signal_change_size.signal.emit(self.indx2size[index].width(), self.indx2size[index].height(), self.currentWidget().windowTitle())

