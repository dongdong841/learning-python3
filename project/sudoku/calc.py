import matrix as d

class calc_lvl_four:
        def __init_(self):
                pass

        def init_possible_for_row(self, m):
                for i in m.matrix_rows:
                        if i.zero_cnt != 0:
                                # 找出这一行中缺少的值
                                less_val_list = [1,2,3,4]
                                for e in i.elements:
                                        if e.val != 0:
                                               less_val_list.remove(e.val)
                                # 为每个空元素初始化可能的值
                                for e in i.zero_item_list:
                                        for val in less_val_list:
                                                e.possible_add_for_row(val)

        def init_possible_for_column(self, m):
                for i in m.matrix_columns:
                        if i.zero_cnt != 0:
                                # 找出这一行中缺少的值
                                less_val_list = [1,2,3,4]
                                for e in i.elements:
                                        if e.val != 0:
                                               less_val_list.remove(e.val)
                                # 为每个空元素初始化可能的值
                                for e in i.zero_item_list:
                                        for val in less_val_list:
                                                e.possible_add_for_column(val)

        def init_possible_for_square(self, m):
                for i in m.matrix_parts:
                        if i.zero_cnt != 0:
                                # 找出这一行中缺少的值
                                less_val_list = [1,2,3,4]
                                for e in i.elements:
                                        if e.val != 0:
                                               less_val_list.remove(e.val)
                                # 为每个空元素初始化可能的值
                                for e in i.zero_item_list:
                                        for val in less_val_list:
                                                e.possible_add_for_square(val)               
                
        def calc_row_one_less(self, m):
                for line in m.get_all_rows():
                        # 看看本行是否是只少一个元素
                        if line.zero_cnt == 1:
                                # 少的那个值就是空元素的possible中仅剩的值
                                line.zero_item_list[0].chg_val(line.zero_item_list[0].row_possible[0])

        def calc_column_one_less(self, m):
                for line in m.get_all_column():
                        # 看看本行是否是只少一个元素
                        if line.zero_cnt == 1:
                                # 少的那个值就是空元素的possible中仅剩的值
                                line.zero_item_list[0].chg_val(line.zero_item_list[0].column_possible[0])

        def calc_square_one_less(self, m):
                for line in m.get_all_squares():
                        # 看看本行是否是只少一个元素
                        if line.zero_cnt == 1:
                                # 少的那个值就是空元素的possible中仅剩的值
                                line.zero_item_list[0].chg_val(line.zero_item_list[0].square_possible[0])        

        def calc_row_exclude(self, m):
                for line in m.get_all_rows():
                        # 本行是否缺少多个元素
                        if line.zero_cnt > 1:
                                for e in line.zero_item_list:
                                        confirm_list = []
                                        for v in e.row_possible:
                                                confirm_list.append(v)
                                        # 看看这个空元素的可能值是否与所在列和所在块的值冲突，将冲突的值删除
                                        # 1、获取所在列的已存在的元素值
                                        column_exsit_list = []
                                        for i in m.get_one_column(e.x):
                                                if i.value != 0:
                                                        column_exsit_list.append(i.value)
                                        # 2、拿掉冲突的值
                                        for v in confirm_list:
                                                if v in column_exsit_list:
                                                        confirm_list.remove(v)
                                        # 3、获取所在块的已存在的元素值
                                        square_exsit_list = []
                                        for i in m.get_one_square(e.y, e.x):
                                                if i.value != 0:
                                                        square_exsit_list.append(i.value)
                                        # 4、拿掉冲突的值
                                        for v in confirm_list:
                                                if v in square_exsit_list:
                                                        confirm_list.remove(v)
                                        if len(confirm_list) == 1:
                                                e.chg_val(confirm_list[0])
