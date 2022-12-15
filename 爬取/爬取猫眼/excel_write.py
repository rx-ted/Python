import xlwt


def save_to_excel(doc_save_path, sheet_name, data):
    f = xlwt.Workbook()
    sheet = f.add_sheet(sheet_name, cell_overwrite_ok=True)
    for row, row_data in enumerate(data):
        for column, column_data in enumerate(row_data):
            sheet.write(row, column, str(column_data))
    f.save(doc_save_path+".xls")

'''
import xlwt
def wite_to_excel(name):
　　filename = name + '.xls'  #定义Excel名字
　　wbk = xlwt.Workbook()  #实例化一个Excel
　　sheet1 = wbk.add_sheet('sheet1',cell_overwrite_ok=True) #添加该Excel的第一个sheet，如有需要可依次添加sheet2等
　　fileds = [u'ID编号',u'名字'] #直接定义结果集的各字段名
　　execude_sql(1024)  #调用函数执行SQL，获取结果集
　　for filed in range(0,len(fileds)):   #写入字段信息
　　　　sheet1.write(0,filed,fileds[i])
　　for row in range(1,len(result)+1):　　#写入SQL查询数据
　　　　for col in range(0,len(fileds))
　　　　　　sheet1.write(row,col,result[row-1][col])
　　wbk.save(filename)　　#保存Excel

'''



