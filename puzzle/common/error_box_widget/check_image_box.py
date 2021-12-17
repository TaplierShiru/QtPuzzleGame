import os
from typing import Optional

from PySide6.QtWidgets import QMessageBox

from puzzle.database import DatabaseController
from puzzle.common.qmess_boxes import return_qmess_box


def check_img_exist(img_id: int) -> Optional[QMessageBox]:
    img_path = DatabaseController.get_img(img_id)
    if img_path is None:
        qmess_box = return_qmess_box(
            title='Ошибка', text='Изображение не было найдено или ошибка подключения к БД.',
            icon=QMessageBox.Icon.Critical
        )
        qmess_box.show()
        DatabaseController.clear_temp()
        return qmess_box

    if not os.path.isfile(img_path):
        qmess_box = return_qmess_box(
            title='Ошибка', text='Изображение не было найдено.',
            icon=QMessageBox.Icon.Critical
        )
        qmess_box.show()
        DatabaseController.clear_temp()
        return qmess_box

