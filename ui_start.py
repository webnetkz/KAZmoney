from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
import threading
import subprocess
import pyautogui as pg
import time


class MatrixChess(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        self.start_btn = MDRectangleFlatButton(
                    text="Calibration for starting",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    on_release=self.start_calibration
                )
        self.start_text = MDLabel(
                    text="Please start the game of chess against the computer with white. Make sure the chessboard is not obscured by other windows and run the calibration. You will need to go through several steps.",
                    halign="center",
                    theme_text_color="Primary",
                    pos_hint={"center_x": 0.5, "center_y": 0.8},
                    padding_x=30
                )

        return (
            MDScreen(
                self.start_text,
                self.start_btn
            )
        )
    

    def start_calibration(self, instance):
        self.start_text.text = "Pleace wait"
        instance.text="Loading..."

        # Получение стартовой позиции и ширины шахматной доски
        from find_board import get_start_position
        position_board = get_start_position()

        if position_board == None:
            self.start_text.text = "Please make sure the entire chessboard is visible"
            instance.text="Reset"
        else:
          #instance.parent.remove_widget(instance)
          
          from draw import draw_rect
          threading.Thread(target = draw_rect, args = (position_board[0]+3, position_board[1]+4, position_board[2]-4)).start()
          self.start_text.text = "Okay, the last step is left. Start the game as black pieces."
          # Перебераем все квадраты
          subprocess.run(['python3', 'find_figures.py'])
          instance.text = "Make sure you start playing as black"




MatrixChess().run()

