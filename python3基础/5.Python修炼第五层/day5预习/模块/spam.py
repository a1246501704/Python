print('from the spam.py')
__all__=['money','x']  #对 from spam import * 有用
money=1000
x=1
def read1():
    print('spam->read1->money',money)

def read2():
    print('spam->read2 calling read')
    read1()

def change():
    global money
    money=0

