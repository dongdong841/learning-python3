import element, csv

MATRIX_ROW_LENGTH = 9
MATRIX_COLUMN_LENGTH = 9

class matrix:
    def __init__(self):
        # 1、将初始数据读入到matrix_all列表中
        self.matrix_all = []
        reader = csv.reader(open('data.csv'))
        y = 0
        length = 0
        for line in reader:
            x = 0
            length = len(line)
            for val in line:
                self.matrix_all.append(element.element(x, y, val))
                x = x+1
            y = y+1

        # 2、原始数据加工
        # 2-1、创建行列表
        # 2-2、创建列列表
        MATRIX_ROW_LENGTH = length
        MATRIX_COLUMN_LENGTH = length
        if length == 4:
            self.init_four_lvl()
        elif length == 9:
            self.init_nine_lvl()
        else:
            print('wrong data!')
            quit()

        # 为每行每列添加元素
        for i in self.matrix_all:
            self.matrix_rows[i.y].append(i)
            self.matrix_columns[i.x].append(i)

        for line in self.matrix_rows:
            string = ''
            for i in line:
                string += ' '
                string += i.value
            print(string)

        print('')
        for line in self.matrix_columns:
            string = ''
            for i in line:
                string += ' '
                string += i.value
            print(string)

    def init_four_lvl(self):
        self.matrix_rows = []
        self.matrix_row_0 = []
        self.matrix_rows.append(self.matrix_row_0)
        self.matrix_row_1 = []
        self.matrix_rows.append(self.matrix_row_1)
        self.matrix_row_2 = []
        self.matrix_rows.append(self.matrix_row_2)
        self.matrix_row_3 = []
        self.matrix_rows.append(self.matrix_row_3)

        self.matrix_columns = []
        self.matrix_column_0 = []
        self.matrix_columns.append(self.matrix_column_0)
        self.matrix_column_1 = []
        self.matrix_columns.append(self.matrix_column_1)
        self.matrix_column_2 = []
        self.matrix_columns.append(self.matrix_column_2)
        self.matrix_column_3 = []
        self.matrix_columns.append(self.matrix_column_3)

    def init_nine_lvl(self):
        self.matrix_rows = []
        self.matrix_row_0 = []
        self.matrix_rows.append(self.matrix_row_0)
        self.matrix_row_1 = []
        self.matrix_rows.append(self.matrix_row_1)
        self.matrix_row_2 = []
        self.matrix_rows.append(self.matrix_row_2)
        self.matrix_row_3 = []
        self.matrix_rows.append(self.matrix_row_3)
        self.matrix_row_4 = []
        self.matrix_rows.append(self.matrix_row_4)
        self.matrix_row_5 = []
        self.matrix_rows.append(self.matrix_row_5)
        self.matrix_row_6 = []
        self.matrix_rows.append(self.matrix_row_6)
        self.matrix_row_7 = []
        self.matrix_rows.append(self.matrix_row_7)
        self.matrix_row_8 = []
        self.matrix_rows.append(self.matrix_row_8)

        self.matrix_columns = []
        self.matrix_column_0 = []
        self.matrix_columns.append(self.matrix_column_0)
        self.matrix_column_1 = []
        self.matrix_columns.append(self.matrix_column_1)
        self.matrix_column_2 = []
        self.matrix_columns.append(self.matrix_column_2)
        self.matrix_column_3 = []
        self.matrix_columns.append(self.matrix_column_3)
        self.matrix_column_4 = []
        self.matrix_columns.append(self.matrix_column_4)
        self.matrix_column_5 = []
        self.matrix_columns.append(self.matrix_column_5)
        self.matrix_column_6 = []
        self.matrix_columns.append(self.matrix_column_6)
        self.matrix_column_7 = []
        self.matrix_columns.append(self.matrix_column_7)
        self.matrix_column_8 = []
        self.matrix_columns.append(self.matrix_column_8)

    def get_one_element(self, x, y):
        if (x < MATRIX_ROW_LENGTH and x >= 0) and (y < MATRIX_COLUMN_LENGTH and y >= 0):
            return (self.matrix_rows[x])[y]
        else:
            print('error x:'+str(x)+'error y:'+str(y))
            quit()

    def get_one_column(self, y):
        if y < MATRIX_COLUMN_LENGTH and y >= 0:
            return self.matrix_columns[y]
        else:
            print('error y:'+str(y))
            quit()

    def get_all_column(self):
        return self.matrix_columns

    def get_one_row(self, x):
        if x < MATRIX_ROW_LENGTH and x >= 0:
            return self.matrix_columns[x]

    def get_all_rows(self):
        return self.matrix_columns

    #def matrix_print(self):
        #for line in self.d:
            #print(line)

    #def column_print(self, y):
        #print(self.get_one_column(y))
