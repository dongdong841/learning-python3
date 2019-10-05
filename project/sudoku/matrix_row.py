import observe

class matrix_row(observe.observe):
        def __init__(self):
                observe.observe.__init__(self)
                self.elements = []
                self.zero_cnt = 0
                self.zero_item_list = []

        def init_data(self):
                for i in self.elements:
                        if i.val == 0:
                              self.zero_item_list.append(i)
                self.zero_cnt = len(self.zero_item_list)

        def add(self, e):
                self.elements.append(e)

        def respone(self, obj):
                self.zero_item_list.remove(obj)
                self.zero_cnt = len(self.zero_item_list)
                for i in self.zero_item_list:
                        i.possible_minus(i.val)
                
