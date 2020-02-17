#模块在第一次导入时才会执行，之后的导入都是直接引用内存已存在的结果
import sys
print(sys.modules)  #存放的是已经加载到内存的模块
print('spam' in sys.modules)

import spam
print('spam' in sys.modules)
# import spam
# import spam
# import spam
# import spam
# import spam


