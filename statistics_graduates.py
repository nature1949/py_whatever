#! /usr/bin/env python
#coding:utf-8

import csv
import re

import time
import requests
from lxml import etree

import json
#from jsonpath import jsonpath

#画图
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['simhei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


import matplotlib
import numpy as np
import pandas as pd

import plotly.graph_objects as go       #画瀑布图
'''
matplotlib.use('qt4agg') 
from matplotlib.font_manager import * 

#定义自定义字体，文件名从1.b查看系统中文字体中来 
myfont = FontProperties(fname='/home/wc/ttf/simsun.ttf') 
#解决负号'-'显示为方块的问题 
matplotlib.rcParams['axes.unicode_minus']=False  
'''
import sys
import importlib
importlib.reload(sys)
#sys.setdefaultencoding('utf8')

#import pandas as pd

def get_data(html, headers):
    html = requests.get(html,headers=headers)
    
    data = []
    etree_html = etree.HTML(html.text)
    ##  postgraduates
    postgraduates_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[6]/td[2]/text()')
    postgraduates_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[6]/td[3]/text()')
    postgraduates_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[6]/td[4]/text()')
    data.append((int(postgraduates_total[0]), int(postgraduates_male[0]), int(postgraduates_fomale[0])))
    
    ##  doctor
    doctor_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[7]/td[2]/text()')
    doctor_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[7]/td[3]/text()')
    doctor_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[7]/td[4]/text()')
    data.append((int(doctor_total[0]), int(doctor_male[0]), int(doctor_fomale[0])))
    
    ##  master
    master_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[8]/td[2]/text()')
    master_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[8]/td[3]/text()')
    master_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[8]/td[4]/text()')
    data.append((int(master_total[0]), int(master_male[0]), int(master_fomale[0])))
    
    ##  undergraduates
    undergraduates_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[9]/td[2]/text()')
    undergraduates_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[9]/td[3]/text()')
    undergraduates_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[9]/td[4]/text()')
    data.append((int(undergraduates_total[0]), int(undergraduates_male[0]), int(undergraduates_fomale[0])))
    
    ##  normal
    normal_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[10]/td[2]/text()')
    normal_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[10]/td[3]/text()')
    normal_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[10]/td[4]/text()')
    data.append((int(normal_total[0]), int(normal_male[0]), int(normal_fomale[0])))
    
    ##  short_cycle
    short_cycle_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[11]/td[2]/text()')
    short_cycle_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[11]/td[3]/text()')
    short_cycle_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[11]/td[4]/text()')
    data.append((int(short_cycle_total[0]), int(short_cycle_male[0]), int(short_cycle_fomale[0])))
    
#    for i in range(len(data)):
#        print(data[i])
    return data

def get_data_2014(html, headers):
    html = requests.get(html,headers=headers)
    
    data = []
    etree_html = etree.HTML(html.text)
    ##  postgraduates
    postgraduates_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[6]/td[2]/span/text()')
    postgraduates_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[6]/td[3]/span/text()')
    postgraduates_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[6]/td[4]/span/text()')
    data.append((int(postgraduates_total[0]), int(postgraduates_male[0]), int(postgraduates_fomale[0])))
    
    ##  doctor
    doctor_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[7]/td[2]/span/text()')
    doctor_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[7]/td[3]/span/text()')
    doctor_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[7]/td[4]/span/text()')
    data.append((int(doctor_total[0]), int(doctor_male[0]), int(doctor_fomale[0])))
    
    ##  master
    master_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[8]/td[2]/span/text()')
    master_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[8]/td[3]/span/text()')
    master_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[8]/td[4]/span/text()')
    data.append((int(master_total[0]), int(master_male[0]), int(master_fomale[0])))
    
    ##  undergraduates
    undergraduates_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[9]/td[2]/span/text()')
    undergraduates_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[9]/td[3]/span/text()')
    undergraduates_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[9]/td[4]/span/text()')
    data.append((int(undergraduates_total[0]), int(undergraduates_male[0]), int(undergraduates_fomale[0])))
    
    ##  normal
    normal_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[10]/td[2]/span/text()')
    normal_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[10]/td[3]/span/text()')
    normal_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[10]/td[4]/span/text()')
    data.append((int(normal_total[0]), int(normal_male[0]), int(normal_fomale[0])))
    
    ##  short_cycle
    short_cycle_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[11]/td[2]/span/text()')
    short_cycle_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[11]/td[3]/span/text()')
    short_cycle_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/div/div/table/tbody/tr[11]/td[4]/span/text()')
    data.append((int(short_cycle_total[0]), int(short_cycle_male[0]), int(short_cycle_fomale[0])))
    
#    for i in range(len(data)):
#        print(data[i])
    return data

def get_data_2013(html, headers):
    html = requests.get(html,headers=headers)
    
    data = []
    etree_html = etree.HTML(html.text)
    ##  postgraduates
    postgraduates_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[4]/td[2]/p/span/text()')
    postgraduates_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[4]/td[3]/p/span/text()')
    postgraduates_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[4]/td[2]/p/span/text()')
    data.append((int(postgraduates_total[0]), int(postgraduates_male[0]), int(postgraduates_fomale[0])))
    
    ##  doctor
    doctor_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[5]/td[2]/p/span/text()')
    doctor_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[5]/td[3]/p/span/text()')
    doctor_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[5]/td[4]/p/span/text()')
    data.append((int(doctor_total[0]), int(doctor_male[0]), int(doctor_fomale[0])))
    
    ##  master
    master_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[6]/td[2]/p/span/text()')
    master_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[6]/td[3]/p/span/text()')
    master_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[6]/td[4]/p/span/text()')
    data.append((int(master_total[0]), int(master_male[0]), int(master_fomale[0])))
    
    ##  undergraduates
    undergraduates_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[7]/td[2]/p/span/text()')
    undergraduates_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[7]/td[3]/p/span/text()')
    undergraduates_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[7]/td[4]/p/span/text()')
    data.append((int(undergraduates_total[0]), int(undergraduates_male[0]), int(undergraduates_fomale[0])))
    
    ##  normal
    normal_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[8]/td[2]/p/span/text()')
    normal_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[8]/td[3]/p/span/text()')
    normal_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[8]/td[4]/p/span/text()')
    data.append((int(normal_total[0]), int(normal_male[0]), int(normal_fomale[0])))
    
    ##  short_cycle
    short_cycle_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[9]/td[2]/p/span/text()')
    short_cycle_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[9]/td[3]/p/span/text()')
    short_cycle_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/table/tbody/tr[9]/td[4]/p/span/text()')
    data.append((int(short_cycle_total[0]), int(short_cycle_male[0]), int(short_cycle_fomale[0])))
    
#    for i in range(len(data)):
#        print(data[i])
    return data

def get_data_2011(html, headers):
    html = requests.get(html,headers=headers)
    
    data = []
    etree_html = etree.HTML(html.text)
    ##  postgraduates
    postgraduates_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[4]/td[2]/p/span/text()')
    postgraduates_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[4]/td[3]/p/span/text()')
    postgraduates_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[4]/td[4]/p/span/text()')
    data.append((int(postgraduates_total[0]), int(postgraduates_male[0]), int(postgraduates_fomale[0])))
    
    ##  doctor
    doctor_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[5]/td[2]/p/span/text()')
    doctor_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[5]/td[3]/p/span/text()')
    doctor_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[5]/td[4]/p/span/text()')
    data.append((int(doctor_total[0]), int(doctor_male[0]), int(doctor_fomale[0])))
    
    ##  master
    master_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[6]/td[2]/p/span/text()')
    master_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[6]/td[3]/p/span/text()')
    master_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[6]/td[4]/p/span/text()')
    data.append((int(master_total[0]), int(master_male[0]), int(master_fomale[0])))
    
    ##  undergraduates
    undergraduates_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[7]/td[2]/p/span/text()')
    undergraduates_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[7]/td[3]/p/span/text()')
    undergraduates_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[7]/td[4]/p/span/text()')
    data.append((int(undergraduates_total[0]), int(undergraduates_male[0]), int(undergraduates_fomale[0])))
    
    ##  normal
    normal_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[8]/td[2]/p/span/text()')
    normal_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[8]/td[3]/p/span/text()')
    normal_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[8]/td[4]/p/span/text()')
    data.append((int(normal_total[0]), int(normal_male[0]), int(normal_fomale[0])))
    
    ##  short_cycle
    short_cycle_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[9]/td[2]/p/span/text()')
    short_cycle_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[9]/td[3]/p/span/text()')
    short_cycle_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/div/div/table/tbody/tr[9]/td[4]/p/span/text()')
    data.append((int(short_cycle_total[0]), int(short_cycle_male[0]), int(short_cycle_fomale[0])))
    
#    for i in range(len(data)):
#        print(data[i])
    return data

def get_data_2010(html, headers):
    html = requests.get(html,headers=headers)
    
    data = []
    etree_html = etree.HTML(html.text)
    ##  postgraduates
    postgraduates_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[6]/td[2]/p/span/span/text()')
    postgraduates_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[6]/td[3]/p/span/span/text()')
    postgraduates_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[6]/td[4]/p/span/span/text()')
    data.append((int(postgraduates_total[0]), int(postgraduates_male[0]), int(postgraduates_fomale[0])))
    
    ##  doctor
    doctor_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[7]/td[2]/p/span/span/text()')
    doctor_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[7]/td[3]/p/span/span/text()')
    doctor_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[7]/td[4]/p/span/span/text()')
    data.append((int(doctor_total[0]), int(doctor_male[0]), int(doctor_fomale[0])))
    
    ##  master
    master_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[8]/td[2]/p/span/span/text()')
    master_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[8]/td[3]/p/span/span/text()')
    master_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[8]/td[4]/p/span/span/text()')
    data.append((int(master_total[0]), int(master_male[0]), int(master_fomale[0])))
    
    ##  undergraduates
    undergraduates_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[9]/td[2]/p/span/span/text()')
    undergraduates_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[9]/td[3]/p/span/span/text()')
    undergraduates_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[9]/td[4]/p/span/span/text()')
    data.append((int(undergraduates_total[0]), int(undergraduates_male[0]), int(undergraduates_fomale[0])))
    
    ##  normal
    normal_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[10]/td[2]/p/span/span/text()')
    normal_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[10]/td[3]/p/span/span/text()')
    normal_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[10]/td[4]/p/span/span/text()')
    data.append((int(normal_total[0]), int(normal_male[0]), int(normal_fomale[0])))
    
    ##  short_cycle
    short_cycle_total = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[11]/td[2]/p/span/span/text()')
    short_cycle_male = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[11]/td[3]/p/span/span/text()')
    short_cycle_fomale = etree_html.xpath('//*[@id="content_body_txt"]/tbody/tr[1]/td[2]/table/tbody/tr[11]/td[4]/p/span/span/text()')
    data.append((int(short_cycle_total[0]), int(short_cycle_male[0]), int(short_cycle_fomale[0])))
    
#    for i in range(len(data)):
#        print(data[i])
    return data



def gettime():
    return int(round(time.time() * 1000))

def get_data_gra():
    # 用来自定义头部的
    headers = {}
    # 用来传递参数的
    keyvalue = {}
    # 目标网址(问号前面的东西)
#    url = 'http://data.stats.gov.cn/easyquery.htm?cn=C01'
    url = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A0M09%22%7D%5D&k1=1584526702747&h=1'

    # 头部的填充
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'

    # 下面是参数的填充，参考图10
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0M09"}]'
    keyvalue['k1'] = str(gettime())

    # 发出请求，使用get方法，这里使用我们自定义的头部和参数
    # r = requests.get(url, headers=headers, params=keyvalue)
    # 建立一个Session
    s = requests.session()
    # 在Session基础上进行一次请求
 #   r = s.get(url, params=keyvalue, headers=headers)
    r = s.get(url, headers=headers)

    etree_html = etree.HTML(r.text)
    ##  postgraduates
    data = etree_html.xpath('//*[@id="table_main"]/tbody/tr[1]/td[2]/text()')
#    print(data)

## 打印返回过来的状态码
#    print (r.text)
#    print(type(r.text))

    res = json.loads(r.text)
#    print(res)  # 打印字典
#    print(type(res))  #打印res类型
#    print(res.keys())  #打印字典的所有key

    gra_data = []
    for i in range(len(res['returndata']['datanodes'])):
        if res['returndata']['datanodes'][i]['wds'][0]['valuecode'] == 'A0M0901':
#            print(res['returndata']['datanodes'][i]['data']['strdata'], res['returndata']['datanodes'][i]['wds'][1]['valuecode'])
#            print('\n')
            gra_data.append([int(res['returndata']['datanodes'][i]['wds'][1]['valuecode']), float(res['returndata']['datanodes'][i]['data']['strdata'])])
#    print(gra_data)

#    # 修改dfwds字段内容
#    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"2000"}]'
#    # 再次进行请求
#    r = s.get(url, params=keyvalue, headers=headers)
#    # 此时我们就能获取到我们搜索到的数据了
#    print (r.text)
    return gra_data

def graph_four_data(data1, data2, data3, data4):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    x4 = []
    y4 = []
    for i in range(len(data1)):
        x1.append(data1[i][0])
        y1.append(data1[i][1])
        x2.append(data2[i][0])
        y2.append(data2[i][1])
        x3.append(data3[i][0])
        y3.append(data3[i][1])
        x4.append(data4[i][0])
        y4.append(data4[i][1])
    fig = plt.figure()
    ax = plt.subplot(111)
    plt.title('在校男女生性别比(女生=100)', fontsize=20)
#    plt.xlabel('年份', fontsize=20)
#    plt.ylabel('男女性别比', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    ax.set_xlabel('年份', fontsize=20)
    ax.set_ylabel('男女性别比', fontsize=20)
#    plt.scatter(x, y, s=10, alpha=0.5) #alpha为透明度，s为size， c为颜色
    ln1, = plt.plot(x1,y1,linestyle='-', linewidth = 2.0)
    ln2, = plt.plot(x2,y2,linestyle='-',linewidth = 2.0)
    ln3, = plt.plot(x3,y3,linestyle='-',linewidth = 2.0)
    ln4, = plt.plot(x4,y4,linestyle='-',linewidth = 2.0)
    matplotlib.rcParams.update({'font.size': 20})
    plt.legend(handles=[ln1, ln2, ln3, ln4], labels=['博士', '硕士', '本科', '专科'], bbox_to_anchor=(1.008, 0), loc=3, fontsize=20)
    plt.grid()
    plt.show()

def graph_one_data(data):
    x1 = []
    y1 = []

    for i in range(len(data)):
        x1.append(data[i][0])
        y1.append(data[i][1])

    fig = plt.figure()
    ax = plt.subplot(111)
    plt.title('毕业生人数(万人)', fontsize=20)
#    plt.xlabel('年份', fontsize=20)
#    plt.ylabel('男女性别比', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    ax.set_xlabel('年份', fontsize=20)
    ax.set_ylabel('每年毕业人数', fontsize=20)
#    plt.scatter(x, y, s=10, alpha=0.5) #alpha为透明度，s为size， c为颜色
    plt.plot(x1,y1,linestyle='-', linewidth = 2.0)

    plt.grid()
    plt.show()

def graph_two_data(data1, data2):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for i in range(min(len(data1), len(data2))):
        x1.append(data1[i+1][0])
        y1.append(data1[i+1][1])
        x2.append(data2[i][0])
        y2.append(data2[i][1])
    fig = plt.figure()
    ax = plt.subplot(111)
    plt.title('每年毕业生人数及毕业比例', fontsize=20)
#    plt.xlabel('年份', fontsize=20)
#    plt.ylabel('男女性别比', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    ax.set_xlabel('年份', fontsize=20)

    ln1,= ax.plot(x1, y1, '-', linewidth = 2.0)
    ax2 = ax.twinx()
    ln2,= ax2.plot(x2, y2, '-r', linewidth = 2.0)
#    ax.legend(loc=0)
    ax.grid()
#    ax.set_xlabel("Time (h)")
    ax.set_ylabel("每年毕业人数")
    ax2.set_ylabel("预计毕业生/实际毕业生")
    plt.legend(frameon=True)
    plt.legend(handles=[ln1, ln2], labels=['每年毕业人数', '预计毕业生/实际毕业生'], bbox_to_anchor=(0.6, 0.8), loc=4, fontsize=20)
    plt.grid()
    plt.show()

def histogram(data):
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for i in range(len(data)):
#        x.append(data[i][0])
        y1.append(round(data[i][1]*100, 2))
        y2.append(round(data[i][2]*100, 2))
        y3.append(round(data[i][3]*100, 2))
        y4.append(round(data[i][4]*100, 2))

    x = np.arange(len(data))
    
    total_width, n = 0.8, 4     # 有多少个类型，只需更改n即可
    width = total_width / n
    x = x - (total_width - width) / 2
    
    plt.bar(x+2010, y1,  width=width, label='博士')
    plt.bar(x+2010 + width, y2, width=width, label='硕士')
    plt.bar(x+2010 + 2 * width, y3, width=width, label='本科')
    plt.bar(x+2010 + 3 * width, y4, width=width, label='专科')
    
    plt.xticks()
    plt.legend(bbox_to_anchor=(1.008, 0), loc=3, fontsize=20)  # 防止label和图像重合显示不出来
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.ylabel('毕业生占总毕业生比例(%)')
    plt.xlabel('年份')

    from matplotlib.pyplot import MultipleLocator
    x_major_locator=MultipleLocator(1)
    #把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator=MultipleLocator(10)
    #把y轴的刻度间隔设置为10，并存在变量里
    ax=plt.gca()
    #ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    #把x轴的主刻度设置为1的倍数

    plt.rcParams['savefig.dpi'] = 300  # 图片像素
    plt.rcParams['figure.dpi'] = 300  # 分辨率
    plt.rcParams['figure.figsize'] = (15.0, 8.0)  # 尺寸
    plt.title("各级毕业生占比")
#    plt.savefig('D:\\result.png')
    plt.show()

def area_chart(data):
    # data
    x = []
    y1 = []
    y2 = []
    y3 = []
    for i in range(len(data)):
        x.append(data[i][0])
        y1.append(data[i][1]/1e4)
        y2.append(data[i][2]/1e4)
        y3.append(round(data[i][1]/data[i][2]*100, 2))
    x = np.array(x)  # x坐标
    y1 = np.array(y1) 
    y2 = np.array(y2)

    labels = ["男毕业生人数", "女毕业生人数"] 
    
    # figure
#    fig =plt.figure(figsize = (12,6))
    fig =plt.figure()
    ax = plt.subplot(111)
    
    # plot
    ax.stackplot(x, y1, y2, labels=labels) #堆积面积图
    #增加标记（美化）
    ax.plot(x,y1,'-', alpha=0.5)
    ax.plot(x,y1+y2,'-', alpha=0.5)

    
    # setting
    ax.legend(bbox_to_anchor=(0.15, 0.8), loc=3, fontsize=10) #图例

    # 修改x轴的刻度
    plt.xticks(x, fontsize=10)
    plt.yticks(fontsize=10)

    ax2 = ax.twinx()
    ln2,= ax2.plot(x, y3, alpha=0.5, c='r')
#    ax.legend(loc=0)
    ax.grid()
#    ax.set_xlabel("Time (h)")
    ax.set_ylabel("每年毕业人数(万人)", fontsize=10)
    ax.set_xlabel('年份', fontsize=10)
    ax2.set_ylabel("男生/女生(女生=100)", fontsize=10)

    
    # 剔除图框上边界和右边界的刻度
    plt.tick_params(top = 'off', right = 'off')

    plt.rcParams['savefig.dpi'] = 300 #图片像素
    plt.rcParams['figure.dpi'] = 300 #分辨率
    plt.title('每年毕业生男女生人数及占比', fontsize = 10)

    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    plt.show()

def pie_chart(data):
    labels = '男生', '女生'
    sizes = [data[0], data[1]]
    
    # 设置分离的距离，0表示不分离
    explode = (0, 0) 
    
    patches,l_text,p_text = plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    
    # Equal aspect ratio 保证画出的图是正圆形
    plt.axis('equal', fontsize=10) 
    plt.title('2010-2018年总毕业生人数性别比', fontsize=10)

    #改变文本的大小
    #方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size(10)
    for t in p_text:
        t.set_size(10)
    
    plt.show()

def radar_chart(data1, data2):
    labels = np.array(['博士','硕士','本科','专科'])
    #数据个数
    dataLenth = 4
    #数据
    del(data1[0])
    del(data2[0])
    for i in range(len(data1)):
        data1[i] = data1[i]/1e4
        data2[i] = data2[i]/1e4
    data = np.array(data1)
    data2 = np.array(data2)
    #========自己设置结束============
    
    angles = np.linspace(np.pi/4, 2.25*np.pi, dataLenth, endpoint=False)
    print(angles)
    data = np.concatenate((data, [data[0]])) # 闭合
    angles = np.concatenate((angles, [angles[0]])) # 闭合
    
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)# polar参数！！
    ax.plot(angles, data, 'ro-', c='r', linewidth=1, alpha=0.5)# 画线
    ax.fill(angles, data, facecolor='r', alpha=0.5)# 填充

    data2 = np.concatenate((data2, [data2[0]])) # 闭合
    ax.plot(angles, data2, 'go-', c='g', linewidth=1, alpha=0.5)# 画线
    ax.fill(angles, data2, facecolor='g', alpha=0.5)# 填充

    ax.set_thetagrids(angles * 180/np.pi, labels, fontsize = 10)    #不显示角度值
    ax.set_title("matplotlib雷达图", va='bottom', fontsize = 10)
    ax.set_rlim(0, 1.05 * max(max(data1), max(data2)))
    ax.grid(True)

    labels = ('男毕业生人数', '女毕业生人数')
    legend = plt.legend(labels, bbox_to_anchor=(0.99, 0), loc=3, fontsize=10, labelspacing=0.1)
    plt.setp(legend.get_texts(), fontsize = 10)
    plt.title('至2018年各级毕业生总数', fontsize = 10)
    plt.show()


