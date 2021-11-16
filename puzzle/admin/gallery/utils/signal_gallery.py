from PySide6.QtCore import QObject, Signal


class SignalGalleryPreview(QObject):
    #               indx
    preview = Signal(int)
