'''
此程序在于可视化训练过程中的损失函数和最终的分类
'''
import matplotlib.pyplot as plt
import pandas as pd

train_loss_WS_2D = pd.read_csv('Data/train_loss_WS_2D.txt',
                               sep=',', header=None)  # 利用pandas导入数据
train_loss_WS_2D = train_loss_WS_2D.values  # 转换为numpy array

train_enconded_WS_2D = pd.read_csv('Data/train_encode_2D.txt',
                                   sep=',', header=None)  # 利用pandas导入数据
train_enconded_WS_2D = train_enconded_WS_2D.values  # 转换为numpy array

plt.plot(train_loss_WS_2D, color='b', label='Train_Loss')
plt.legend()
# plt.title('Train Loss For Train WS')
plt.savefig('train_loss_WS_2D.pdf')
plt.show()

x_1 = []
y_1 = []
for i in range(100000):
    x, y = train_enconded_WS_2D[i]
    x_1.append(x)
    y_1.append(y)

plt.scatter(x_1, y_1, marker='+', color='b', label='Train_Data_WS_2D')
plt.legend()
# plt.title('Train_Enconded_WS_2D')
plt.savefig('train_enconded_WS_2D.pdf')
plt.show()
