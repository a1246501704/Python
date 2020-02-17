2.【csv模块 -Excel表格.csv】
## （1）猫砂
import csv
with open(‘sample/Excel.csv‘,‘r‘,newline=‘‘) as f:
    r=csv.reader(f)  # a按表格的行读取
    for i in r:
        print(i)
### 下面是读取内容：
 # [‘商品编号‘, ‘商品名称‘, ‘单价‘, ‘库存‘, ‘销量‘]
 # [‘1‘, ‘猫零食‘, ‘12‘, ‘3313‘, ‘5164‘]
 # [‘2‘, ‘普通猫粮‘, ‘33‘, ‘5055‘, ‘2231‘]
 # [‘3‘, ‘猫粮四合‘, ‘187‘, ‘212‘, ‘334‘]

### 要存放2行
with open(‘sample/Excel.csv‘,‘a+‘, newline=‘‘) as f:
  # with open(‘sample/Excel.csv‘,‘w+‘, newline=‘‘) as f:
  # 写入方式w/a都可以，因为没有循环for
    w=csv.writer(f)  # <class list>嵌套列表
   # 按行写入
    w.writerow([‘4‘, ‘猫砂‘, ‘25‘, ‘1022‘, ‘886‘])
    w.writerow([‘5‘, ‘猫罐头‘, ‘18‘, ‘2234‘, ‘3121‘])
with open(‘sample/Excel.csv‘,‘r‘, newline=‘‘) as f:
    h=csv.reader(f)  # <class list>嵌套列表
    for i in h:
        print(i)

## （2）写入、读取收件人
import csv
data=[[‘收件人‘,‘邮箱‘],[‘刘‘,‘702352870@qq.com‘],[‘杨‘,‘1427369427@qq.com‘]]
## excel表格.csv文件写入要 列表嵌套
with open(‘sample/recipient.csv‘,‘w‘,newline=‘‘) as a:
  # with open(‘sample/recipient.csv‘,‘a‘,newline=‘‘) as a:
  # 如果是‘a‘则第一行就是空的？？‘w‘就没有这个bug！！
  # 因为有循环for,也算写入一行，没有输出就返回空行！！
    b=csv.writer(a)  # 写入内容放入b
     # 按行写入
    for i in data:   # i=[‘收件人‘,‘邮箱‘]
       b.writerow(i)
with open(‘sample/recipient.csv‘,‘r‘,newline=‘‘) as a:
    c=csv.reader(a)  # 读取内容放入c
    for i in c:
        print(i)