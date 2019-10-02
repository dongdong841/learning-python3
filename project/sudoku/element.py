class element:
    chg_flag = False

    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.value = v
        self.possible = []
        chg_flag = True

    def possible_add(val):
        if val not in self.possible:
            self.possible.append(val)
            chg_flag = True

    def possible_minus(val):
        del self.possible[self.possible.index(val)]
        chg_flag = True

    def chg_val(val):
        self.value = val
        chg_flag = True
        
