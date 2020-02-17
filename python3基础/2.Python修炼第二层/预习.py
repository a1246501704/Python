#
# for i,v in enumerate(range(2,10)):
#     print(i,v)
#
# shopping 购物车
# product_list = [
#     ['Iphone7',6500],
#     ['MacBook',12000],
#     ['Python Book',99],
#     ['Coffee',31],
#     ['Bike',999],
# ]
# shopping_cart = []
# salary = int(input("input your salary:")) #输入金额
# while True:
#     for index,i in enumerate(product_list): #循环商品列表
#         print("%s.\t%s\t%s" %(index,i[0],i[1])) #打印商品列表
#
#     choice = input(">>: ").strip() #输入商品序列号，选着商品  #.strip()去掉空格
#     if len(choice) == 0:  #判断输入字符串是否为空和字符串长度
#         print('-->您没有选择商品<--')
#         continue
#     if choice.isdigit():  #判断choice是不是一个数字
#         choice = int(choice) #把输入的字符串转成整数
#         if choice < len(product_list) and choice >=0: #输入的整数必须小于商品列表的数量
#             product_item = product_list[choice] #获取商品
#             if salary >= product_item[1]: #拿现有金额跟商品对比，是否买得起
#                 salary -= product_item[1] #扣完商品的价格
#                 shopping_cart.append(product_item) #把选着的商品加入购物车
#                 print("添加 \033[32;1m%s\033[0m 到购物车,您目前的金额是 \
# \033[31;1m%s\033[0m" %(product_item[0],salary))
#             else:
#                 print("对不起，您的金额不足,还差",product_item[1]-salary)
#         else:
#             print("-->没有此商品<--")
#     elif choice == "exit":
#         total_cost = 0
#         print("您的购物车列表")
#         for i in shopping_cart:
#             print(i)
#             total_cost+=i[1]
#         print("您的购物车总价是:",total_cost)
#         print("您目前的余额是",salary)
#         break
#
# product_list = [
#     ['Iphone7',6500],
#     ['MacBook', 12000],
#     ['Python Book', 99],
#     ['Coffee', 31],
#     ['Bike', 999],
# ]
# shopping_cart = []
# salary = int(input('请输入您的金额： '))
#
# while True:
#     for index,i in enumerate(product_list):
#         print("%s.\t%s\t%s" %(index,i[0],i[1]))
#     choice = input(">>: ").strip()
#     if len(choice) == 0:
#         print('您还没有选择商品')
#         continue
#     if choice.isdigit():
#         choice = int(choice)
#         if choice < len(product_list) and choice >=0:
#             product_itme = product_list[choice]
#             if salary >= product_itme[1]:
#                 salary -= product_itme[1]
#                 shopping_cart.append(product_itme)
#                 print("添加 %s 到购物车，您目前的金额是 %s" %(product_itme[0],salary))
#             else:
#                 print('对不起，您的金额不足，还差',product_itme[1]-salary)
#         else:
#             print('没有此商品')
#     elif choice == 'exit':
#         total_cost = 0
#         print('您的购物车列表')
#         for i in shopping_cart:
#             print(i)
#             total_cost+=i[1]
#         print("您的购物车总价是：",total_cost)
#         print("您目前的余额是：",salary)
#         break
#
#
# 元组
# 元组其实跟列表差不多，也是存一组数，只不过它一旦创建，便不能修改，所以又叫只读列表
# name=("alex","jack","eric")
# 它只有2个方法，一个是count，一个是index，完毕
#
# # 字符串操作
# name = 'Alex Li ehgiish hahae'
# print(name.capitalize()) # 首字母大写
# print(name.casefold()) #大写全部改小写
# print(name.center(30,'-')) #指定宽度，然后在宽度之内对象居中，左右两侧填充字符
# print(name.count("e",0,5)) #统计字符出现次数，可以指定范围
# print(name.endswith("ae")) #以什么结束，打印布尔值 真或假
# # name = "alex\tli"
# # print(name)
# # print(name.expandtabs(20)) #指定 \t 的距离
# print(name.find('Li'))  #find 查找  找到了返回位置
# print(name.find('Lid')) #查不到
# msg = "my name is {0} , and i am {1} years old"
# msg2 = "my name is {name} , and i am {age} years old"
# print(msg.format("Alex",22))
# print(msg2.format(age=22,name="jack")) # format 格式化输出 对应字符串里面的{}
#
# print(msg.isalpha())  #是否是字母
# print("ab".isalpha())  #是否是字母
# print("a3b".isalnum()) #是不是阿拉伯数字和字母
#
# print("2".isdecimal()) # 整数
# print("0".isdigit()) #只能是正整数
# print("al_ex".isidentifier()) #是不是一个合法的变量名
# print("al_ex".islower()) #
# print("al_ex".isupper()) #
# print("3.1".isnumeric()) #
#
# print(float("3.1")) #
# print("3.1".isprintable()) #可否打印
# print("My Name Is Alex".istitle()) #首字母大写
# print("，".join("alex")) #循环字符串 指定添加字符
# print("|".join(["alex","jack",'rain'])) #列表转换字符串
# print("alex".ljust(50,'-')) #指定宽度和字符，在右边添加
# print("alex".rjust(50,'-')) #指定宽度和字符，在左边添加
# print("Alex".lower()) #大写改小写
# # print("   Alex   \n".strip()) #去掉空格
# # print("   Alex   \n".lstrip()) #去掉左边空格
# # print("   Alex   \n".rstrip()) #去掉右边空格
#
# # #简单的加密  把from_str和to_str 绑定 然后根据字符串输出
# # from_str = "!@#$%^&"
# # to_str = "abcdefg"
# # trans_table =str.maketrans(to_str,from_str)
# # print("alex".translate(trans_table))
#
# print("alex li".partition("x"))  #根据partition分隔
# print("alex li".replace("l","L",1))  #替换 可以指定次数
# print("alex\n l\ni".splitlines()) #根据\n 分成不同元素
# print("alex li".split("l")) #默认就是\n 来切分
# print("alex li".zfill(40)) # 基本用不到




