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
