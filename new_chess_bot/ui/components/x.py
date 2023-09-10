if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Маленькая консоль с шахматной доской")
    window.setGeometry(100, 100, 200, 200)  # Установите размеры окна
    
    chessboard_console = createChessboardConsole(window)
    window.setCentralWidget(chessboard_console)
    
    window.show()
    sys.exit(app.exec_())
