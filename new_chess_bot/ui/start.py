import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_secure import Ui_SecureWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SecureWindow()
        self.ui.setupUi(self)
        self.ui.NextButton.clicked.connect(self.print_input_value)

    def print_input_value(self):
        input_value = self.ui.CodeInput.text()
        print(f"Input Value: {input_value}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
