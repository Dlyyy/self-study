def person(name, age, **kw):      #关键字参数
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
    
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
# 其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。