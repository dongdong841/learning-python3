import matrix as m
import calc as c
import element as e

# 输出这个数独
#for i in sudoku:
    #print(i)

mgr = m.matrix()
controler = c.calc_lvl_four()
controler.init_possible_for_row(mgr)
controler.init_possible_for_column(mgr)
controler.init_possible_for_square(mgr)

e.element.chg_flag = True
while mgr.is_complete() == False:
    if e.element.chg_flag == True:
        e.element.chg_flag = False
        controler.calc_row_one_less(mgr)
        mgr.matrix_print()
        controler.calc_column_one_less(mgr)
        mgr.matrix_print()
        controler.calc_square_one_less(mgr)
        mgr.matrix_print()
        controler.calc_row_exclude(mgr)
        mgr.matrix_print()
        controler.calc_column_exclude(mgr)
        mgr.matrix_print()
        controler.calc_square_exclude(mgr)
        mgr.matrix_print()
    else:
        # 仍然存在空元素，但是无法确定该填什么的情况
        # 根据行或列的可能值主动选择一个
        controler.choice_and_change(mgr)


del mgr
del controler
