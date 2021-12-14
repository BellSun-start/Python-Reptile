# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Author:玄铁重剑无锋
# # @Author  :   {玄铁重剑无锋}
# # @License :   (C) Copyright 2021 玄铁重剑无锋, All rights reserved.
# # @Contact :   {sfrexpect@163.com}
# # @File    :   test_list.py
# # @Time    :   2021/11/12 14:43
# # @Desc    :
# # coding: utf-8
# '''　　多线程 Socket TCP 端口扫描器  by: EvilCLAY'''
# import socket
# from datetime import datetime
# from multiprocessing.dummy import Pool as ThreadPool
#
# remote_server = list[]
# remote_server_ip = socket.gethostbyname(remote_server)
# ports = []
#
# print( '-' * 60)
# print('Please wait, scanning remote host ', remote_server_ip)
# print('-' * 60)
#
# socket.setdefaulttimeout(0.5)
#
#
# def scan_port(port):
#     try:
#         s = socket.socket(2, 1)
#         res = s.connect_ex((remote_server_ip, port))
#         if res == 0:  # 如果端口开启 发送 hello 获取banner
#             print
#             'Port {}: OPEN'.format(port)
#         s.close()
#     except Exception, e:
#         print
#         str(e.message)
#
#
# for i in range(1, 1025):
#     ports.append(i)
#
# # Check what time the scan started
# t1 = datetime.now()
#
# pool = ThreadPool(processes=8)
# results = pool.map(scan_port, ports)
# pool.close()
# pool.join()
#
# print
# 'Multiprocess Scanning Completed in  ', datetime.now() - t1