from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

import numpy as np
from sklearn import svm
from sklearn import model_selection
import matplotlib.pyplot as plt
import matplotlib as mpl
import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import TensorDataset, DataLoader
from tqdm import tqdm

#=============== 数据准备 ===============
file_path = './testingBox/svm_test_data_2.txt'

# 该方法可将输入的字符串作为字典it 的键进行查询，输出对应的值
# 该方法就是相当于一个转换器，将数据中非浮点类型的字符串转化为浮点 -->edit point
def iris_type(s):
    it = {b'background':0, b'breath':1, b'abnormal':2}
    return it[s]

# 加载data文件，类型为浮点，分隔符为逗号，对第四列也就是data 中的鸢尾花类别这一列的字符串转换为0-2 的浮点数 -->edit point
data = np.loadtxt(file_path, dtype=float, delimiter='\t', converters={3:iris_type})  
# print(data)

# 对data 矩阵进行分割，从第四列包括第四列开始后续所有列进行拆分
x, y = np.split(data, (3,), axis=1)
# 对x 矩阵进行切片，所有行都取，但只取前两列 -->edit point
x = x[:, 0:2]
print(x)

# 随机分配训练数据和测试数据，随机数种子为1，测试数据占比为0.3
data_train, data_test, tag_train, tag_test = model_selection.train_test_split(x, y, random_state=1, test_size=0.5)

# X_train_t = torch.from_numpy(data_train).to(torch.float32).to("cuda")
# y_train_t = F.one_hot(torch.from_numpy(tag_train).to(torch.long)).squeeze(1).to("cuda")
# X_val_t = torch.from_numpy(data_test).to(torch.float32).to("cuda")
# y_val_t = F.one_hot(torch.from_numpy(tag_test).to(torch.long)).squeeze(1).to("cuda")

X_train_t = torch.from_numpy(data_train).to(torch.float32)
y_train_t = F.one_hot(torch.from_numpy(tag_train).to(torch.long)).squeeze(1)
X_val_t = torch.from_numpy(data_test).to(torch.float32)
y_val_t = F.one_hot(torch.from_numpy(tag_test).to(torch.long)).squeeze(1)
train_dataset = TensorDataset(X_train_t, y_train_t)
val_dataset = TensorDataset(X_val_t, y_val_t)
train_dataloader = DataLoader(train_dataset, batch_size=256,shuffle=True)
val_dataloader = DataLoader(val_dataset, batch_size=256,shuffle=False)


model = nn.Sequential(
    nn.Linear(2,8),
    nn.ReLU(),
    nn.Linear(8,16),
    nn.ReLU(),
    nn.Linear(16,32),
    nn.ReLU(),
    nn.Linear(32,64),
    nn.ReLU(),
    nn.Linear(64,64),
    nn.ReLU(),
    nn.Linear(64,128),
    nn.ReLU(),
    nn.Linear(128,3),
)


epoch = 10000
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_func = nn.CrossEntropyLoss()
pbar = tqdm(range(epoch))
for _ in pbar:
    acc_list = []
    for i,batch in enumerate(train_dataloader):
        x,y = batch
        output = model(x)
        loss = loss_func(output,y.float())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        acc = (output.max(1)[1] == torch.argmax(y, dim=1)).float().mean()
        acc_list.append(acc)
        pbar.set_postfix({"acc":acc.cpu().detach().item(), "loss":loss.cpu().detach().item()})

print(output)
print(batch)
        
print(f"train_acc: {torch.tensor(acc_list).mean():.4f}")

acc_list = []
for i,batch in enumerate(val_dataloader):
    x,y = batch
    output = model(x)
    loss = loss_func(output,y.float())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    acc = (output.max(1)[1] == torch.argmax(y, dim=1)).float().mean()
    acc_list.append(acc)
    pbar.set_postfix({"acc":acc.cpu().detach().item(), "loss":loss.cpu().detach().item()})

print(f"valid_acc: {torch.tensor(acc_list).mean():.4f}")