import chess
import cv2
# from find_board import get_start_position
# position_board = get_start_position()

# BOARD_SIZE = position_board[2]-4
# DARK_SQUARE_THRESHOLD = 160
# CELL_SIZE = int(BOARD_SIZE / 8)
# BOARD_TOP_COORD = position_board[1]+4
# BOARD_LEFT_COORD = position_board[0]+3


from PyQt6 import QtGui
from PyQt6.QtCore import Qt
import win32gui
import win32ui
import win32con

hwnd = win32gui.GetDesktopWindow()
wDC = win32gui.GetWindowDC(hwnd)
dc = win32ui.CreateDCFromHandle(wDC)

painter = QtGui.QPainter()
painter.begin(dc)

pen = QtGui.QPen(Qt.red)
pen.setWidth(5)
painter.setPen(pen)

painter.drawLine(0, 0, 500, 500)

painter.end()
dc.DeleteDC()
win32gui.ReleaseDC(hwnd, wDC)






#draw_square_on_screen(200, 200, 500)

#draw_square_on_screen(BOARD_LEFT_COORD, BOARD_TOP_COORD, BOARD_SIZE)


# тестовый код
if __name__ == '__main__':
  m = "g1f3"
  b = "rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 1"
 
