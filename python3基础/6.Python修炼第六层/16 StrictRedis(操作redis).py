Python操作Redis数据库

\连接数据库
1\StrictRedis
from redis import StrictRedis

# 使用默认方式连接到数据库
redis = StrictRedis(host='localhost', port=6379, db=0)

# 使用url方式连接到数据库
redis = StrictRedis.from_url('redis://@localhost:6379/1')

2\ConnectionPool
from redis import StrictRedis,ConnectionPool

# 使用默认方式连接到数据库
pool = ConnectionPool(host='localhost', port=6379, db=0)
redis = StrictRedis(connection_pool=pool)

# 使用url方式连接到数据库
pool = ConnectionPool.from_url('redis://@localhost:6379/1')
redis = StrictRedis(connection_pool=pool)

# 构造url方式连接到数据库，有以下三种模式: 
redis://[:password]@host:port/db    # TCP连接
rediss://[:password]@host:port/db   # Redis TCP+SSL 连接
unix://[:password]@/path/to/socket.sock?db=db    # Redis Unix Socket 连接

\String操作
    方法	                            作用	                                    示例	                                  示例结果
set(name, value)	            给name赋值为value	                       redis.set('name', 'Bob')	                           True
get(name)	                    返回数据库中key为name的string的value	     redis.get('name')	                                 b'Bob'
getset(name, value)	            给数据库中key为name的string赋予值value并返回上次的value	redis.getset('name', 'Mike')	           b'Bob'
mget(keys, *args)	            返回多个key对应的value	                    redis.mget(['name', 'nickname'])	                [b'Mike', b'Miker']
setnx(name, value)	            如果key不存在才设置value	                 redis.setnx('newname', 'James')	                 第一次运行True，第二次False
setex(name, time, value)	    设置可以对应的值为string类型的value，并指定此键值对应的有效期	redis.setex('name', 1, 'James')	       True
setrange(name, offset, value)	设置指定key的value值的子字符串	             redis.set('name', 'Hello') redis.setrange('name', 6, 'World')	11，修改后的字符串长度
mset(mapping)	                批量赋值	                               redis.mset({'name1': 'Durant', 'name2': 'James'})	True
msetnx(mapping)	                key均不存在时才批量赋值	                     redis.msetnx({'name3': 'Smith', 'name4': 'Curry'})	  True
incr(name, amount=1)	        key为name的value增值操作，默认1，key不存在则被创建并设为amount	redis.incr('age', 1)	              1，即修改后的值
decr(name, amount=1)	        key为name的value减值操作，默认1，key不存在则被创建并设置为-amount	redis.decr('age', 1)	          -1，即修改后的值
append(key, value)	            key为name的string的值附加value	            redis.append('nickname', 'OK')	                     13，即修改后的字符串长度
substr(name, start, end=-1)	    返回key为name的string的value的子串	         redis.substr('name', 1, 4)	                          b'ello'
getrange(key, start, end)	    获取key的value值从start到end的子字符串	      redis.getrange('name', 1, 4)	                       b'ello'

# 源码
def set(self, name, value, ex=None, px=None, nx=False, xx=False):
        """
        Set the value at key ``name`` to ``value``
        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.
        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.
        ``nx`` if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.
        ``xx`` if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.
        """

# 中文翻译（我的理解）
ex：name的生存时间，单位秒，也就是ex= n n秒后name在内存中将不存在
px：生存时间，单位毫秒
nx：如果nx = True，当name不存在时，才会设置name-->value
xx：如果xx = True，当name已经存在时，才会设置name-->value




\Key操作
    方法	                作用	            示例	                            示例结果
exists(name)	    判断一个key是否存在	         redis.exists('name')	              True
delete(name)	    删除一个key	                redis.delete('name')	              1
type(name)	        判断key类型	                redis.type('name')	               b'string'
keys(pattern)	    获取所有符合规则的key	      redis.keys('n*')	                 [b'name']
randomkey()	        获取随机的一个key	         randomkey()	                     b'name'
rename(src, dst)	将key重命名	                redis.rename('name', 'nickname')	 True
dbsize()	        获取当前数据库中key的数目	  dbsize()	                            100
expire(name, time)	设定key的过期时间，单位秒	  redis.expire('name', 2)               True
ttl(name)	        获取key的过期时间，单位秒，-1为永久不过期	redis.ttl('name')	       -1
move(name, db)	    将key移动到其他数据库	      move('name', 2)	                   True
flushdb()	        删除当前选择数据库中的所有key  flushdb()	                         True
flushall()	        删除所有数据库中的所有key	  flushall()	                        True

\List操作
        方法	                        作用	                                                    示例	                  示例结果
