class Singieton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # 如果没有cls._instance对象，就通过下面的方法得到一个实例对象
            cls._instance = super(Singieton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Myclass(Singieton):
    a = 1


mc1 = Myclass()

mc2 = Myclass()

mc3 = Myclass()

# 上面3个得到的结果是一样的，因为这个类只允许有一个实例对象



# 单例模式2 ：模块方式(在python中模块加载只会加载一遍)
# 实例化以后的对象不管导入多少次都是同一个

