from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

def createClose(self):
    self.steam_button = QPushButton('x', self)
    self.steam_button.clicked.connect(self.close)
    
    # Добавляем hover-эффект
    self.steam_button.setCursor(Qt.PointingHandCursor)
    self.steam_button.setStyleSheet("""
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

    return self.steam_button