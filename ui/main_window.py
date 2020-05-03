from logic.tetris import Tetris
from tkinter import *


class TetrisUI(object):
    def __init__(self, game: Tetris):
        self.game = game
        self.root = Tk()
        self.root.title("Tetris 2020")
        self.root.geometry("500x600")
        self.root.resizable(0, 0)
        self.mainframe = MainFrame(self.root)

    def show(self):
        self.root.mainloop()


class MainFrame(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.game_panel = None
        self.info_panel = None
        self.init_ui()

    def init_ui(self):
        self.pack(fill=BOTH, expand=True)

        self.game_panel = Canvas(self, bg="#FFF", width=300, height=600)
        self.game_panel.pack(anchor=W, expand=False, side=LEFT)

        self.info_panel = Frame(self, bg="#EEE")
        self.info_panel.pack(anchor=N, fill=BOTH, expand=TRUE, side=LEFT)
