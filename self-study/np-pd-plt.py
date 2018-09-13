import numpy as np
# c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]],dtype = ﬂoat)
# np.zeros((3,4))
# a = np.array([1,2,3])
# print(a[a<2])
# b = np.array([(1.5,2,3), (4,5,6)], dtype = ﬂoat)
# print(b[[1, 0, 1, 0],[0, 1, 2, 0]])

# h=a.view()

# h=a.copy()

# print(b.T)
# print(b.ravel())
# print(b.reshape(-1,2))

# e=np.full((2,2),7)
# f=np.eye(2)
# print(np.r_[e,f])
# print(np.hstack((e,f)))

import pandas as pd
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
# print(s)
data = {'Country': ['Belgium', 'India', 'Brazil'],
'Capital': ['Brussels', 'New Delhi', 'Brasília'],
'Population': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data,columns=['Country', 'Capital', 'Population'])
# print(df)
# print(df.ix[0,0])
# print(df.ix[0,'Country'])
# print(df.ix[0])
# print(df.ix[:,'Country'])

# from sqlalchemy import create_engine
# import pymysql
# engine = create_engine('mysql+pymysql://root:000000@localhost:3306/testdb')
# df1=pd.read_sql('SELECT * FROM tasks;', engine)
# print(df1)

# print(df.drop('Country',axis=1))
# print(df.sort_index())
# print(df.rank())
# print(df.sort_values(by='Country'))

# print(df.info)
# print(df.shape)
# print(df.columns)
# print(df.index)
# print(df.count())
# print(df.describe())
# print(df.sum())
# print(df.cumsum())

# f=lambda x:x*2
# print(df.apply(f))
# print(df.applymap(f))

import matplotlib.pyplot as plt
# s.plot()
# plt.show()
fig = plt.figure(num='test',figsize=(10,10))
ax=fig.add_subplot(223)
s.plot(marker='o',ls='--',color='red',linewidth=3)
ax.set(title='example',xlabel='X-axis',ylabel='Y-axis')
ax.legend('line',loc='best')
plt.tight_layout()
plt.show()

# print(s.where(s>0))
# print(df.index.duplicated())

