from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

def createButton(self, text='text', f=print):
    text = text.upper()
    self.steam_button = QPushButton(text, self)
    self.steam_button.clicked.connect(f)
    
    # Добавляем hover-эффект
    self.steam_button.setCursor(Qt.PointingHandCursor)
    self.steam_button.setStyleSheet("""
        QPushButton {
            background-color: #FF0033;
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            border-radius: 12px;
            font-size: 20px;
        }
        
        QPushButton:hover {
            background-color: #FF0055; /* Цвет фона при наведении */
        }
    """)

    return self.steam_button