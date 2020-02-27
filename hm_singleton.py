"""
    单例设计模式
        目的 -- 让 类创建的对象,在系统中只有唯一的一个实例
        每一次执行类名() 返回的对象,内存地址是相同的

    __new__ 方法 内置的静态方法 作用:
        1.在内存中为对象分配空间
        2.返回 对象的引用

    __init__ 初始化方法
"""


class MusicPlayer(object):
    instance = None

    # 记录是否执行过初始化方法
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.创建对象时, __new__ 方法会自动被调用
        # print("创建对象,分配空间")
        # return MusicPlayer()
        # 2. 为对象分配空间(静态方法) 重写__new__ 方法
        # instance = super().__new__(cls)
        # 3. 返回对象的引用
        # return instance

        # 单例模式
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    # 创建几个对象,初始化(__init__) 就会调用几次
    def __init__(self):
        # 判断是否执行过初始化动作
        if MusicPlayer.init_flag :
            return

        # 没有执行,执行动作
        print("播放器初始化")

        # 修改标记
        MusicPlayer.init_flag =True

player = MusicPlayer()
print(player)

player1 = MusicPlayer()
print(player1)
