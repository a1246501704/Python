import os

res=os.system('dir')
print('命令的结果',res)


import subprocess

obj=subprocess.Popen('dir',shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)



stdout_res1=obj.stdout.read()
print(stdout_res1.decode('gbk'))

stdout_res2=obj.stdout.read() #在第一次读时，管道就空了
print('========>',stdout_res2.decode('gbk'))




import subprocess

obj=subprocess.Popen('diasdfasdfasr',shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)

stdout_res1=obj.stdout.read() #命令执行错误会把结果送到stderr管道
print(stdout_res1.decode('gbk'))

stdout_res2=obj.stderr.read() #命令执行错误会把结果送到stderr管道
print(stdout_res2.decode('gbk'))





#ls ; pwasdfasdfd; echo 123
#ls && pwd && echo 123


#执行命令
import subprocess

obj=subprocess.Popen('tasklist | findstr pycharm',shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)

print(obj.stdout.read().decode('gbk'))




import subprocess
obj1=subprocess.Popen('tasklist',shell=True,
                 stdout=subprocess.PIPE,)

obj2=subprocess.Popen('findstr pycharm',shell=True,
                     stdin=obj1.stdout,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)

print(obj2.stdout.read().decode('gbk'))