\#基于用户名密码连接，远程执行命令


# 123.56.157.199:22022
# root
# HLH199300.

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='123.56.157.199', port=22022, username='root', password='HLH199300.')

# 执行命令

while True:
    cmd=input('>>: ').strip()
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # 获取命令结果
    result = stdout.read()
    print(result.decode('utf-8'))
    # 关闭连接
ssh.close()


\#基于密钥登录
import paramiko

private_key = paramiko.RSAKey.from_private_key_file(r'C:\\id_rsa')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='123.56.157.199', port=22022, username='root', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
result = stdout.read()
print(result.decode('utf-8'))
# 关闭连接
ssh.close()


\#上传下载
import paramiko

transport = paramiko.Transport(('123.56.157.199', 22022))
transport.connect(username='root', password='HLH199300.')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put(r'C:\\id_rsa', '/tmp/test.rsa')
# sftp.get('remove_path', 'local_path') # 将remove_path 下载到本地 local_path

transport.close()




