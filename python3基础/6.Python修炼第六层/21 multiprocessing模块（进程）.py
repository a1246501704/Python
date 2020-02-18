\子进程和父进程变量共享
# 主进程中声明一个变量为共享变量。
# 例如
    # 主进程中声明的共享变量array作为实参传到子进程process_handle(arg)，arg作为形参，接受array的值。
    # 如果在子进程中改变arg的值，父进程中array的值也会随之改变。

import multiprocessing
from multiprocessing import Process
 
def process_handle(arg):
    arg.extend([1,2,3,4]) # 往空列表中加值
    print(arg)
 
def main():
    array = multiprocessing.Manager().list()  # 一个类的空列表
    handle_process = Process(target=process_handle, args=(array,))
    handle_process.start()
    handle_process.join()
    array.extend([5,6,7]) # 往空列表中加值
    print(array)

if __name__ == "__main__":
    main()

# 这段代码父进程的array和子进程的arg（列表）是共享变量。
# 子进程中为arg追加[1,2,3,4]，输出arg为[1,2,3,4]。
# 父进程中为array追加[5,6,7]，输出array为[1,2,3,4,5,6,7]。
# 运行结果如下
'''
[1, 2, 3, 4]
[1, 2, 3, 4, 5, 6, 7]
'''