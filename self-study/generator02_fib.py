def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
    
fib(6)
# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib1(6)
print(f)
# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，
# 遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
for n in fib1(6):
    print(n)
# 回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。

# 同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代：

# 但是用for循环调用generator时，发现拿不到generator的return语句
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：

g=fib1(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
    