import sys,os
# os.path.abspath(__file__) #当前文件的绝对路劲
# os.path.dirname(os.path.abspath(__file__)) #获取上一成目录的路径
BASR_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #
sys.path.append(BASR_DIR)

from core import src

if __name__ == '__main__':
    src.run()

