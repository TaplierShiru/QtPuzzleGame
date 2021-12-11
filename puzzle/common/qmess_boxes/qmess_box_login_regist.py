from PySide6.QtWidgets import QMessageBox


def return_qmess_box_login_regist_error(title: str, text: str) -> QMessageBox:
    qmess_box = QMessageBox()
    qmess_box.setIcon(QMessageBox.Icon.Warning)
    qmess_box.setText(text)
    qmess_box.setWindowTitle(title)
    return qmess_box

