from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.old_pos = None
        self.frame_color = Qt.darkCyan

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(QPushButton("Закрыть окно", clicked=self.close))

        self.setLayout(layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return

        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setBrush(QColor(0, 0, 0, 200))
        painter.setPen(QPen(self.frame_color, 10))

        painter.drawRect(self.rect())


if __name__ == '__main__':
    app = QApplication([])

    w = Widget()
    w.resize(400, 300)
    w.show()

    app.exec()