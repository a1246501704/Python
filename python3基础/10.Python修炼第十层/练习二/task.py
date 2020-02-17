from threading import Thread
msg_l=[]
format_l=[]
def talk():
    while True:
        msg=input('>>: ').strip()
        if not msg:continue
        msg_l.append(msg)

def format_msg():
    while True:
        if msg_l:
            res=msg_l.pop()
            format_l.append(res.upper())

def save():
    while True:
        if format_l:
            with open('db.txt','a',encoding='utf-8') as f:
                res=format_l.pop()
                f.write('%s\n' %res)

if __name__ == '__main__':
    t1=Thread(target=talk)
    t2=Thread(target=format_msg)
    t3=Thread(target=save)
    t1.start()
    t2.start()
    t3.start()