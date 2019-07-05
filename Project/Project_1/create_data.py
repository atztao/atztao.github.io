'''
此函数用来产生训练数据和测试数据.WS:小世界网络,ER:ER随机网络,BA:BA无标度网络,GZ:规则网络
'''

import networkx as nx
import numpy as np


def output_train_WS(N, S, L):
    '''
    此N用来产生数据的个数,S为矩阵的大小,L为连边的个数
    '''
    f = open("Data/train_data_WS.txt",
             "wb")  # 打开文件
    f.truncate()  # 清空文件
    step = 1 / N  # 此常量为更新数据的步长
    for i in range(N):
        ws = nx.random_graphs.watts_strogatz_graph(S, L, i*step)  # 此为小世界网络
        a = nx.to_numpy_matrix(ws)  # 此变量为转化后的邻接矩阵
        b = a.reshape(1, -1)
        np.savetxt(f, b, delimiter=",", fmt="%d")   # 写入文件
    f.close()  # 关闭文件


def output_train_ER(N, S):
    f = open("Data/train_data_ER.txt",
             "wb")  # 打开文件
    f.truncate()  # 清空文件
    step = 1 / N  # 此常量为更新数据的步长
    for i in range(N):
        ws = nx.random_graphs.erdos_renyi_graph(S, i*step)  # 此为ER随机网络
        a = nx.to_numpy_matrix(ws)  # 此变量为转化后的邻接矩阵
        b = a.reshape(1, -1)
        np.savetxt(f, b, delimiter=",", fmt="%d")   # 写入文件
    f.close()  # 关闭文件


def output_train_BA(N, S, L):
    f = open("Data/train_data_BA.txt",
             "wb")  # 打开文件
    f.truncate()  # 清空文件
    for i in range(N):
        ws = nx.random_graphs.barabasi_albert_graph(S, L)  # 此为BA无标度网络
        a = nx.to_numpy_matrix(ws)  # 此变量为转化后的邻接矩阵
        b = a.reshape(1, -1)
        np.savetxt(f, b, delimiter=",", fmt="%d")   # 写入文件
    f.close()  # 关闭文件


def output_train_GZ(N, S, L):
    f = open("Data/train_data_GZ.txt",
             "wb")  # 打开文件
    f.truncate()  # 清空文件
    for i in range(N):
        ws = nx.random_graphs.random_regular_graph(S, L)  # 此为规则网络
        a = nx.to_numpy_matrix(ws)  # 此变量为转化后的邻接矩阵
        b = a.reshape(1, -1)
        np.savetxt(f, b, delimiter=",", fmt="%d")   # 写入文件
    f.close()  # 关闭文件


def output_test_WS(N, S, L):
    '''
    此N用来产生数据的个数,S为矩阵的大小,L为连边的个数
    '''
    f = open("Data/test_data_WS.txt",
             "wb")   # 打开文件
    f.truncate()  # 清空文件
    step = 1 / N  # 此常量为更新数据的步长
    for i in range(N):
        ws = nx.random_graphs.watts_strogatz_graph(S, L, i*step)  # 此为小世界网络
        a = nx.to_numpy_matrix(ws)  # 此变量为转化后的邻接矩阵
        b = a.reshape(1, -1)
        np.savetxt(f, b, delimiter=",", fmt="%d")   # 写入文件
    f.close()  # 关闭文件


def output_test_ER(N, S):
    f = open("Data/test_data_ER.txt",
             "wb")  # 打开文件
    f.truncate()  # 清空文件
    step = 1 / N  # 此常量为更新数据的步长
    for i in range(N):
        ws = nx.random_graphs.erdos_renyi_graph(S, i*step)  # 此为ER随机网络
        a = nx.to_numpy_matrix(ws)  # 此变量为转化后的邻接矩阵
        b = a.reshape(1, -1)
        np.savetxt(f, b, delimiter=",", fmt="%d")   # 写入文件
    f.close()  # 关闭文件


def output_test_BA(N, S, L):
    f = open("Data/test_data_BA.txt",
             "wb")  # 打开文件
    f.truncate()  # 清空文件
    for i in range(N):
        ws = nx.random_graphs.barabasi_albert_graph(S, L)  # 此为BA无标度网络
        a = nx.to_numpy_matrix(ws)  # 此变量为转化后的邻接矩阵
        b = a.reshape(1, -1)
        np.savetxt(f, b, delimiter=",", fmt="%d")   # 写入文件
    f.close()  # 关闭文件


def output_test_GZ(N, S, L):
    f = open("Data/test_data_GZ.txt",
             "wb")  # 打开文件
    f.truncate()  # 清空文件
    for i in range(N):
        ws = nx.random_graphs.random_regular_graph(S, L)  # 此为规则网络
        a = nx.to_numpy_matrix(ws)  # 此变量为转化后的邻接矩阵
        b = a.reshape(1, -1)
        np.savetxt(f, b, delimiter=",", fmt="%d")   # 写入文件
    f.close()  # 关闭文件


output_test_WS(10000, 28, 20)
