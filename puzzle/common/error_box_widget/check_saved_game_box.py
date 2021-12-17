import os
from typing import Optional

from PySide6.QtWidgets import QMessageBox

from puzzle.database import DatabaseController
from puzzle.common.qmess_boxes import return_qmess_box


def check_game_exist(saved_game_id: int) -> Optional[QMessageBox]:
    saved_game = DatabaseController.get_saved_game(saved_game_id)
    if saved_game is None:
        qmess_box = return_qmess_box(
            title='Ошибка', text='Сохраненная игра не была найдена или ошибка подключения к БД.',
            icon=QMessageBox.Icon.Critical
        )
        qmess_box.show()
        DatabaseController.clear_temp()
        return qmess_box

    if not os.path.isfile(saved_game):
        qmess_box = return_qmess_box(
            title='Ошибка', text='Сохраненная игра не найдена.',
            icon=QMessageBox.Icon.Critical
        )
        qmess_box.show()
        DatabaseController.clear_temp()
        return qmess_box

