from logic.tetris import Tetris
from tkinter import *

from ui.drawer import TetrisDrawer


class Keys:
    Down = 65364
    Up = 65362
    Left = 65361
    Right = 65363
    Space = 32


class TetrisUI(object):
    def __init__(self, game: Tetris):
        self.game = game
        self.root = Tk()
        self.mainframe = MainFrame(self.root, self.on_keypress, game)

    def show(self):
        self.root.title("Tetris 2020")
        self.root.geometry("500x600")
        self.root.resizable(0, 0)
        self.root.mainloop()

    def redraw_game_state(self):
        self.mainframe.redraw(self.game.field)

    def on_keypress(self, event):
        key = event.keysym_num
        if key == Keys.Space:
            self.game.touchdown()
        elif key == Keys.Up:
            self.game.rotate()
        elif key == Keys.Down:
            self.game.touchdown()
        elif key == Keys.Right:
            self.game.move_right()
        elif key == Keys.Left:
            self.game.move_left()
        self.redraw_game_state()


class MainFrame(Frame):
    def __init__(self, root, on_keypress, game):
        super().__init__(root)
        self.root = root
        self.game_panel = None
        self.info_panel = None
        self.drawer = None
        self.on_keypress = on_keypress
        self.init_ui(game)
        self.init_keyboard()

    def init_ui(self, game):
        self.pack(fill=BOTH, expand=True)

        self.game_panel = Canvas(self, bg="#FFF", width=300, height=600, bd=0, highlightthickness=0, relief='ridge')
        self.game_panel.pack(anchor=W, expand=False, side=LEFT)

        self.info_panel = Frame(self, bg="#EEE")
        self.info_panel.pack(anchor=N, fill=BOTH, expand=TRUE, side=LEFT)

        self.drawer = TetrisDrawer(self.game_panel, 300, 600, game.field)

    def init_keyboard(self):
        self.root.bind("<Key>", self.on_keypress)

    def redraw(self, field):
        self.drawer.clear()
        self.drawer.draw(field)
