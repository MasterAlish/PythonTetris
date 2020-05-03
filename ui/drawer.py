from random import randint
from tkinter import Canvas

from logic.field import TetrisField


def color():
    colors = ["#F00", "#FF0", "#FF4", "#0FF", "#0F0", "#00F"]
    r = randint(0, len(colors) - 1)
    return colors[r]


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

    def clear(self):
        pass

    def draw(self, field: TetrisField):
        for row in range(field.rows):
            for col in range(field.cols):
                cell = self.cells[row][col]
                self.canvas.itemconfig(cell, fill=color())

    def new_cell(self, canvas, col, row, cell_width, cell_height):
        x = col * cell_width
        y = row * cell_height
        x2 = x + cell_width
        y2 = y + cell_height

        if col == self.cols - 1:
            x2 -= 1
        if row == self.rows - 1:
            y2 -= 1
        return self.canvas.create_rectangle(x, y, x2, y2, outline="#444", fill="#FFF")