rpush(name, *values)	    在key为name的list尾添加值为value的元素，可以传多个	                redis.rpush('list', 1, 2, 3)	 3，list大小
lpush(name, *values)	    在key为name的list头添加值为value的元素，可以传多个	                redis.lpush('list', 0)	         4，list大小
llen(name)	                返回key为name的list的长度	                                     redis.llen('list')	              4
lrange(name, start, end)    返回key为name的list中start至end之间的元素	                      redis.lrange('list', 1, 3)	   [b'3', b'2', b'1']
ltrim(name, start, end)	    截取key为name的list，保留索引为start到end的内容	                   ltrim('list', 1, 3)	            True
lindex(name, index)	        返回key为name的list中index位置的元素	                          redis.lindex('list', 1)	       b'2'
lset(name, index, value)    给key为name的list中index位置的元素赋值，越界则报错	                redis.lset('list', 1, 5)	     True
lrem(name, count, value)    删除count个key的list中值为value的元素	                          redis.lrem('list', 2, 3)	       1，即删除的个数
lpop(name)	                返回并删除key为name的list中的首元素	                               redis.lpop('list')	            b'5'
rpop(name)	                返回并删除key为name的list中的尾元素	                               redis.rpop('list')	            b'2'
blpop(keys, timeout=0)	    返回并删除名称为在keys中的list中的首元素，如果list为空，则会一直阻塞等待 redis.blpop('list')	          [b'5']
brpop(keys, timeout=0)	    返回并删除key为name的list中的尾元素，如果list为空，则会一直阻塞等待	    redis.brpop('list')	             [b'2']
rpoplpush(src, dst)	        返回并删除名称为src的list的尾元素，并将该元素添加到名称为dst的list的头部 redis.rpoplpush('list', 'list2')  b'2'

\Set操作
        方法	                            作用	                            示例	                                            示例结果
sadd(name, *values)	            向key为name的set中添加元素	                  redis.sadd('tags', 'Book', 'Tea', 'Coffee')	    3，即插入的数据个数
srem(name, *values)	            从key为name的set中删除元素	                  redis.srem('tags', 'Book')	                    1，即删除的数据个数
spop(name)	                    随机返回并删除key为name的set中一个元素	        redis.spop('tags')	                                    b'Tea'
smove(src, dst, value)	        从src对应的set中移除元素并添加到dst对应的set中	 redis.smove('tags', 'tags2', 'Coffee')	                  True
scard(name)	                    返回key为name的set的元素个数	              redis.scard('tags')	                                     3
sismember(name, value)	        测试member是否是key为name的set的元素	       redis.sismember('tags', 'Book')	                        True
sinter(keys, *args)	            返回所有给定key的set的交集	                   redis.sinter(['tags', 'tags2'])	                    {b'Coffee'}
sinterstore(dest, keys, *args)	求交集并将交集保存到dest的集合	                redis.sinterstore('inttag', ['tags', 'tags2'])	          1
sunion(keys, *args)	            返回所有给定key的set的并集	                   redis.sunion(['tags', 'tags2'])	                {b'Coffee', b'Book', b'Pen'}
sunionstore(dest, keys, *args)	求并集并将并集保存到dest的集合	                redis.sunionstore('inttag', ['tags', 'tags2'])	          3
sdiff(keys, *args)	            返回所有给定key的set的差集	                   redis.sdiff(['tags', 'tags2'])	                    {b'Book', b'Pen'}
sdiffstore(dest, keys, *args)	求差集并将差集保存到dest的集合	                redis.sdiffstore('inttag', ['tags', 'tags2'])	          3
smembers(name)	                返回key为name的set的所有元素	               redis.smembers('tags')	                        {b'Pen', b'Book', b'Coffee'}
srandmember(name)	            随机返回key为name的set的一个元素，但不删除元素	  redis.srandmember('tags')	

\Sorted Set操作
            方法	                                                                            作用	                                                                                            示例	                            示例结果
