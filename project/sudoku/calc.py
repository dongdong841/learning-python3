import matrix as d

class calc_lvl_four:
        def __init_(self):
                pass

        def row_one_less(self, m):
                for line in m.get_all_rows():
                        # 看看本行是否是只少一个元素
                        ret, x, y, row_data = self.is_one_less(line)
                        if ret == True:
                                tgt_data = [1,2,3,4]
                                for i in tgt_data:
                                        if i not in row_data:
                                                m.get_one_element(x, y).chg_val(i)
                                

        def is_one_less(self, l):
                zero_cnt = 0
                line_data = []
                x = 0
                y = 0
                for i in l:
                        if i.val == 0:
                                zero_cnt += 1
                                x = i.x
                                y = i.y
                        else:
                                line_data.append(i.val)

                if zero_cnt > 1:
                        return False, x, y, line_data
                elif zero_cnt = 0:
                        return False, x, y, line_data
                else:
                        return True, x, y, line_data
                        
