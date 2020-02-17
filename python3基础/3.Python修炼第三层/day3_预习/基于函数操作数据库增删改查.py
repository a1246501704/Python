
# 基于函数操作数据库增删改查

# 函数：
# 1.代码重用
# 2.可扩展性
# 3.易维护

# 作业实现思路：
# sql=input('sql> ').strip()
# sql="select id,name from db1.emp where id>10 limit 3"

# 第一部分：sql_dic=sql解析(sql)
sql_dic={
    'select':["id,name"],
    'from':["db1.emp"],
    'where':["id>10"],
    'limit':["3"],
}

#第二部分：res=sql执行(sql_dic)

# 主函数
# 1. sql=input('sql> ').strip()
# 2. sql_dic=sql解析(sql)
# 3. res=sql执行(sql_dic)
# 4. 格式化输出res













