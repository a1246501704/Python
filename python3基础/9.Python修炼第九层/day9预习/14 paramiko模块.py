# import paramiko
#
# # 创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname='120.92.84.249', port=22, username='root', password='123QWEasd')
#
# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('df')
# # 获取命令结果
# result = stdout.read()
# print(result.decode('utf-8'))
# # 关闭连接
# ssh.close()


# import paramiko
#
# private_key = paramiko.RSAKey.from_private_key_file('id_rsa')
#
# # 创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname='120.92.84.249', port=22, username='root', pkey=private_key)
#
# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('df')
# # 获取命令结果
# result = stdout.read()
# print(result.decode('utf-8'))
# # 关闭连接
# ssh.close()


import paramiko

transport = paramiko.Transport(('120.92.84.249', 22))
transport.connect(username='root', password='123QWEasd')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('id_rsa', '/tmp/test.rsa')
# 将remove_path 下载到本地 local_path
# sftp.get('remove_path', 'local_path')

transport.close()