\想从一个按照从小到大排列的数字列表中找到指定的数字，遍历的效率太低，用二分法（算法的一种，算法是解决问题的方法）可以极大缩小问题规模.

# 用二分法实现类似in的效果
l=[1,2,10,30,33,99,101,200,301,402] #从小到大排列的数字列表,如果不是从小到大排序的可以先用sorted()排序。

# 用for循环遍历，需要一个一个匹配。运气好第一个值就找到了，运气不好可能遍历到最后一个值才能匹配到。效率低。
num=200
for item in l:
    if num == item:
        print('find it')
        break

# 用二分法，将列表一分为二后判断是在左边还是右边，再进行判断
def get(num,l):
    print(l)
    if len(l) > 0:         # 列表不为空，则证明还有值是可以执行二分法逻辑的
        mid=len(l)//2
        if num > l[mid]:   # 判断num如果在右边，mid当索引使用
            l=l[mid+1:]    # 将列表一切为二，+1是为了不算mid这个值。因为mid这个值已经比较过了。
        elif num < l[mid]: # 判断num如果在左边
            l=l[:mid]      # 每次切完重新赋值给l
        else:
            print('find it')
            return   # 找到后结束
        get(num,l)   # 没有找到继续递归查找，将if和elif中都要执行的get提出来写一份。避免重复代码
    else: #列表为空，则证明根本不存在要查找的值
        print('not exists')
        return
get(200,l)
'''
[1, 2, 10, 30, 33, 99, 101, 200, 301, 402]
[101, 200, 301, 402]
[101, 200]
find it
'''

# 实现类似于l.index(30)的效果，输出值的索引。
l=[1,2,10,30,33,99,101,200,301,402]

def search(num,l,start=0,stop=len(l)-1):
    if start <= stop:
        mid=start+(stop-start)//2
        print('start:[%s] stop:[%s] mid:[%s] mid_val:[%s]' %(start,stop,mid,l[mid]))
        if num > l[mid]:
            start=mid+1
        elif num < l[mid]:
            stop=mid-1
        else:
            print('find it',mid)
            return
        search(num,l,start,stop)
    else: #如果stop > start则意味着列表实际上已经全部切完，即切为空
        print('not exists')
        return

search(301,l)
'''
start:[0] stop:[9] mid:[4] mid_val:[33]
start:[5] stop:[9] mid:[7] mid_val:[200]
start:[8] stop:[9] mid:[8] mid_val:[301]
find it 8
'''