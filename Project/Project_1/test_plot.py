'''
此程序用来测试不同的网络在一个用一种复杂网络训练过的自编码网络上的表现
'''
from create_data import output_test_WS, output_test_BA
from create_data import output_test_ER, output_test_GZ
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import torch
from torch.autograd import Variable
from AutoEncoder_NN import AutoEncoder_2D


#  载入模型
autoencoder_2D = AutoEncoder_2D()
autoencoder_2D.load_state_dict(torch.load('AutoEncoder_2D.pkl'))

#  生成数据
output_test_WS(100000, 28, 15)
output_test_BA(100000, 28, 20)
output_test_ER(100000, 28)
output_test_GZ(100000, 25, 28)

# 利用pandas导入数据
test_data_WS = pd.read_csv('Data/test_data_WS.txt', sep=',', header=None)
test_data_WS = test_data_WS.values  # 转换为numpy array
# print(data[0:27, :])
test_data_WS = torch.from_numpy(test_data_WS)


test_encoded_WS_2D = []

for i in range(100000):
        x = test_data_WS[i]
        x = x.float()

        # print(x)
        b_x = Variable(x.view(-1, 28*28))
        encoded, decoded = autoencoder_2D(b_x)  # 返回两个值
        test_encoded_WS_2D.append(encoded.data.numpy())  # 收集压缩后的特征值
test_encoded_WS_2D = np.vstack(test_encoded_WS_2D)  # 将list类型转换为array

# 利用pandas导入数据
test_data_ER = pd.read_csv('Data/test_data_ER.txt', sep=',', header=None)
test_data_ER = test_data_ER.values  # 转换为numpy array
# print(data[0:27, :])
test_data_ER = torch.from_numpy(test_data_ER)


test_encoded_ER_2D = []

for i in range(100000):
        x = test_data_ER[i]
        x = x.float()

        # print(x)
        b_x = Variable(x.view(-1, 28*28))
        encoded, decoded = autoencoder_2D(b_x)  # 返回两个值
        test_encoded_ER_2D.append(encoded.data.numpy())  # 收集压缩后的特征值
test_encoded_ER_2D = np.vstack(test_encoded_ER_2D)  # 将list类型转换为array


# 利用pandas导入数据
test_data_BA = pd.read_csv('Data/test_data_BA.txt', sep=',', header=None)
test_data_BA = test_data_BA.values  # 转换为numpy array
# print(data[0:27, :])
test_data_BA = torch.from_numpy(test_data_BA)


test_encoded_BA_2D = []

for i in range(100000):
        x = test_data_BA[i]
        x = x.float()

        # print(x)
        b_x = Variable(x.view(-1, 28*28))
        encoded, decoded = autoencoder_2D(b_x)  # 返回两个值
        test_encoded_BA_2D.append(encoded.data.numpy())  # 收集压缩后的特征值
test_encoded_BA_2D = np.vstack(test_encoded_BA_2D)  # 将list类型转换为array


# 利用pandas导入数据
test_data_GZ = pd.read_csv('Data/test_data_GZ.txt', sep=',', header=None)
test_data_GZ = test_data_GZ.values  # 转换为numpy array
# print(data[0:27, :])
test_data_GZ = torch.from_numpy(test_data_GZ)


test_encoded_GZ_2D = []

for i in range(100000):
        x = test_data_GZ[i]
        x = x.float()

        # print(x)
        b_x = Variable(x.view(-1, 28*28))
        encoded, decoded = autoencoder_2D(b_x)  # 返回两个值
        test_encoded_GZ_2D.append(encoded.data.numpy())  # 收集压缩后的特征值
test_encoded_GZ_2D = np.vstack(test_encoded_GZ_2D)  # 将list类型转换为array

x_1 = []
y_1 = []
for i in range(100000):
    x, y = test_encoded_WS_2D[i]
    x_1.append(x)
    y_1.append(y)

plt.scatter(x_1, y_1, marker='+', color='r', label='WS')

x_2 = []
y_2 = []
for i in range(100000):
    x, y = test_encoded_BA_2D[i]
    x_2.append(x)
    y_2.append(y)

plt.scatter(x_2, y_2, marker='+', color='b', label='BA')


x_3 = []
y_3 = []
for i in range(100000):
    x, y = test_encoded_ER_2D[i]
    x_3.append(x)
    y_3.append(y)

plt.scatter(x_3, y_3, marker='+', color='g', label='ER')

x_4 = []
y_4 = []
for i in range(100000):
    x, y = test_encoded_GZ_2D[i]
    x_4.append(x)
    y_4.append(y)

plt.scatter(x_4, y_4, marker='+', color='c', label='GZ')

plt.title('Different Complex Network In AutoEncoder_NN ')
plt.legend()
plt.savefig('test_encoded_2D.pdf')
plt.show()
