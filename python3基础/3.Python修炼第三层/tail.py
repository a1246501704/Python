import time
with open('access.log','rb') as f:
    f.seek(0,2)   # 光标移动到文件最后
    while True:
        line=f.readline() # 从光标处开始读，readline每读一行光标会移动一行。
        if line:
            print(line.decode('utf-8'),end='')
        else:
           time.sleep(0.2)  # 等待的过程中文件中会有新的内容写入


#以a的模式打开文件，追加内容，测试上面的功能是否实现。
with open('access.log','a',encoding='utf-8') as f:
    f.write('11111\n')