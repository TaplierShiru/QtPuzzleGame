from PySide6.QtWidgets import QMessageBox


def return_qmess_box_connect_db_error(
        title: str = "Ошибка", text: str = "Ошибка подключения к БД.") -> QMessageBox:
    qmess_box = QMessageBox()
    qmess_box.setIcon(QMessageBox.Icon.Critical)
    qmess_box.setText(text)
    qmess_box.setWindowTitle(title)
    return qmess_box

