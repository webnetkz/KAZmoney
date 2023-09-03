
from PyQt5.QtWidgets import QLineEdit

from PyQt5.QtCore import Qt

def createInput(self, text='text'):
    self.input_field = QLineEdit(self)
    self.input_field.setPlaceholderText(text)
    self.input_field.setStyleSheet("""
        font-size: 18px;
        border-radius: 12px;
        padding: 10px 20px;
    """)
    return self.input_field