'''
此函数利用自编码的神经网络来训练并分类以上数据和网络
'''
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
from create_data import output_train_WS
from AutoEncoder_NN import AutoEncoder_2D

# 生成数量为1000的小世界网络作为训练数据集
output_train_WS(100000, 28, 20)

# 超参数
EPOCH = 10
BATCH_SIZE = 1000
LR = 0.005

# 读取数据
# 利用pandas导入数据
train_data = pd.read_csv('Data/train_data_WS.txt', sep=',', header=None)
train_data = train_data.values  # 转换为numpy array
# print(data[0:27, :])
train_data = torch.from_numpy(train_data)

# 数据随机批量化
torch_dataset = Data.TensorDataset(data_tensor=train_data,
                                   target_tensor=train_data)

trian_loader = Data.DataLoader(
    dataset=torch_dataset,      # torch TensorDataset format
    batch_size=BATCH_SIZE,      # mini batch size
    shuffle=True,               # 要不要打乱数据 (打乱比较好)
    num_workers=10,              # 多线程来读数据
)


autoencoder_2D = AutoEncoder_2D()


# 对AutoEncoded_2D网络进行训练

optimizer_2D = torch.optim.SGD(autoencoder_2D.parameters(),
                               lr=0.01, momentum=0.9)  # 随机梯度下降算法
loss_func_2D = nn.MSELoss()  # 损失函数定义为最小二乘法

train_loss_2D = []
train_encoded_2D = []


# 此处将数据随机批量化进行训练
for epoch in range(EPOCH):
    for step, (x, y) in enumerate(trian_loader):
        x = x.float()

        # print(x)
        b_x = Variable(x.view(-1, 28*28))
        b_y = Variable(x.view(-1, 28*28))

        encoded, decoded = autoencoder_2D(b_x)  # 返回两个值

        train_encoded_2D.append(encoded.data.numpy())  # 收集压缩后的特征值
        loss = loss_func_2D(decoded, b_y)  # 计算损失
        # print(loss.data.numpy())
        train_loss_2D.append(loss.data.numpy())  # 收集损失函数
        optimizer_2D.zero_grad()  # 权值归零操作
        loss.backward()  # 反向传播
        optimizer_2D.step()

train_encoded_2D = np.vstack(train_encoded_2D)  # 将list类型转换为array


# 保存整个网络
torch.save(autoencoder_2D.state_dict(), 'AutoEncoder_2D.pkl')

# torch.save(AutoEncoder_2D, 'AutoEncoder_2D.pkl')

# 保存文件并清空内存
f1 = open("Data/train_loss_WS_2D.txt", "wb")  # 打开文件
f1.truncate()  # 清空文件
np.savetxt(f1, train_loss_2D, delimiter=",", fmt="%f")   # 保存loss数据
f1.close()  # 关闭文件

f2 = open("Data/train_encode_WS_2D.txt", "wb")  # 打开文件
f2.truncate()  # 清空文件
np.savetxt(f2, train_encoded_2D, delimiter=",", fmt="%f")  # 保存encoded数据
f2.close()  # 关闭文件

train_loss_2D = []
train_encoded_2D = []

# TODO 实际上将一个网络的矩阵作为一个图像也是可以的,然后利用卷积神经网络来处理
