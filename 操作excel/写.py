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

def write2excel(data_list, file_path, column_names):
    workbook = xlsxwriter.Workbook(file_path)
    sheet1 = workbook.add_worksheet()
    #column_names = ["中心词", "节目id", "节目名称","节目摘要"]
    for i in range(len(column_names)):
        sheet1.write(0, i, column_names[i])
    # 将数据写入
    for i, row_li in enumerate(data_list):
        sheet1_row = i+1
        for j in range(len(row_li)):
            print(sheet1_row, j, row_li[j])
            sheet1.write(sheet1_row, j, row_li[j])
    workbook.close()

    