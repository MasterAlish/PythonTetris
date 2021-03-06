from tkinter import messagebox

from logic.field import TetrisField
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
        self.game_over = False
        self.game = game
        self.root = Tk()
        self.mainframe = MainFrame(self.root, self.on_keypress, game)

    def show(self):
        self.start_timer()
        self.root.title("Tetris 2020")
        self.root.geometry("500x600")
        self.root.resizable(0, 0)
        self.root.mainloop()

    def start_timer(self):
        self.game_over = False
        self.on_timer()

    def on_timer(self):
        self.tick()
        if not self.game_over:
            self.root.after(1000, self.on_timer)

    def tick(self):
        self.game.step()
        self.redraw_game_state()
        if self.game.is_over():
            self.game_over = True
            messagebox.showinfo("Game over!", "Your score: %d" % self.game.score)

    def redraw_game_state(self):
        self.mainframe.redraw(self.game)

    def on_keypress(self, event):
        if not self.game_over:
            key = event.keysym_num
            if key == Keys.Space:
                self.game.touchdown()
            elif key == Keys.Up:
                self.game.rotate()
            elif key == Keys.Down:
                self.game.step()
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
        self.score_label_var = None
        self.next_shape_panel = None
        self.drawer = None
        self.next_shape_drawer = None
        self.on_keypress = on_keypress
        self.init_ui(game)
        self.init_keyboard()

    def init_ui(self, game):
        self.pack(fill=BOTH, expand=True)

        self.game_panel = Canvas(self, bg="#FFF", width=300, height=600, bd=0, highlightthickness=0, relief='ridge')
        self.game_panel.pack(anchor=W, expand=False, side=LEFT)

        self.info_panel = Frame(self, bg="#EEE")
        self.info_panel.pack(anchor=N, fill=BOTH, expand=TRUE, side=LEFT)

        self.score_label_var = StringVar(value="Score: 0")
        score_label = Label(self.info_panel, bg="#EEE", textvariable=self.score_label_var)
        score_label.pack()

        self.next_shape_panel = Canvas(self.info_panel, bg="#FFF", width=100, height=100, bd=0, highlightthickness=0, relief='ridge')
        self.next_shape_panel.pack()

        self.drawer = TetrisDrawer(self.game_panel, 300, 600, game.field)
        self.next_shape_drawer = TetrisDrawer(self.next_shape_panel, 100, 100, TetrisField(4, 4))

    def init_keyboard(self):
        self.root.bind("<Key>", self.on_keypress)

    def redraw(self, game: Tetris):
        self.drawer.clear()
        self.drawer.draw(game.field)
        self.drawer.draw_shape(game.get_shape_future(), game.field, transparent=True)
        self.drawer.draw_shape(game.current_shape, game.field)

        next_shape = game.next_shape.clone()
        next_shape.x = 0
        self.next_shape_drawer.clear()
        self.next_shape_drawer.draw_shape(next_shape, TetrisField(4, 4))

        self.score_label_var.set("Score: %d" % game.score)
