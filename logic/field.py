class TetrisField(object):
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.cells = self.generate_cells()

    def generate_cells(self):
        return [[0 for x in range(self.cols)] for y in range(self.rows)]

    def freeze(self, shape):
        for row in range(shape.size):
            for col in range(shape.size):
                shape_cell_color = shape.cells[row][col]
                if shape_cell_color:
                    self.cells[shape.y + row][shape.x + col] = shape_cell_color

    def explode(self):
        rows_to_remove = []
        for row in range(self.rows):
            if all(map(lambda x: x > 0, self.cells[row])):
                rows_to_remove.append(row)

        for row in rows_to_remove:
            self.remove_row(row)

        return len(rows_to_remove)

    def remove_row(self, row):
        for col in range(self.cols):
            self.cells[row][col] = 0

        for y in range(row, 0, -1):
            for col in range(self.cols):
                self.cells[y][col] = self.cells[y-1][col]

    def clashes_with(self, shape):
        for row in range(shape.size):
            for col in range(shape.size):
                shape_cell_color = shape.cells[row][col]
                field_y = shape.y + row
                field_x = shape.x + col
                if shape_cell_color:
                    if field_x < 0 or field_x >= self.cols:
                        return True
                    if field_y < 0 or field_y >= self.rows:
                        return True
                    cell_color = self.cells[field_y][field_x]
                    if cell_color:
                        return True
        return False