zadd(name, args, *kwargs)	                                            向key为name的zset中添加元素member，score用于排序。如果该元素存在，则更新其顺序	                                   redis.zadd('grade', 100, 'Bob', 98, 'Mike')	      2，即添加的元素个数
zrem(name, *values)	                                                    删除key为name的zset中的元素	                                                                                redis.zrem('grade', 'Mike')	                       1，即删除的元素个数
zincrby(name, value, amount=1)	                                        如果在key为name的zset中已经存在元素value，则该元素的score增加amount，否则向该集合中添加该元素，其score的值为amount	  redis.zincrby('grade', 'Bob', -2)	                 98.0，即修改后的值
zrank(name, value)	                                                    返回key为name的zset中元素的排名（按score从小到大排序）即下标	                                                 redis.zrank('grade', 'Amy')	                         1
zrevrank(name, value)	                                                返回key为name的zset中元素的倒数排名（按score从大到小排序）即下标	                                              redis.zrevrank('grade', 'Amy')	                      2
zrevrange(name, start, end, withscores=False)	                        返回key为name的zset（按score从大到小排序）中的index从start到end的所有元素	                                     redis.zrevrange('grade', 0, 3)	                [b'Bob', b'Mike', b'Amy', b'James']
zrangebyscore(name, min, max, start=None, num=None, withscores=False)	返回key为name的zset中score在给定区间的元素	                                                                  redis.zrangebyscore('grade', 80, 95)	            [b'Amy', b'James']
zcount(name, min, max)	                                                返回key为name的zset中score在给定区间的数量	                                                                  redis.zcount('grade', 80, 95)	                          2
zcard(name)	                                                            返回key为name的zset的元素个数	                                                                             redis.zcard('grade')	                                 3
zremrangebyrank(name, min, max)	                                        删除key为name的zset中排名在给定区间的元素	                                                                   redis.zremrangebyrank('grade', 0, 0)	             1，即删除的元素个数
zremrangebyscore(name, min, max)                                        删除key为name的zset中score在给定区间的元素	                                                                  redis.zremrangebyscore('grade', 80, 90)	        1，即删除的元素个数

\Hash操作
            方法	                    作用	                                        示例	                                  示例结果
hset(name, key, value)	        向key为name的hash中添加映射	                     hset('price', 'cake', 5)	                   1，即添加的映射个数
hsetnx(name, key, value)	    向key为name的hash中添加映射，如果映射键名不存在	    hsetnx('price', 'book', 6)	                  1，即添加的映射个数
hget(name, key)	                返回key为name的hash中field对应的value	         redis.hget('price', 'cake')	                     5
hmget(name, keys, *args)	    返回key为name的hash中各个键对应的value	          redis.hmget('price', ['apple', 'orange'])	     [b'3', b'7']
hmset(name, mapping)	        向key为name的hash中批量添加映射	                  redis.hmset('price', {'banana': 2, 'pear': 6})	True
hincrby(name, key, amount=1)	将key为name的hash中映射的value增加amount	     redis.hincrby('price', 'apple', 3)	            6，修改后的值
hexists(name, key)	            key为namehash中是否存在键名为key的映射	          redis.hexists('price', 'banana')	                 True
hdel(name, *keys)	            key为namehash中删除键名为key的映射	             redis.hdel('price', 'banana')	                     True
hlen(name)	                    从key为name的hash中获取映射个数	                 redis.hlen('price')	                               6
hkeys(name)	                    从key为name的hash中获取所有映射键名	              redis.hkeys('price')	                    [b'cake', b'book', b'banana', b'pear']
hvals(name)	                    从key为name的hash中获取所有映射键值	              redis.hvals('price')	                    [b'5', b'6', b'2', b'6']
hgetall(name)	                从key为name的hash中获取所有映射键值对	           redis.hgetall('price')	       {b'cake': b'5', b'book': b'6', b'orange': b'7', b'pear': b'6'}

\RedisDump
# redis-load
#将数据导入到数据库中
redis-load -h   # 获取帮助信息
< redis_data.json redis-load -u redis://@localhost:6379  # 将json数据导入数据库中

#redis-dump
#将数据库信息导出
redis-dump -h  # 获取帮助信息
redis-dump -u redis://@localhost:6379 -d 1 > ./redis.data.jl  # 导出到json文件
redis-dump -u redis://@localhost:6379 -f adsl:* > ./redis.data.jl  # 导出adsl开头的数据



redis学习 （key）键，Python操作redis 键 （二） http://www.cnblogs.com/xuchunlin/p/7061524.html
Python操作redis字符串(String)详解 (三) http://www.cnblogs.com/xuchunlin/p/7062065.html
Python操作redis系列以 哈希(Hash)命令详解（四） http://www.cnblogs.com/xuchunlin/p/7064860.html
Python操作redis系列之 列表（list） (五) http://www.cnblogs.com/xuchunlin/p/7067154.html
Python操作redis学习系列之（集合）set，redis set详解 （六）http://www.cnblogs.com/xuchunlin/p/7070267.html
python 操作redis之——有序集合(sorted set) （七） http://www.cnblogs.com/xuchunlin/p/7097272.html
Python学习记录 ——redis  https://blog.csdn.net/tony10010/article/details/84270700
Redis数据库迁移-python实现 https://blog.csdn.net/q1694222672/article/details/82734221
Python进行Redis数据迁移   http://www.manongjc.com/detail/9-ezbzzydchyulskl.html
使用python来操作redis用法详解 https://www.jianshu.com/p/2639549bedc8