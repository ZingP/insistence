import xlrd
import xlsxwriter

def read_excel_row(excelname):
    li = []
    hash_set = set()
    workbook = xlrd.open_workbook(excelname)
    sheet = workbook.sheet_by_name('Sheet1')
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        topic = row[2]
        if topic in hash_set:
            continue
        hash_set.add(topic)
        li.append(row)
    return li