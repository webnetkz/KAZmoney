from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

def createInfo(self, text):
    self.steam_info = QLabel(text, self)
    
    # Добавляем hover-эффект
    self.steam_info.setCursor(Qt.PointingHandCursor)
    self.steam_info.setStyleSheet("""
        QPushButton {
            color: #ffffff;
            border: none;
            padding: 7px;
            border-radius: 7px;
            font-size: 20px;
            line-heihgt: 20px;
            max-width: 20px;
            width: 20px;
        }
        
        QPushButton:hover {
            background-color: #FF0055; /* Цвет фона при наведении */
        }
    """)

    return self.steam_info