from multiprocessing import Process
import time
class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print('task <%s> is runing' % self.name)
        time.sleep(2)
        print('task <%s> is done' % self.name)



if __name__ == '__main__':
    p=MyProcess('egon')
    p.start()

    print('主')