class Dog:
    counter = []
    def __init__(self,name,type):
        self.name = name
        self.dog_type = type
        self.life_value = 2000
        # Dog.counter += 1

史努比 = Dog('史努比','大白狗')
史努比.counter.append(1)
史努比2 = Dog('史努比','大白狗')
史努比2.counter.append(1) 
print(史努比.counter)
print(史努比2.counter)


#对于任何数据类型的静态属性：他的修改操作尽量用类名
#尤其是对于不可变数据类型：修改必须用类名