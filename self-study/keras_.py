#https://www.cnblogs.com/Anita9002/p/8136357.html
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
data = np.random.random((1000,100))
#numpy.random.randint(low,high=None,size=None,dtype) 
#生成在半开半闭区间[low,high)上离散均匀分布的整数值;若high=None，则取值区间变为[0,low) 
labels = np.random.randint(2,size=(1000,1)) #取0or1
model = Sequential()
model.add(Dense(32,activation='relu',input_dim=100)) #添加层 Dense就是常用的全连接层，所实现的运算是output = activation(dot(input, kernel)+bias)
model.add(Dense(1, activation='sigmoid')) #添加层
model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy']) #模型训练的BP模式设置
model.fit(data,labels,epochs=15,batch_size=32) #模型训练参数设置 + 训练
#model.evaluate(data, labels, batch_size=32, verbose=1, sample_weight=None)  #evaluate 模型评估
predictions = model.predict(data) #predict 模型评估
