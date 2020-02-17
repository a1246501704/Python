#coding:utf-8
# pip3 install XlsxWriter
import xlsxwriter

#1.创建一个excel
work = xlsxwriter.Workbook("1.xlsx")

#2、创建表格
worksheet = work.add_worksheet("first")
worksheet1 = work.add_worksheet("second")

#3、写入内容
    #写入字符
worksheet.write("A1","For")
worksheet1.write("A1","While")
    #写入图片
worksheet.insert_image("A2","1.png")


#关闭并保存
work.close()