### 没有用到
'''
def waterfall_chart(data):
    x = []
    y = []
    for i in range(len(data)):
        x.append(data[i][0])
        y.append(data[i][2])
    fig = go.Figure(go.Waterfall(
        name = "20", orientation = "v",
        measure = ["relative", "relative", "total", "relative", "relative", "total"],
        x = ["Sales", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"],
        textposition = "outside",
        text = ["+60", "+80", "", "-40", "-20", "Total"],
        y = [60, 80, 0, -40, -20, 0],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))
    
    fig.update_layout(
            title = "Profit and loss statement 2018",
            showlegend = True
    )
    
    fig.show()
'''
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.2, 1.03*height, '%s' % float(height),color="black",ha="left", va= 'top',fontsize=10)

def histogram2(data):
    plt.figure( dpi=300)
    # 柱子总数
    N = len(data)
    x = []
    y1 = []
    y2 = []
    for i in range(len(data)):
        x.append(data[i][0])
        y1.append(data[i][1])
        y2.append(int(data[i][2]/1e4))
    # 包含每个柱子对应值的序列
    values = (56796,42996,24872,13849,8609,5331,1971,554,169,26)
    # 包含每个柱子下标的序列
    index = np.arange(N)
    # 柱子的宽度
    width = 0.6
    # 绘制柱状图, 每根柱子的颜色为紫罗兰色
    ax = plt.subplot(111)
    p2 = plt.bar(index+2010, y2, width, label="num", color="#87CEFA")
    plt.xticks(x, fontsize=10)
    plt.yticks(fontsize=10)
    for a,b in zip(x,y2): 
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10, color = 'b') 
    ax2 = ax.twinx()
    ln2,= ax2.plot(x, y1, alpha=0.5, c='r')
    # 设置横轴标签
