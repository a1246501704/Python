#spam.py
print('from the spam.py')
__all__=['money','read1'] #from ... import *

money=1000

def read1():
    print('spam模块：',money)

def read2():
    print('spam模块')
    read1()

def change():
    global money
    money=0

# print(__name__) #文件spam.py当做脚本执行，该值等于__main__,文件spam.py当做模块被导入时，该值等于spam
if __name__ == '__main__':
    read1()
    read2()
    change()