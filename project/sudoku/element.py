import subject

class element(subject.subject):
    chg_flag = False

    def __init__(self, x, y, v):
        subject.subject.__init__(self)
        self.x = x
        self.y = y
        self.value = v
        self.row_possible = []
        self.column_possible =[]
        self.square_possible = []
        element.chg_flag = True

    def possible_add_for_row(self, val):
        if val not in self.row_possible:
            self.row_possible.append(val)
            element.chg_flag = True

    def possible_minus_for_row(self, val):
        del self.row_possible[self.row_possible.index(val)]
        element.chg_flag = True

    def possible_add_for_column(self, val):
        if val not in self.column_possible:
            self.column_possible.append(val)
            element.chg_flag = True

    def possible_minus_for_column(self, val):
        del self.column_possible[self.column_possible.index(val)]
        element.chg_flag = True

    def possible_add_for_square(self, val):
        if val not in self.square_possible:
            self.square_possible.append(val)
            element.chg_flag = True

    def possible_minus_for_square(self, val):
        del self.square_possible[self.square_possible.index(val)]
        element.chg_flag = True

    def chg_val(self, val):
        self.value = val
        if val != 0:
            self.row_possible.clear()
            self.column_possible.clear()
            self.square_possible.clear()
            self.notify_observes()
        element.chg_flag = True
        
