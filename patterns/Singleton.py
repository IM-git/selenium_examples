#Method 1
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# class MyClass(metaclass=Singleton):
#     pass
#
#
# x = MyClass()
# y = MyClass()
#
# print(x)
# print(y)

# Method 2
# class Foo(object):
#     pass
#
#
# some_global_variable = Foo()
#
# x = some_global_variable
# y = some_global_variable
#
# print(x)
# print(y)
