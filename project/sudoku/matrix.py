class matrix:
    def __init__(self, sudoku):
        self.d = sudoku

    def get_one_element(self, x, y):
        return self.d[x][y]

    def get_one_column(self, y):
        column_elements = []
        for x in range(0,9):
            column_elements.append(self.get_one_element(x, y))
        return column_elements

    def matrix_print(self):
        for line in self.d:
            print(line)

    def column_print(self, y):
        print(self.get_one_column(y))
