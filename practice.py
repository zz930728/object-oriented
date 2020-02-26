class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []

    def __str__(self):
        return ("户型: %s\n总面积: %.2f [剩余%.2f]\n家具: %s" %
                (self.house_type, self.free_area,
                 self.free_area, self.item_list))

    def add_item(self, item):

        # 家具的面积小于剩余面积  可以添加
        if item.area < self.free_area:
            self.free_area = self.free_area - item.area
            print("要添加 %s " % item.name)
            # 添加家具
            self.item_list.append(item.name)
        else:
            print("%s 的面积太大,无法添加 " % item.name)


bed = HouseItem("席梦思", 400)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

print()
print()
print()

# 创建房子对象
my_home = House("两室一厅", 120)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
print()
print()


# 枪类
class Gun:
    def __init__(self, model):
        """
        :param model: 枪的型号
        """
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了..." % self.model)
            return

        self.bullet_count -= 1
        print("[%s] 突突突突 [%d]" % (self.model, self.bullet_count))


# 士兵
class Soldier:
    # None 空对象
    def __init__(self, name):
        self.name = name

        # 新兵没有枪
        self.gun = None

    def fire(self):
        # 判断士兵有没有枪
        if self.gun is None:
            print("[%s] 还没有枪" % self.name)
            return

        # 装填子弹
        self.gun.add_bullet(50)

        self.gun.shoot()


ak47 = Gun("ak47")

xusanduo = Soldier("许三多")

xusanduo.gun = ak47
xusanduo.fire()

print()
print()

# print(xusanduo.gun)

# 身份运算符
# is / is not  is是判断引用是不是同一个 ==是判断两个值是否相同

# 私有属性 和私有方法
# 在属性和方法前加两个下划线 __
class Women:
    def __init__(self,name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 私有属性,可以访问对象的私有属性
        print("我的年龄是 %d" % self.__age)

xiaofang = Women("小芳")
# 私有属性,在外界是不能被直接访问的
# print(xiaofang.__age)
# 私有方法 在外界也是不能被访问的
# xiaofang.secret()
# 对象名._类名__属性名
print(xiaofang._Women__age)
xiaofang._Women__secret()