#    plt.xlabel('年份', fontsize = 10)
    # 设置纵轴标签
    ax.set_ylabel('男生-女生数(万人)', fontsize = 10)
    ax.set_xlabel('年份', fontsize = 10)
    ax2.set_ylabel('男女比（女=100）', fontsize = 10)
## ax2设置x轴标签无效!!!
#    ax2.set_xlabel('年份', fontsize = 10)
##显示每处的数据，方法一：
    for a,b in zip(x,y1): 
        plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'top',fontsize=10, color = 'r') 
##显示每处的数据，方法二：
    '''    
    for a,b in zip(x,y1):
        plt.annotate('%.2f'%float(b), xy=(a,b), xytext=(-20,10), textcoords='offset points', fontsize=10, color='r')
    '''

    plt.title('2010年始男女性毕业生总数统计（万人）', fontsize = 10)

    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    plt.show()

if __name__ == '__main__':
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    html_2018 = "http://www.moe.gov.cn/s78/A03/moe_560/jytjsj_2018/qg/201908/t20190812_394231.html"
    html_2017 = "http://www.moe.gov.cn/s78/A03/moe_560/jytjsj_2017/qg/201808/t20180808_344694.html"
    html_2016 = "http://www.moe.gov.cn/s78/A03/moe_560/jytjsj_2016/2016_qg/201708/t20170822_311614.html"
    html_2015 = "http://www.moe.gov.cn/s78/A03/moe_560/jytjsj_2015/2015_qg/201610/t20161012_284506.html"
    html_2014 = "http://www.moe.gov.cn/s78/A03/moe_560/jytjsj_2014/2014_qg/201509/t20150902_205095.html"
    html_2013 = "http://www.moe.gov.cn/s78/A03/moe_560/s8492/s8493/201412/t20141216_181716.html"
    html_2012 = "http://www.moe.gov.cn/s78/A03/moe_560/s7567/201309/t20130904_156890.html"
    html_2011 = "http://www.moe.gov.cn/s78/A03/moe_560/s7382/201305/t20130529_152561.html"
    html_2010 = "http://www.moe.gov.cn/s78/A03/moe_560/s6200/201201/t20120117_129613.html"

    #每年各级各类学校女学生数
    data=[]
    data_2018 = [2018] + get_data(html_2018, headers)
    data_2017 = [2017] + get_data(html_2017, headers)
    data_2016 = [2016] + get_data(html_2016, headers)
    data_2015 = [2015] + get_data(html_2015, headers)
    data_2014 = [2014] + get_data_2014(html_2014, headers)
    data_2013 = [2013] + get_data_2013(html_2013, headers)
    data_2012 = [2012] + get_data_2013(html_2012, headers)
    data_2011 = [2011] + get_data_2011(html_2011, headers)
    data_2010 = [2010] + get_data_2010(html_2010, headers)
    data = [data_2010] + [data_2011] + [data_2012] + [data_2013] + [data_2014] + [data_2015] + [data_2016] + [data_2017] + [data_2018]
    #每年毕业生人数
    gra_data = get_data_gra()

    #统计计算

    #每年女生学比
    female_ratio_doc = []
    female_ratio_mas = []
    female_ratio_und = []       #Undergraduate
    female_ratio_sho = []       #Short-cycle Courses
    for i in range(2010, 2019):
        if data[i-2010][0] == i:
            female_ratio_doc.append([i,round(data[i-2010][2][1]/data[i-2010][2][2]*100, 2)])  #[年份，男/女*100(百分比)]
            female_ratio_mas.append([i,round(data[i-2010][3][1]/data[i-2010][3][2]*100, 2)])  #[年份，男/女*100(百分比)]
            female_ratio_und.append([i,round(data[i-2010][5][1]/data[i-2010][5][2]*100, 2)])  #[年份，男/女*100(百分比)]
            female_ratio_sho.append([i,round(data[i-2010][6][1]/data[i-2010][6][2]*100, 2)])  #[年份，男/女*100(百分比)]
    graph_four_data(female_ratio_doc, female_ratio_mas, female_ratio_und, female_ratio_sho)

    #每年毕业生人数以及比例
    data_gra_ratio = []
    classification_ratio = []
    for i in range(2010, 2019):
        if data[i-2010][0] == i:
            for j in range(len(gra_data)):
                if gra_data[j][0] == i:
                    theoretical_num = (data[i-2010][2][0]/4 + data[i-2010][3][0]/3 + data[i-2010][5][0]/4 + data[i-2010][6][0]/3)
                    data_gra_ratio.append([i,round(theoretical_num/gra_data[j][1]/1e4, 2)])  #[年份，男/女*100(百分比)]

                    classification_ratio.append([i, data[i-2010][2][0]/4/theoretical_num, data[i-2010][3][0]/3/theoretical_num, data[i-2010][5][0]/4/theoretical_num, data[i-2010][6][0]/3/theoretical_num])

    graph_two_data(gra_data, data_gra_ratio)
    histogram(classification_ratio)

    #截至2018年毕业男女比例
    sum_all = []
    doc_all = []
    mas_all = []
    und_all = []
    sho_all = []
    for i in range(2010, 2019):
        if data[i-2010][0] == i and female_ratio_doc[i-2010][0] == i and  female_ratio_mas[i-2010][0] == i and female_ratio_und[i-2010][0] == i and female_ratio_sho[i-2010][0] == i:
            male_all = data[i-2010][2][1]/4 + data[i-2010][3][1]/3 + data[i-2010][5][1]/4 + data[i-2010][6][1]/3
            female_all = data[i-2010][2][2]/4 + data[i-2010][3][2]/3 + data[i-2010][5][2]/4 + data[i-2010][6][2]/3
            theoretical_num = (data[i-2010][2][0]/4 + data[i-2010][3][0]/3 + data[i-2010][5][0]/4 + data[i-2010][6][0]/3)            
            for j in range(len(gra_data)):
                if gra_data[j][0] == i:
                    sum_all.append([i, int(gra_data[j][1]*1e4/theoretical_num * male_all), int(gra_data[j][1]*1e4/theoretical_num * female_all)])
                    doc_all.append([i, int(gra_data[j][1]*1e4/theoretical_num*data[i-2010][2][1]/4), int(gra_data[j][1]*1e4/theoretical_num*data[i-2010][2][2]/4)])
                    mas_all.append([i, int(gra_data[j][1]*1e4/theoretical_num*data[i-2010][3][1]/3), int(gra_data[j][1]*1e4/theoretical_num*data[i-2010][3][2]/3)])
                    und_all.append([i, int(gra_data[j][1]*1e4/theoretical_num*data[i-2010][5][1]/4), int(gra_data[j][1]*1e4/theoretical_num*data[i-2010][5][2]/4)])
                    sho_all.append([i, int(gra_data[j][1]*1e4/theoretical_num*data[i-2010][6][1]/3), int(gra_data[j][1]*1e4/theoretical_num*data[i-2010][6][2]/3)])

    area_chart(sum_all)

    #计算2018年度已毕业人数
    gra_num = []
    male=0
    female=0
    categories_male_num = []
    categories_female_num = []
    print(len(sum_all), len(doc_all), len(mas_all))
    for i in range(len(sum_all)):
        male = male + sum_all[i][1]
        female = female + sum_all[i][2]
        gra_num.append([sum_all[i][0], male, female, round((male/female*100), 2)])
        if len(categories_male_num) == 0:
            categories_male_num.append([sum_all[i][0], doc_all[i][1], mas_all[i][1], und_all[i][1], sho_all[i][1]])
            categories_female_num.append([sum_all[i][0], doc_all[i][2], mas_all[i][2], und_all[i][2], sho_all[i][2]])
        else:
            categories_male_num.append([sum_all[i][0], categories_male_num[i-1][1] + doc_all[i][1], categories_male_num[i-1][2] + mas_all[i][1], 
                categories_male_num[i-1][3] + und_all[i][1], categories_male_num[i-1][4] + sho_all[i][1]])
            categories_female_num.append([sum_all[i][0], categories_female_num[i-1][1] + doc_all[i][2], categories_female_num[i-1][2] + mas_all[i][2], 
                categories_female_num[i-1][3] + und_all[i][2], categories_female_num[i-1][4] + sho_all[i][2]])

    pie_chart([gra_num[-1][1], gra_num[-1][2]])
    per_year_gra = []
    for i in range(len(gra_num)):
        print(gra_num[i][0], gra_num[i][1]/float(gra_num[i][2])*100, gra_num[i][1] - gra_num[i][2])
        per_year_gra.append((gra_num[i][0], gra_num[i][1]/float(gra_num[i][2])*100, gra_num[i][1] - gra_num[i][2]))

    radar_chart(categories_male_num[-1], categories_female_num[-1])
    histogram2(per_year_gra)