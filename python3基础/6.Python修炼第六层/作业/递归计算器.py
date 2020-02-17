#!/usr/bin/env python
#_*_coding:utf-8

import re

def compute_multipy_divide(arg):
    value = arg[0]
    mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',value)
    if not mch:
        return
    content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',value).group()
    if len(content.split('*')) > 1:
        v1,v2 = content.split('*')
        get_value = float(v1) * float(v2)
    else:
        v1,v2 = content.split('/')
        get_value = float(v1) / float(v2)
    left,right = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',value,1)
    new_value = '%s%s%s' %(left,get_value,right)
    arg[0] = new_value
    compute_multipy_divide(arg)

def compute_add_substract(arg):
    while True:
        if '--' in arg[0] or '++' in arg[0] or '-+' in arg[0] or '+-' in arg[0]:
            arg[0] = arg[0].replace('--','+')
            arg[0] = arg[0].replace('++','+')
            arg[0] = arg[0].replace('-+','-')
            arg[0] = arg[0].replace('+-','-')
        else:
            break
    if arg[0].startswith('-'):
        arg[1] += 1
        arg[0] = arg[0].replace('-','&')
        arg[0] = arg[0].replace('+','-')
        arg[0] = arg[0].replace('&','+')
        arg[0] = arg[0][1:]
    value = arg[0]
    mch = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*',value)
    if not mch:
        return
    content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*',value).group()
    if len(content.split('+')) >1:
        v1,v2 = content.split('+')
        get_value = float(v1) + float(v2)
    else:
        v1,v2 = content.split('-')
        get_value = float(v1) - float(v2)
    left,right = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*',str(value),1)
    new_value = '%s%s%s' %(left,get_value,right)
    arg[0] = new_value
    compute_add_substract(arg)

def compute(expression):
    inp = [expression,0]
    compute_multipy_divide(inp)
    compute_add_substract(inp)
    count = divmod(inp[1],2)
    result = float(inp[0])
    if count[1] == 1:
        result = result * (-1)
    return result

def excute(expression):
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',expression):
        result = compute(expression)
        return result
    content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',expression).group()
    new_content = content[1:len(content)-1]
    new_list = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',expression,1)
    print('需要计算的公式：',expression)
    left = new_list[0]
    right = new_list[2]
    final = compute(new_content)
    print('提取目前优先级最高的公式进行计算：%s=%s' % (new_content, final))
    new_expression = '%s%s%s' %(left,final,right)
    print('计算一次之后的结果：', new_expression)
    print('上次计算公式结束'.center(30,'-'))
    return excute(new_expression)

def run():
    while True:
        str_input = input('输入您要计算的公式==>>: ').strip()
        if str_input == 'q': exit()
        if len(str_input) == 0 : continue
        if len(str_input) >0 :
            no_space_str = re.sub('\s*','',str_input)
        final = excute(no_space_str)
        print('您的计算结果是',final)

if __name__ == '__main__':
    run()