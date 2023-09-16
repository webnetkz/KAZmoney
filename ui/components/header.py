from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt

from .info import createInfo
from .close import createClose

def createHeader(self):
    self.header = QHBoxLayout()

    # Добавляем кнопку "Info" в горизонтальный макет
    info_button = createInfo(self, 'This is info')
    self.header.addWidget(info_button, alignment=Qt.AlignLeft)
    
    # Добавляем кнопку "Close" в горизонтальный макет
    close_button = createClose(self)
    self.header.addWidget(close_button, alignment=Qt.AlignRight)

    return self.header