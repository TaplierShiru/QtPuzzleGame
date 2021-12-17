import pathlib
from typing import Optional

from PySide6.QtCore import QTemporaryFile, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QMessageBox

from puzzle.common.qmess_boxes import return_qmess_box


class GuideController:

    FOLDER_GUIDE = "guide_data"

    URL = f'{pathlib.Path().resolve()}/{FOLDER_GUIDE}/page.html'

    @staticmethod
    def open_webpage() -> bool:
        """
        Return True - if success
            False - otherwise

        """
        try:
            return QDesktopServices.openUrl(QUrl.fromLocalFile(GuideController.URL))
        except Exception:
            return False

    @staticmethod
    def open_webpage_catch_error() -> Optional[QMessageBox]:
        result = GuideController.open_webpage()
        if result:
            return

        qmess_box = return_qmess_box(
            title="Ошибка", text="Ошибка при открытие справки.\nВозможно файл отсутствует или поврежден.",
            icon=QMessageBox.Icon.Critical
        )
        return qmess_box

