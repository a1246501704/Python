

# 由于纯文本的邮件内容已经不能满足多样化的需求，主要介绍通过引入mail.mime的MIMEText 类来实现支持HTML格式的邮件，支持所有HTML格式的元素，包括表格，图片，动画，css样式，表单等。（参考刘老师文献）
# 案例中收集的是最简单的服务器硬件信息，通过smtp将信息发到收件人邮箱，大家可以根据自己的需求收集所需要的信息（比如CPU百分比，硬盘剩余百分比，内存使用百分比，并设定阈值，当硬盘剩余空间不足10%,发送邮件通知管理员及时处理）

\MIME类型解析：
MIME（Multipurpose Inrernet Mail Extension）多用途网络邮件扩展类型
可以被称为Media type 或者Content type;
它设定某种类型的文件当被浏览器打开的时候需要用什么样的应用程序，多用于HTTP通信和设定文档类型；
例如：HTML
服务器将此类型名放入传给浏览器的数据中以告诉浏览器用什么样的插件打开它；

\常见的MIME类型;
application:某种二进制附件，对于没有subtype的情况下，默认是application/octet-stream;
text:文本，理论上可读，对于没有subtype的情况下，默认是text/plain;
image:图像
audio:音频
video:视频
multipart:多部分文档文件（复合文档文件）

详细介绍：
application/octet-stream:未知应用程序文件
application/json:JSON数据
text/plain:未知的文本文件（纯文本文件），浏览器会认为这是可以直接显示的；
 

\浏览器分辨文件是基于MIME的，而不会把文件打开查看是否为其他类型的；
text/css:css文件
text/html：HTML文件
image/gif:gif文件
multipart/form-data:多用于表达提交，其中的multipart即多部分文档
其只支持post
当表单包含文件上传时，只能用multipart/form-data;

\下是常见的一些MIME的使用

.doc     application/msword
.docx   application/vnd.openxmlformats-officedocument.wordprocessingml.document
.rtf       application/rtf
.xls     application/vnd.ms-excel	 application/x-excel
.xlsx    application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
.ppt     application/vnd.ms-powerpoint
.pptx    application/vnd.openxmlformats-officedocument.presentationml.presentation
.pps     application/vnd.ms-powerpoint
.ppsx   application/vnd.openxmlformats-officedocument.presentationml.slideshow
.pdf     application/pdf
.swf    application/x-shockwave-flash
.dll      application/x-msdownload
.exe    application/octet-stream
.msi    application/octet-stream
.chm    application/octet-stream
.cab    application/octet-stream
.ocx    application/octet-stream
.rar     application/octet-stream
.tar     application/x-tar
.tgz    application/x-compressed
.zip    application/x-zip-compressed
.z       application/x-compress
.wav   audio/wav
.wma   audio/x-ms-wma
.wmv   video/x-ms-wmv
.mp3 .mp2 .mpe .mpeg .mpg     audio/mpeg
.rm     application/vnd.rn-realmedia
.mid .midi .rmi     audio/mid
.bmp     image/bmp
.gif     image/gif
.png    image/png
.tif .tiff    image/tiff
.jpe .jpeg .jpg     image/jpeg
.txt      text/plain
.xml     text/xml
.html     text/html
.css      text/css
.js        text/javascript
.mht .mhtml   message/rfc822

\一、smtplib模块：(负责发送邮件)
主要通过SMTP类与邮件系统进行交互。使用方法如下：
1.实例化一个SMTP对象：
　　s = smtplib.SMTP(邮件服务地址，端口号)
　　s = smtplib.SMTP_SSL(邮件服务地址，端口号)
2.登陆邮件，权限验证：
　　s.login(用户名，密码)
3.发送邮件：
　　s.sendmail(发件人邮箱，收件人邮箱，发送内容)
4.断开连接：
　　s.close()

