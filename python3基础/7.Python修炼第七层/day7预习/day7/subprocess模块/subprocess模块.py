import subprocess

#执行系统命令

# res=subprocess.Popen(r'deeddddir D:\04-视频录制存放目录\python18期\day7\xml模块',
#                      shell=True,
#                      stdout=subprocess.PIPE,
#                      stderr=subprocess.PIPE)
# # print('=================>',res)
# # print('-========>',res.stdout.read())
# print('-========>',res.stderr.read().decode('gbk'))
# print('-========>',res.stderr.read().decode('gbk'))
# print('-========>',res.stderr.read().decode('gbk'))
# print('-========>',res.stderr.read().decode('gbk'))


# stdin 输入
# stdut 标准正确输出
# stderr 错误输出
# PIPE 管道

#dir file_path | findstr xml$
res1=subprocess.Popen(r'dir D:\04-视频录制存放目录\python18期\day7\xml模块',
                     shell=True,
                     stdout=subprocess.PIPE,)

# stdin=res1.stout
res2=subprocess.Popen(r'findstr xml$',
                     shell=True,
                     stdin=res1.stdout,
                     stdout=subprocess.PIPE,)


print(res2.stdout.read().decode('gbk'))