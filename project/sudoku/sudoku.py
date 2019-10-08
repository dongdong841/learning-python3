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
while e.element.chg_flag == True and mgr.is_complete() == False:
    e.element.chg_flag = False
    controler.calc_row_one_less(mgr)
    controler.calc_column_one_less(mgr)
    controler.calc_square_one_less(mgr)

mgr.matrix_print()

del mgr
del controler
