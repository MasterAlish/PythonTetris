from logic.tetris import Tetris
from ui.main_window import TetrisUI


class TetrisLauncher:
    def launch(self):
        game = Tetris(10, 20)
        window = TetrisUI(game)
        window.show()
