class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


# class Dog:
#     def eat(self):
#         print("吃")
#
#     def drink(self):
#         print("喝")
#
#     def run(self):
#         print("跑")
#
#     def sleep(self):
#         print("睡")
#
#     def bark(self):
#         print("汪汪叫")

# class 类名(父类名)
# class XiaoTianQuan(Dog):
#     def fly(self):
#         print("飞")

class Dog(Animal):

    def bark(self):
        print("旺旺叫")


class XiaoTianQuan(Dog):
    # 子类重写父类方法 在使用子类对象中被调用 会使用子类的方法 不调用父类的方法
    def eat(self):
        print("吃狗粮")

    def bark(self):
        print("神一样叫唤")

        # 同样super对象 进行扩展
        super().bark()
        print("/*/*/**q/*1/*12/*/1*2/21")

    def fly(self):
        print("我会飞")


class Cat(Animal):

    # 重写 定义一个和父类同样的方法
    def eat(self):
        print("吃猫粮")

    def catch(self):
        print("抓老鼠")


xtq = XiaoTianQuan()

xtq.eat()
xtq.drink()
xtq.run()
xtq.sleep()
xtq.bark()
xtq.fly()

print()

cat = Cat()
cat.eat()
print()

# class A:
#     def __init__(self):
#         # 成员变量
#         self.num1 = 100
#         # 私有变量
#         self.__num2 = 200
#
#     def __test(self):
#         print("私有方法 %d %d" % (self.num1, self.__num2))
#
#
# class B(A):
#     def demo(self):
#         # print("访问父类的私有属性%d" % self.__num2)
#         self.__test()
#     pass
#
#
# b = B()
# # print(b._A__num2)
# # b.demo()
# # 子类不能访问父类的私有方法
# b.demo()


# class A:
#     def __init__(self):
#         # 成员变量
#         self.num1 = 100
#         # 私有变量
#         self.num2 = 200
#
#     def test(self):
#         print("私有方法 %d %d" % (self.num1, self.__num2))
#
#
# class B(A):
#     def demo(self):
#         # print("访问父类的私有属性%d" % self.__num2)
#         self.__test()

"""
    创建出来的对象叫做类的实例
    创建对象的动作叫做实例化
    对象的属性叫做实例属性
    对象调动的方法叫做实例方法
    
    类 是 特殊的对象 
        程序运行时, 类会被加载到内存
        类是一个特殊的对象 -- 类对象
        类对象在内存中 只有一份 使用一个类可以创建出很多对象实例
        1.类属性
        2.类方法
    
    类名.对象属性
    对象名.对象属性
"""


class Tool(object):
    # 类属性
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    def __del__(self):
        Tool.count -= 1

    """
    @classmethod 表示一个类方法
    def 类方法名(cls):
        pass
    """

    @classmethod  # 类方法
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)

    @staticmethod
    def statit_method():
        pass


tool = Tool("斧头")
tool1 = Tool("榔头")
tool2 = Tool("水桶")
tool3 = Tool("菜刀")
tool3.count = 99

Tool.show_tool_count()
tool3.show_tool_count()

print(Tool.count)

print("=================> %d" % tool3.count)


class Person(object):
    @staticmethod
    def run():
        print("run")


Person.run()

"""
实例方法-- 方法内部需要访问实例属性
    实例方法 内部可以使用类名 访问类属性

类方法-- 方法内部 值访问类属性

静态方法-- 方法内部,不需要访问实例属性 和类属性
"""
class Game(object):
    # 最高分
    top_scope = 0

    def __init__(self, play_name):
        self.play_name = play_name

    @staticmethod
    def show_help():
        print("帮助菜单")

    @classmethod
    def show_top_score(cls):
        print("历史记录%d" % cls.top_scope)

    def start_game(self):
        print("%s 开始游戏..." % self.play_name)

Game.show_help()

Game.show_top_score()

g = Game("小名")
g.start_game()