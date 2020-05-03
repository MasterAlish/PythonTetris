from logic.field import TetrisField
from logic.shapes.generator import ShapeGenerator


class Tetris(object):
    def __init__(self, cols, rows):
        self.field = TetrisField(cols, rows)
        self.next_shape = self.random_shape()
        self.current_shape = self.random_shape()
        self.score = 0

    def step(self):
        if self.current_shape.can_move_down(self.field):
            self.current_shape.move_down(self.field)
            return True
        else:
            self.field.freeze(self.current_shape)
            self.current_shape = self.next_shape
            self.next_shape = self.random_shape()
            lines = self.field.explode()
            self.score += lines * lines * 10
            return False

    def can_go_down(self, current_shape):
        shape_bottom_y = current_shape.y + current_shape.size
        return shape_bottom_y < self.field.rows

    def touchdown(self):
        while self.step():
            pass

    def rotate(self):
        self.current_shape.rotate(self.field)

    def move_right(self):
        self.current_shape.move_right(self.field)

    def move_left(self):
        self.current_shape.move_left(self.field)

    def get_shape_future(self):
        return self.current_shape.get_future(self.field)

    def random_shape(self):
        start_x = int(self.field.cols/2-1)
        return ShapeGenerator.random_shape(start_x)
