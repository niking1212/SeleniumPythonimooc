# coding=utf-8
import xlrd
from xlutils.copy import copy


class ExcelUitl(object):
    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            self.excel_path = "D:/pycharm/imooc/163/config/casedata.xls"
        else:
            self.excel_path = excel_path
        if index is None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]

    # 获取excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []
        rows = self.get_lines()[0]
        if rows is not None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        else:
            return None

    # 获取excel行数列数
    def get_lines(self):
        cols = self.table.ncols  # 列数
        rows = self.table.nrows  # 行数
        if rows >= 1 and cols >= 1:
            return rows, cols
        else:
            return None

    # 获取单元格的数据
    def get_col_value(self, row, col):
        if self.get_lines()[0] > row and self.get_lines()[1] > col:
            data = self.table.cell(row, col).value
            return data
        else:
            return None

    # 写入数据
    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)


if __name__ == '__main__':
    ex = ExcelUitl("D:/pycharm/imooc/163/config/keyword.xls")
    print(ex.get_col_value(3, 2))
