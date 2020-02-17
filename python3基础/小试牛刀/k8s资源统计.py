#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# @Author: fujianan 使用python3执行
import subprocess,os,sys
node_list_exec = '''kubectl get nodes | egrep -v 'SchedulingDisabled|NAME' | awk '{print $1}' '''
node_list=str(subprocess.check_output(node_list_exec,shell=True).strip(),encoding='utf8').split("\n")
content="""node  可用内存   限制内存  剩余内存  可运行java数量"""
num = 0
for node in node_list:
    desc_node_exec = """kubectl describe node %s |grep -A 5 "Allocated resources:"| grep "Mi"| awk '{print $7" "$8}' """ % node
    desc_node_res = str(subprocess.check_output(desc_node_exec,shell=True).strip(),encoding='utf8')
    no_mem_lim = int(desc_node_res.split(" ")[0].replace("Mi",""))
    no_mem_lim_per = int(desc_node_res.split(" ")[1].replace('(','').replace('%)',''))
    no_mem_ava = int(no_mem_lim / no_mem_lim_per * 100)
    no_mem_free = int(no_mem_ava - no_mem_lim)
    java_ava_cnt = int(no_mem_free / 2253 )
    #print(node,no_mem_ava,no_mem_lim,no_mem_free,java_ava_cnt)
    num = num + java_ava_cnt
    content += """
%s\t%sMi\t%sMi\t%sMi\t%s""" % (node,no_mem_ava,no_mem_lim,no_mem_free,java_ava_cnt)
content += "\njava_ava_total: %s" % num
print(content)


\修订1（过滤掉了打了污点的主机）
#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
# @Author: fujianan
import subprocess,os,sys
#node_list_exec = '''kubectl get nodes | egrep -v 'SchedulingDisabled|NAME' | awk '{print $1}' '''
node_list_exec = '''for i in `kubectl get nodes | egrep -v 'SchedulingDisabled|NAME' | awk '{print $1}'`;do for node in $i;do kubectl describe nodes $node| grep "Taints:             <none>" >> /dev/null;done;if [ $? -eq 0 ];then echo $node;fi;done '''
node_list=str(subprocess.check_output(node_list_exec,shell=True).strip(),encoding='utf8').split("\n")
content="""node  可用内存   限制内存  剩余内存  可运行java数量"""
num = 0
for node in node_list:
    desc_node_exec = """kubectl describe node %s |grep -A 5 "Allocated resources:"| grep "Mi"| awk '{print $7" "$8}' """ % node
    desc_node_res = str(subprocess.check_output(desc_node_exec,shell=True).strip(),encoding='utf8')
    no_mem_lim = int(desc_node_res.split(" ")[0].replace("Mi",""))
    no_mem_lim_per = int(desc_node_res.split(" ")[1].replace('(','').replace('%)',''))
    no_mem_ava = int(no_mem_lim / no_mem_lim_per * 100)
    no_mem_free = int(no_mem_ava - no_mem_lim)
    java_ava_cnt = int(no_mem_free / 2253 )
    #print(node,no_mem_ava,no_mem_lim,no_mem_free,java_ava_cnt)
    num = num + java_ava_cnt
    content += """
%s\t%sMi\t%sMi\t%sMi\t%s""" % (node,no_mem_ava,no_mem_lim,no_mem_free,java_ava_cnt)
content += "\njava_ava_total: %s" % num
print(content)