# 如果启动Python交互环境，再导入hello模块：

# $ python3
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import hello
# >>>
# 导入时，没有打印Hello, word!，因为没有执行test()函数。

# 调用hello.test()时，才能打印出Hello, word!：
import hello
hello.test()

# 直接在终端下面输入
# F:\PythonProject01>python hello.py mike
# Hello, mike!