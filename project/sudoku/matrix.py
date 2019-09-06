import element, csv

MATRIX_ROW_LENGTH = 9
MATRIX_COLUMN_LENGTH = 9

class matrix:
    def __init__(self):
        # 1、将初始数据读入到matrix_all列表中
        self.matrix_all = []
        reader = csv.reader(open('data.csv'))
        y = 0
        for line in reader:
            x = 0
            for val in line:
                self.matrix_all.append(element.element(x, y, val))
                x = x+1
            y = y+1

        # 2、原始数据加工
        # 2-1、创建行列表
        # 2-2、创建列列表
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

    #def get_one_element(self, x, y):
        #return self.d[x][y]

    #def get_one_column(self, y):
        #column_elements = []
        #for x in range(0,9):
            #column_elements.append(self.get_one_element(x, y))
        #return column_elements

    #def matrix_print(self):
        #for line in self.d:
            #print(line)

    def column_print(self, y):
        print(self.get_one_column(y))