\二、email模块：(负责构建邮件)
　　email模块：支持发送的邮件内容为纯文本、HTML内容、图片、附件。email模块中有几大类来针对不同的邮件内容形式，常用如下：
　　MIMEText：（MIME媒体类型）内容形式为纯文本、HTML页面。
　　MIMEImage：内容形式为图片。
　　MIMEMultupart：多形式组合，可包含文本和附件。

        每一类对应的导入方式：
        　　from email.mime.text import MIMEText
        　　from email.mime.image import MIMEImage
        　　from email.mime.multipart import MIMEMultipart
\三、MIMEText:
　　MIMEText(msg,type,chartset)
　　    msg：邮件内容
　　    type：文本类型默认为plain（纯文本）,发送HTML格式的时候，修改为html，但同时要求msg的内容也是html的格式。
　　    chartset：文本编码，中文为“utf-8”
　　# 构造TEXT格式的消息
　　msg = MIMEText("hello.text","plain","utf-8")
　　msg["Subject"] = "xxxxx"
　　msg["From"] = "xxxx"
　　msg["To"] = "xxxx"
　　#发送以上构造的邮件内容要使用as_string将构造的邮件内容转换为string形式。
　　s.sendmail("xxx","xxx",msg.as_string)

\四、MIMEImage、MIMEMultipart：
　　msg = MIMEMultipart()
　　#实例化一个文本对象 
　　msg_sub = MIMEText("hello.text","plain","utf-8")
　　#将text消息添加到MIMEMultipart中，作为邮件正文。
　　msg.attach(msg_sub)
　　#图片作为附件
　　import os
　　img_datas = open(os.getcwd()+ "/reports/xxxx.png","rb").read()
　　msg_img = MIMEImage(img_data)
　　msg_img.add_header('Content-Disposition','attachment', filename = "xxxx.png" )
　　msg_img.add_header('Content-ID','<0>')
　　#将图片添加到MIMEMultiplart中，作为附件发送。
　　msg.attach(mag_img)

\用例
#!/usr/bin/env python
#coding: utf-8

import smtplib
import os
import psutil
from email.mime.text import MIMEText    # 导入MIMEText类

ip = os.popen("ifconfig |grep -v 127 |grep inet |awk '{print $2}'|cut -d: -f2").read().strip()     # 获取IP地址
hostname  = os.popen("hostname").read().strip()   # 获取主机名
cpu = psutil.cpu_count()  # 获取CPU线程
mem = os.popen("free -m |grep Mem |awk '{print $2}'").read().strip()+"M"  # 获取内存总量
disk = os.popen("fdisk -l |grep -E Disk |awk '{print $3}'").read().strip()+"G" # 获取硬盘总大小
HOST = "smtp.163.com"      # 指定使用网易163邮箱
SUBJECT = u"服务器硬件信息"   # 邮件标题
TO = "1351271xxxx@139.com"   # 收件人
FROM = "sallsoul@163.com"    # 发件人
msg = MIMEText("""
                <table color="CCCC33" width="800" border="1" cellspacing="0" cellpadding="5" text-align="center">
                        <tr>
                                <td text-align="center">name</td>
                                <td text-align="center">network</td>
                                <td>CPU</td>
                                <td>Mem</td>
                                <td>Disk</td>
                        </tr>   
                        <tr>   
                                <td text-align="center">%s </td>
                                <td>%s </td>
                                <td>%s </td>
                                <td>%s </td>
                                <td>%s </td>
                        </tr>
                </table>""" % (hostname,ip,cpu,mem,disk),"HTML","uft-8")
msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
try:
        server  = smtplib.SMTP()      # 创建一个SMTP对象
        server.connect(HOST,"25")     # 通过connect方法链接到smtp主机
        server.starttls()             # 启动安全传输模式
        server.login("sallsoul@163.com","passwordxx") # 登录163邮箱 校验用户，密码
        server.sendmail(FROM, [TO], msg.as_string())  # 发送邮件  
        server.quit()
        print "邮件发送成功 %s %s %s %s %s" % (hostname,ip,cpu,mem,disk)  # 发送成功并打印
except Exception, e:
        print "邮件发送失败："+str(e)


