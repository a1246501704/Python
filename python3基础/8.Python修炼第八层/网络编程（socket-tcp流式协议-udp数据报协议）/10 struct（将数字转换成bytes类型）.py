import struct

res1=struct.pack('i',23322) # i代表打包后的结果是4个Bytes，打包的目标整型数字
print(res1)   # b'\x1a[\x00\x00'
print(len(res1)) # 4

res2=struct.unpack('i',res1)
print(res2)   # (23322,)
print(res2[0])# 23322

res3=struct.pack('q',23222222232222222222) # b'\x0e\xfa\x0b\xf3|\x80R\x00'
print(res3)  # 8
 

 
#制作报头
import json
header_dic={
    'filename':'a.txt',
    'total_size':123111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112312111111111,
    'md5':'xxxxxxxxx'
}
head_json=json.dumps(header_dic)
head_bytes=head_json.encode('utf-8')

print(head_bytes)
print(len(head_bytes))
