struct是python(包括版本2和3)中的内建模块，它用来在c语言中的结构体与python中的字符串之间进行转换，数据一般来自文件或者网络。

\struct模块中的函数
函数	                            return	 explain
pack(fmt,v1,v2…)	                string	按照给定的格式(fmt),把数据转换成字符串(字节流),并将该字符串返回.
pack_into(fmt,buffer,offset,v1,v2…)	None	按照给定的格式(fmt),将数据转换成字符串(字节流),并将字节流写入以offset开始的buffer中.(buffer为可写的缓冲区,可用array模块)
unpack(fmt,v1,v2…..)	            tuple	按照给定的格式(fmt)解析字节流,并返回解析结果。
pack_from(fmt,buffer,offset)	    tuple	按照给定的格式(fmt)解析以offset开始的缓冲区,并返回解析结果
calcsize(fmt)	                  size of fmt	计算给定的格式(fmt)占用多少字节的内存，注意对齐方式

