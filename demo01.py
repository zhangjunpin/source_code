def func(fn):
    def inner():
        print('这是个什么函数')
        fn()
    return inner


@func
def abc():
    print('加入个什么呢')


abc()