# # 字典操作
# #dict
#
# names = {
#     "stu1101":{"name":"Alex","age":22,"hobbie":"girl"},
#     "stu1102":"Jack",
#     "stu1103":"rain",
# }
#
# # search
# print(names["stu1101"]["hobbie"]) #取值
# # print("stu1101" in names)  #判断
# print(names.get("stu1101","abc")) #get获取
# print(names.get("stu1104","abc")) #get获取
#
# #add
# names["stu1104"] = ["yangjian",31,"DBA"]  #增加 key=value
# print(names)
#
# #update
# names["stu1104"][0] = "杨剑"  #修改 指定key里面value的位置
# print(names)
#
# #delete
# print(names.pop("stu1102")) #删除一个key 并且返回删除key的 value
# print(names.pop("stu1105","ssss")) #指定删除 不会报错 返回这个value没找到
# del names["stu1103"] #删除key
# print(names)

# names.clear() #清空
#
# names = ["jack","alex","eric"]
# print(dict.fromkeys(names,0))   #把列表的值取出 当做字典的key 自定义value
#
# n3 = dict.fromkeys(names,[1,2,3])
# n3 = dict.fromkeys(names,'jd')
# n3["jack"][1] = 9    #修改列表，全部修改
# n3["jack"]= 9    #重新赋值，修改单独key
# print(n3)
# print(id(n3["jack"]),id(n3["eric"]))
#
# print(names)
# print(names.items()) #把字典转换成一个 大的列表，列表里每个元素变成元组
#
# for key in names: #效率高
#     print(key,names[key])
#
# for k,v in names.items(): #效率低
#     print(k,v)
#
# print(names.keys())  #取所有key
# print(names.values())  #取所有value
# names.popitem() #随机删除
# print(names)
#
# print(names.setdefault("stu1106","Racheal")) #如果不存在就添加，存在就打印
# print(names)
#
#
# print(names)
# d1 = {"stu1102":"JACK",1:333,2:444}
# names.update(d1) #合并两个字典,无序
# print(names)
#
#
#
# 字典是无序的，列表是有序的
# 因为字典不需要维护索引表，所以无序
# 字典无序，取值只能通过key
# 字典比列表速度快很多
# 字典的key，永远都是唯一的，是通过hash 散列 通过一定的数学算法，使字符串对应生成一个唯一的数字队里
# hash("abc")
# 找key的时候 是把要找的key转成hash 再去hash表里找
#
# key与key之间没有任何关系
#
# hash 散列
# 	[1212,232,434,5656,34331]
# 	[232,434,555,666,777,888,1212,5656,34331]
# 	"alex" in ["alex","jack","rain"]
#
# 	多少数据 就是 2的多少次方
# 	42亿数据 查32次最多就能肯定查到
#
# 列表之所以比字典慢 是因为要把无序的数据先排序 而字典 的hash表已经是排序好了的
#
# 总结字典：无序、key天生去重、查询效率高
#
#
#
# 深浅copy
#
# 第一层的数据独立，后面的数据共享
#
# names = {
#     "stu1101":{"name":"Alex","age":22,"hobbie":"girl"},
#     "stu1102":"Jack",
#     "stu1103":"rain",
# }
# n2 = names.copy()
# names["stu1103"] = "RAIN"
# names["stu1101"]["age"] = 24
# print(names)
# print(n2)
#
#
# import copy
# credit_card = {"name":"YangJian","acc":{"id":23333,"balance":900}}
# credit_card2 = credit_card.copy()  #shallow  浅copy
# credit_card3 = copy.deepcopy(credit_card)  #深copy 不常用，完全复制出一块内存空间
# credit_card2["name"] = "YangJianXifu"
#
# print(credit_card)
# print(credit_card2)
#
# credit_card["acc"]["balance"] -=300
# credit_card2["acc"]["balance"] -=500
# print(credit_card)
# print(credit_card2)
# print(credit_card3)



