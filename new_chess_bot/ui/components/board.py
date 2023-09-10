from PyQt5.QtWidgets import QWidget, QTextBrowser, QVBoxLayout
from PyQt5.QtCore import Qt

def createChessboardConsole(self, board_text):
    console_widget = QWidget(self)
    console_widget.setFixedSize(150, 150)
    console_widget.setStyleSheet("border-radius: 12px; background-color: rgb(30, 30, 30); width: 0px;")  # Скругление углов и фоновый цвет
    layout = QVBoxLayout()
    
    text_browser = QTextBrowser(console_widget)
    text_browser.setPlainText(board_text)  
    text_browser.setReadOnly(True)
    text_browser.setAlignment(Qt.AlignCenter)
    
    layout.addWidget(text_browser)
    console_widget.setLayout(layout)
    
    return console_widget
