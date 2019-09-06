class element:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.value = v
        self.possible = []

    def possible_add(val):
        if val not in self.possible:
            self.possible.append(val)

    def possible_minus(val):
        del self.possible[self.possible.index(val)]
        
