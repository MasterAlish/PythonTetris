from tkinter import Canvas

from logic.field import TetrisField
from logic.shapes.shape import Shape


def color(cell_color):
    colors = ["#58d3df", "#d04a74", "#9d08c8", "#f6c983", "#e88071", "#27cf7b"]
    return colors[cell_color % len(colors)]


class TetrisDrawer(object):
    def __init__(self, canvas: Canvas, width, height, field: TetrisField):
        self.width = width
        self.height = height
        self.cols = field.cols
        self.rows = field.rows
        self.canvas = canvas
        self.cells = self.create_cells(canvas)

    def create_cells(self, canvas):
        cell_width = self.width / self.cols
        cell_height = self.height / self.rows
        return [
            [self.new_cell(self.canvas, col, row, cell_width, cell_height) for col in range(self.cols)]
            for row in range(self.rows)
        ]

    def new_cell(self, canvas, col, row, cell_width, cell_height):
        x = col * cell_width
        y = row * cell_height
        x2 = x + cell_width
        y2 = y + cell_height

        if col == self.cols - 1:
            x2 -= 1
        if row == self.rows - 1:
            y2 -= 1
        return self.canvas.create_rectangle(x, y, x2, y2, outline="#2d356f", width=2, fill="#2d356f")

    def clear(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                self.canvas.itemconfig(cell, fill="#2d356f")

    def draw(self, field: TetrisField):
        for row in range(field.rows):
            for col in range(field.cols):
                cell = self.cells[row][col]
                cell_color = field.cells[row][col]
                if cell_color:
                    self.canvas.itemconfig(cell, fill=color(cell_color))
                else:
                    self.canvas.itemconfig(cell, fill="#2d356f")

    def draw_shape(self, shape: Shape, field: TetrisField, transparent=False):
        for row in range(shape.size):
            for col in range(shape.size):
                shape_cell_color = shape.cells[row][col]
                if shape_cell_color:
                    cell = self.cells[shape.y + row][shape.x + col]
                    cell_color = field.cells[row][col]
                    if shape_cell_color:
                        if not transparent:
                            self.canvas.itemconfig(cell, fill=color(shape_cell_color))
                        else:
                            self.canvas.itemconfig(cell, fill="#37407f")
                    elif cell_color:
                        self.canvas.itemconfig(cell, fill=color(cell_color))
