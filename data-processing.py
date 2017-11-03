# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
# import itchat
# itchat.auto_login(hotReload=True)
# itchat.send_msg('begin')

data_path = 'C:/Users/wangyicheng/Desktop/5001project/data/csv1.csv'
column_name_path = 'C:/Users/wangyicheng/Desktop/5001project/data/header.xlsx'
all_vids_path = 'C:/Users/wangyicheng/Desktop/5001project/data/all_car_vid.csv'
out_path = 'C:/Users/wangyicheng/Desktop/5001project/dataprocessing/'
need_data_index = [1,2,13,14,15,18,21,80,81,82,83,85,161,165]
#
columns = pd.read_excel(column_name_path,0).columns.values[need_data_index]
vids = pd.read_csv(all_vids_path,encoding='UTF-8').values[:,1]
'''选取前N锟斤拷vid'''
N = 5
need_vids = vids[0:N].tolist()
'''
锟斤拷取vid锟斤拷应锟斤拷锟斤拷锟斤拷
'''
of = open(data_path,'r')                                    #锟斤拷锟侥硷拷
line = True
i = 0
final_data = []
while line:
    line = of.readline()                                    #锟斤拷取锟斤拷锟斤拷
    try:
        temp = line.split(',')                              #锟斤拷锟斤拷锟脚分革拷
        vid = temp[1]                                       #锟斤拷取锟斤拷锟斤拷vid
        if vid in need_vids:                                #锟斤拷锟斤拷诟锟斤拷锟斤拷锟�
            odata = np.asarray(temp)[need_data_index]       #锟斤拷锟斤拷取锟斤拷要锟斤拷锟斤拷锟斤拷
            #锟剿达拷锟斤拷颖锟斤拷锟斤拷锟诫，锟斤拷vid写锟斤拷锟街典保锟斤拷
            final_data.append(odata)

    except:
        p = 0
    #
    i+= 1
    if i%100000 == 0: print('已经读取到第%d行'%i)


final_data = pd.DataFrame(data=final_data,columns=columns)
final_data.to_csv(out_path+'前10条vid.csv',index=False)

#itchat.send_msg('ok')
#

