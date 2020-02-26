class Cat:

    def __init__(self, new_name):
        """
        对象的初始化方法
        定义一个类 指定类有哪些属性
        """
        print("这是一个初始化方法")
        # self.name = "Tom"
        self.name = new_name
        print("%s 来了" % self.name)
        pass

    # self 就是对象的引用
    def eat(self):
        print("%s小猫爱吃鱼" % self.name)
        # print("小猫爱吃鱼")

    def drink(self):
        print("%s要喝水" % self.name)
        # print("小猫要喝水")

    # 必须要有返回值 返回值必须为str 修改print方法的输出值
    def __str__(self):
        return "我是小猫[%s] " % self.name

    # 对象销毁 希望在销毁前 在干点事情
    def __del__(self):
        print("%s 我走了" % self.name)


# 创建对象
tom = Cat("懒猫")
# 类.属性名 可以创建属性 ===> 不推荐
# tom.name = "Tom"
tom.eat()
tom.drink()
# tom.name = "Tom"
print(tom)
# 在内存中删除一个对象 del 方法会调用 __del__ 方法
del tom
# tom.name = "Tom"
print("-" * 50)

# print(type(tom))
# print(tom)
#
# addr = id(tom)
# # %x 表示16进制输出
# # %d 表示10进制输出
# print("%x" % addr)
#
# print("%s" % tom)
print("---------------" * 50)


class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print("%s == %s" % (name, weight))

    def run(self):
        print("%s 跑步能减肥" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 吃东西能增总" % self.name)
        self.weight += 1

    def __str__(self):
        return "我的名字叫%s 体重是 %.2f" % (self.name, self.weight)


p = Person("小明", 75.0)
p.run()
p.eat()
print(p)
print("====>")

xiaomei = Person("小美", 45.0)
xiaomei.run()
xiaomei.eat()
print(xiaomei)
print(p)

