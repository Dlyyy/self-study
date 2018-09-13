def person(name, age, *, city='Beijing', job):   #命名关键字参数
    print(name, age, city, job)
person('Jack', 24, job='Engineer')

#由于命名关键字参数city具有默认值，调用时，可不传入city参数：
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，
# Python解释器将无法识别位置参数和命名关键字参数：

# def person(name, age, city, job):
#     # 缺少 *，city和job被视为位置参数
#     pass