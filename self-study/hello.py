#使用模块

# Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。

# 我们以内建的sys模块为例，编写一个hello的模块：

'a test module'
__author__ = 'Dly'

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()


# 今天用Jenkins执行.py文件时，总是提示ModuleNotFoundError: No module named 'XXX'，百思不得其解。但是在PyCharm中却是能执行成功的，想了想然后在终端中运行该.py文件，仍然提示ModuleNotFoundError: No module named 'XXX' 。后面发现，在命令行中执行.py文件时找不到包是因为我们没有把项目路径保存，可通过sys.path.append()将你的项目路径保存，执行后就能成功，如下：


# import sys
# print(sys.path)
# import os
# #获取项目路径下的目录
# os.chdir('项目路径')
# #打印出项目路径下的目录
# for file in os.listdir(os.getcwd()):
#      print(file)
# #将项目路径保存
# sys.path.append('项目路径')
# 注意：如果要导入该项目其他模块的包名，应将导入的方法写在上面方法的后面，如下：
# import sys
# print(sys.path)
# import os
# os.chdir('/A／B／C')
# for file in os.listdir(os.getcwd()):
#      print(file)
# sys.path.append('/A／B／C')
# from C.XX import D
# 这时在终端中通过 python XX.py 才不会提示 ModuleNotFoundError: No module named ‘D’
class Hello(object):
    def hello(self,name='world'):
        print('Hello, %s'%name)