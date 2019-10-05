import subject

class element(subject.subject):
    chg_flag = False

    def __init__(self, x, y, v):
        subject.subject.__init__(self)
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
        if val != 0:
            self.possible.clear()
        chg_flag = True
        
