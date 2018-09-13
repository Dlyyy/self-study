#https://zhuanlan.zhihu.com/p/23310475?refer=c_56324009

#波形图
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(10000)
# y = np.sin(2*0.01*x)


# fig=plt.figure(figsize=(6,2.5))
# ax = fig.add_subplot(111)
# plt.plot(x,y,label='cosine')
# ax.set_xlim(0,10000)
# ax.set_ylim(-2,2)
# ax.set_xticks(np.linspace(0,10000,5)) 
# ax.set_yticks(np.linspace(-2,2,5))

# ax.set_xlabel('Times')
# ax.set_ylabel('Amplitude')

# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.legend(loc='upper left')

# plt.tight_layout()
# fig.set_size_inches(6,2.5)
# fig.savefig('first.png',dpi=1200)

# plt.show()

#直方图
# import numpy as np
# from numpy import arange
# import matplotlib.pyplot as plt

# import scipy.io as sio

# corr_m = [[0.8,0.4,0.7,0.65],[0.75,0.42,0.51,0.65],[0.45,0.91,0.34,0.51],[0.41,0.32,0.51,0.28],[0.12,0.32,0.25,0.41]]
# corr_m = np.array(corr_m)
# mean_corr_m = np.mean(corr_m,axis=1)



# N1,N2 = corr_m.shape
# index = np.arange(N1)+1

# ################################### Plot  ##############################
# mean_corr_m_sort_location1 = np.argsort(mean_corr_m)
# mean_corr_m_sort1 = np.sort(mean_corr_m)
# mean_corr_m_sort_location = mean_corr_m_sort_location1[::-1]
# mean_corr_m_sort = mean_corr_m_sort1[::-1]

# corr_m_sort = np.zeros([5,4])
# for i in range(N1):
#     corr_m_sort[i,:] = corr_m[mean_corr_m_sort_location[i],:]

# fig = plt.figure(figsize=(6,2.5))
# ax = fig.add_subplot(111)
# bar_width = 0.13
# opacity = 0.8
# rects1 = plt.bar(index, corr_m_sort[:,0], bar_width, alpha=opacity, color = 'b',label=    'Men') 
# rects2 = plt.bar(index+bar_width*1, corr_m_sort[:,1], bar_width, alpha=opacity, color = 'm')
# rects3 = plt.bar(index+bar_width*2, corr_m_sort[:,2], bar_width, alpha=opacity, color = 'g')
# rects4 = plt.bar(index+bar_width*3, corr_m_sort[:,3], bar_width, alpha=opacity, color = 'k')

# plt.plot(index+bar_width*3,mean_corr_m_sort[:],'ro-')

# ax.set_xlim(1,6)
# ax.set_ylim(0,1)

# ax.set_xticks(np.linspace(1,6,6))  
# ax.set_yticks(np.linspace(0,1,6))

# plt.xticks(index + 2*bar_width, ('1', '2', '3', '4', '5')) 
# plt.tight_layout()
# fig.set_size_inches(6,2.5)
# fig.savefig('fig19_a.png',dpi=1200)
# plt.show()


#三维画图、变换背景颜色、方向转换
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib.colors import colorConverter

import scipy.io as sio

t = np.linspace(0,10,2000)

z = np.zeros([5,2000])

for i in range(5):
    z[i,:] = np.sin(2*np.pi*t*(i+1)*0.2)
    
x = [np.linspace(0,9,5)]*2000
y = [np.linspace(0,1999,2000)]*5
x = np.array(x).T
y = np.array(y)

fig = plt.figure(figsize=(6,2.5))

ax = fig.gca(projection='3d')
plt.gca().patch.set_facecolor('white')


ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

for i in range(5):
    ax.plot(x[i,:],y[i,:],z[i,:])

ax.view_init(20,60)     
fig.set_size_inches(6, 2.5)
ax.set_ylim(0,3000)
ax.set_zticks(np.arange(-1,1.1,0.5))
ax.set_yticks([0,500,1000,1500,2000])
fig.savefig('fig6.png',dpi=1200)
plt.show()