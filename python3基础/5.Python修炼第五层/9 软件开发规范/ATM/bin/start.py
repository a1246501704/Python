import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # abspath取文件绝对路径、dirname取文件上一级目录名
sys.path.append(BASE_DIR) # 将目录添加到环境变量搜索路径中

from core import src

if __name__ == '__main__':
    src.run()