# #文件初识
#
# #file in 2.x only
# print(open("lyrics")) #打开文件对象 数据还没有加载到内存
# print(open("lyrics",encoding="utf-8").read()) #read 读文件
# data = open("lyrics",encoding="utf-8").read()
#
# #file mode r=read ,w=write , a=append
# #读模式打开就不能写，写模式打开就不能读
# #如果以写模式打开，是创建，如果有旧文件就会覆盖旧文件
#
# #先读 修改  再打开 写入
# f = open("lyric",mode="r",encoding="utf-8") # f 赋予一个变量,使用读模式
# data = f.read() #读到对象中
# data = data.replace("Somehow","ABCABCA") #修改好 存进去
# f.close() #关闭读模式
# f = open("lyric",mode="w",encoding="utf-8") #使用写模式
# f.write(data) #修改后 写入
# f.close() #关闭写模式
#
# #一行行的读我文件 一行行的写如新文件
# import os
# f = open("lyric",mode="r",encoding="utf-8") #读模式 老文件
#     # print(f.readline().strip()) #取一行 ，去掉换行符
#     # print(f.readline())  #取一行
# f_new = open("lyric_new",mode="w",encoding="utf-8") #写模式 新文件
# for line in f: #循环 老文件 一行一行查看
#     if "Somehow" in line: #判断要替换的字符串 是否在这一行
#         line = line.replace("Somehow","HHAAAA") #修改数据
#     f_new.write(line) #把修改的数据 写入新文件
# f.close() #关闭老文件
# f_new.close() #关闭新文件
# os.remove("lyric") #删除老文件
# os.rename("lyric_new","lyric") #新文件覆盖到老文件
#




