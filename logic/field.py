class TetrisField(object):
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.cells = self.generate_cells()

    def generate_cells(self):
        return [[0 for x in range(self.cols)] for y in range(self.rows)]
