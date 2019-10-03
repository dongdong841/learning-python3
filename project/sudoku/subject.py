
class subject:
        def __init__(self):
                self.observe_list = []
        def add(self, obj):
                if obj not in self.observe_list:
                        self.observe_list.append(obj)
        def remove(self, obj):
                if obj in self.observe_list:
                        self.observe_list.remove(obj)
        def notify_observes(self):
                if len(self.observe_list) ==0:
                        pass
                else:
                        for i in self.observe_list:
                                i.respone(self)
        
