def calc(*numbers):    #*number可变参数
    sum =0
    for n in numbers:
        sum=sum+n*n  
    return sum   

calc(1, 3, 5, 7)
    
# 可变参数 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。

# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：

# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# 但是调用的时候，需要先组装出一个list或tuple：

# >>> calc([1, 2, 3])
# 14
# >>> calc((1, 3, 5, 7))
# 84
# 如果利用可变参数，调用函数的方式可以简化成这样：

# >>> calc(1, 2, 3)
# 14
# >>> calc(1, 3, 5, 7)
# 84
# 所以，我们把函数的参数改为可变参数：

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：

# >>> calc(1, 2)
# 5
# >>> calc()
# 0
# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：

# >>> nums = [1, 2, 3]
# >>> calc(nums[0], nums[1], nums[2])
# 14
# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：

# >>> nums = [1, 2, 3]
# >>> calc(*nums)
# 14
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。