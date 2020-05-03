from logic.field import TetrisField


class Tetris(object):
    def __init__(self, cols, rows):
        self.field = TetrisField(cols, rows)

    def generate_cells(self):
        pass

    def touchdown(self):
        pass

    def rotate(self):
        pass

    def move_right(self):
        pass

    def move_left(self):
        pass
