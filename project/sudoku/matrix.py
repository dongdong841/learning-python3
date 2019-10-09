import element, csv, matrix_row, matrix_column, matrix_square

class matrix:
    def __init__(self):
        # 1、将初始数据读入到matrix_all列表中
        self.matrix_all = []
        reader = csv.reader(open('data_lvl_four.csv'))
        y = 0
        length = 0
        for line in reader:
            x = 0
            length = len(line)
            for val in line:
                self.matrix_all.append(element.element(x, y, int(val)))
                x = x+1
            y = y+1

        # 2、原始数据加工
        # 2-1、创建行列表
        # 2-2、创建列列表
        self.MATRIX_ROW_LENGTH = length
        self.MATRIX_COLUMN_LENGTH = length
        self.MATRIX_SQUARE_LENGTH = length
        if length == 4:
            self.create_four_lvl()
            self.init_row_lvl_four()
            self.init_column_lvl_four()
            self.init_parts_lvl_four()
        elif length == 9:
            self.init_nine_lvl()
        else:
            print('wrong data!')
            quit()

        print('原始数独数据：')
        self.matrix_print()

        print('块数据：')
        print('0块：')
        string = ''
        for i in self.matrix_parts[0].elements:
            string += ' '
            string += str(i.value)
            string += '('
            string += str(i.x)
            string += str(i.y)
            string += ')'
        print(string)
        print('')
        print('块数据：')
        print('1块：')
        string = ''
        for i in self.matrix_parts[1].elements:
            string += ' '
            string += str(i.value)
            string += '('
            string += str(i.x)
            string += str(i.y)
            string += ')'
        print(string)
        print('')
        print('块数据：')
        print('2块：')
        string = ''
        for i in self.matrix_parts[2].elements:
            string += ' '
            string += str(i.value)
            string += '('
            string += str(i.x)
            string += str(i.y)
            string += ')'
        print(string)
        print('')
        print('块数据：')
        print('3块：')
        string = ''
        for i in self.matrix_parts[3].elements:
            string += ' '
            string += str(i.value)
            string += '('
            string += str(i.x)
            string += str(i.y)
            string += ')'
        print(string)
        print('')

    def create_four_lvl(self):
        # 创建行元素
        self.matrix_rows = []
        cnt = 0
        while cnt < self.MATRIX_ROW_LENGTH:
            self.matrix_rows.append(matrix_row.matrix_row())
            cnt += 1

        # 创建列元素
        self.matrix_columns = []
        cnt = 0
        while cnt < self.MATRIX_COLUMN_LENGTH:
            self.matrix_columns.append(matrix_column.matrix_column())
            cnt += 1

        # 创建正方形元素
        self.matrix_parts = []
        cnt = 0
        while cnt < self.MATRIX_SQUARE_LENGTH:
            self.matrix_parts.append(matrix_square.matrix_square())
            cnt += 1

    def init_row_lvl_four(self):
        for i in self.matrix_all:
            self.matrix_rows[i.y].add(i)
        for i in self.matrix_rows:
            i.init_data()

    def init_column_lvl_four(self):
        for i in self.matrix_all:
            self.matrix_columns[i.x].add(i)
        for i in self.matrix_columns:
            i.init_data()
            
    def init_parts_lvl_four(self):
        self.matrix_parts[0].add(self.matrix_rows[0].elements[0])
        self.matrix_parts[0].add(self.matrix_rows[0].elements[1])
        self.matrix_parts[0].add(self.matrix_rows[1].elements[0])
        self.matrix_parts[0].add(self.matrix_rows[1].elements[1])
        self.matrix_parts[0].init_data()

        self.matrix_parts[1].add(self.matrix_rows[0].elements[2])
        self.matrix_parts[1].add(self.matrix_rows[0].elements[3])
        self.matrix_parts[1].add(self.matrix_rows[1].elements[2])
        self.matrix_parts[1].add(self.matrix_rows[1].elements[3])
        self.matrix_parts[1].init_data()
        
        self.matrix_parts[2].add(self.matrix_rows[2].elements[0])
        self.matrix_parts[2].add(self.matrix_rows[2].elements[1])
        self.matrix_parts[2].add(self.matrix_rows[3].elements[0])
        self.matrix_parts[2].add(self.matrix_rows[3].elements[1])
        self.matrix_parts[2].init_data()

        self.matrix_parts[3].add(self.matrix_rows[2].elements[2])
        self.matrix_parts[3].add(self.matrix_rows[2].elements[3])
        self.matrix_parts[3].add(self.matrix_rows[3].elements[2])
        self.matrix_parts[3].add(self.matrix_rows[3].elements[3])
        self.matrix_parts[3].init_data()
        
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
        if (x < self.MATRIX_ROW_LENGTH and x >= 0) and (y < self.MATRIX_COLUMN_LENGTH and y >= 0):
            return (self.matrix_rows[x])[y]
        else:
            print('error x:'+str(x)+'error y:'+str(y))
            quit()

    def get_one_column(self, y):
        if y < self.MATRIX_COLUMN_LENGTH and y >= 0:
            return self.matrix_columns[y]
        else:
            print('error y:'+str(y))
            quit()

    def get_all_column(self):
        return self.matrix_columns

    def get_one_row(self, x):
        if x < self.MATRIX_ROW_LENGTH and x >= 0:
            return self.matrix_rows[x]

    def get_all_rows(self):
        return self.matrix_rows

    def get_one_square(self, row, column):
        if (row >= 0 and row <= 1) and (column >= 0 and column <= 1):
            return self.matrix_parts[0]
        elif (row >=0 and row <= 1) and (column > 1 and column <= 3):
            return self.matrix_parts[1]
        elif (row > 1 and row <=3) and (column >=0 and column <= 1):
            return self.matrix_parts[2]
        else:
            return self.matrix_parts[3]
        
    def get_all_squares(self):
        return self.matrix_parts

    def is_complete(self):
        ret = True
        for l in self.matrix_rows:
            if l.zero_cnt != 0:
                ret = False
                break
        return ret

    def matrix_print(self):
        for line in self.matrix_rows:
            string = ''
            for i in line.elements:
                string += ' '
                string += str(i.value)
            print(string)
        print('')

    #def column_print(self, y):
        #print(self.get_one_column(y))
