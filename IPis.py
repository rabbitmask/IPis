#!/usr/bin/env python3
#_*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
                                                    
'''
import requests
import re
def ip_adr():
    headers = {'user-agent': 'ceshi/0.0.1'}
    print('本脚本为接口练习使用，\n请勿批量使用。\n退出请输入exit……')
    while True:
        try:
            target_ip = input('请输入目标域名/IP：')
            if target_ip=='exit':
                break
            r = requests.get('http://ip.tool.chinaz.com/{}'.format(target_ip),headers=headers)

            find_adr = re.compile(r'<span class="Whwtdhalf w50-0">.*</span>')
            find_ip = re.compile(r'<span class="Whwtdhalf w15-0">.*</span>')
            res1=find_adr.findall(r.text)
            res2=find_ip.findall(r.text)
            adr=re.findall(r'>.*<',str(res1[1]))
            adr=str(adr)[3:]
            adr=str(adr)[:-3]
            ip=re.findall(r'>.*<',str(res2[4]))
            ip=str(ip)[3:]
            ip=str(ip)[:-3]
            print('目标IP为：{}\n物理地址为：{}'.format(ip,adr))
        except:
            print('您的格式有误,大侠请重新来过~')

if "__main__" == __name__ :
    ip_adr()