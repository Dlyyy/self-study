def power(x,n=2):
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s

print(power(5, 3))
    
# 修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
# 新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：

# >>> power(5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: power() missing 1 required positional argument: 'n'
# Python的错误信息很明确：调用函数power()缺少了一个位置参数n。

# 这个时候，默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：

# 设置默认参数时，有几点要注意：

# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

# 二是如何设置默认参数。

# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。