from multiprocessing import Process,Pool

# Pool进程的用法
# p.apply_async() #p.submit()
# p.apply() #p.submit().result()
pool = Pool()
futrues = []
for i in range(10):
    futrue = pool.apply_async(task, i)  # 异步的方式提交任务
    futrues.append(futrue)

pool.close()
pool.join()
for future in futrues:
    print(futrue.get())