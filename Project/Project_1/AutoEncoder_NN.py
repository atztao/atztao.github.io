# 定义压缩为2D的自编码训练网络
import torch.nn as nn


class AutoEncoder_2D(nn.Module):
    def __init__(self):
        super(AutoEncoder_2D, self).__init__()

        # 压缩
        self.encoder = nn.Sequential(
            nn.Linear(28*28, 128),
            nn.Tanh(),
            nn.Linear(128, 64),
            nn.Tanh(),
            nn.Linear(64, 12),
            nn.Tanh(),
            nn.Linear(12, 2),  # 压缩成2D进行可视化
        )
        # 解压
        self.decoder = nn.Sequential(
            nn.Linear(2, 12),
            nn.Tanh(),
            nn.Linear(12, 64),
            nn.Tanh(),
            nn.Linear(64, 128),
            nn.Tanh(),
            nn.Linear(128, 28*28),
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded  # 此处返回encoded的值和decode的值,一个用来观察其特征,一个用来计算损失函数
