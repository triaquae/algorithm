#_*_coding:utf-8_*_
__author__ = 'Alex Li'
#
# 生活中的一个例子:
#     就拿汽车在路上行驶的来说。即有小汽车又有公共汽车，它们都不但能在市区中的公路上行驶，也能在高速公路上行驶。这你会发现，对于交通工具（汽车）有不同的类型，然而它们所行驶的环境（路）也在变化，在软件系统中就要适应两个方面的变化？怎样实现才能应对这种变化呢？
# 概述:
# 在软件系统中，某些类型由于自身的逻辑，它具有两个或多个维度的变化，那么如何应对这种“多维度的变化”？如何利用面向对象的技术来使得该类型能够轻松的沿着多个方向进行变化，而又不引入额外的复杂度？这就要使用Bridge模式。
# 意图:
# 　　　将抽象部分与实现部分分离，使它们都可以独立的变化。
#                                                                     ——《设计模式》GOF

# 效果及实现要点：
# 1．Bridge模式使用“对象间的组合关系”解耦了抽象和实现之间固有的绑定关系，使得抽象和实现可以沿着各自的维度来变化。
# 2．所谓抽象和实现沿着各自维度的变化，即“子类化”它们，得到各个子类之后，便可以任意它们，从而获得不同路上的不同汽车。
# 3．Bridge模式有时候类似于多继承方案，但是多继承方案往往违背了类的单一职责原则（即一个类只有一个变化的原因），复用性比较差。Bridge模式是比多继承方案更好的解决方法。
# 4．Bridge模式的应用一般在“两个非常强的变化维度”，有时候即使有两个变化的维度，但是某个方向的变化维度并不剧烈——换言之两个变化不会导致纵横交错的结果，并不一定要使用Bridge模式。
#
# 适用性：
#    在以下的情况下应当使用桥梁模式：
# 1．如果一个系统需要在构件的抽象化角色和具体化角色之间增加更多的灵活性，避免在两个层次之间建立静态的联系。
# 2．设计要求实现化角色的任何改变不应当影响客户端，或者说实现化角色的改变对客户端是完全透明的。
# 3．一个构件有多于一个的抽象化角色和实现化角色，系统需要它们之间进行动态耦合。
# 4．虽然在系统中使用继承是没有问题的，但是由于抽象化角色和具体化角色需要独立变化，设计要求需要独立管理这两者。
# 总结：
#       Bridge模式是一个非常有用的模式，也非常复杂，它很好的符合了开放-封闭原则和优先使用对象，而不是继承这两个面向对象原则


class AbstractRoad(object):
    '''公路基类'''
    car = None

class AbstractCar(object):
    '''车辆基类'''

    def run(self):
        pass

class People(object):
    pass


class Street(AbstractRoad):
    '''市区街道'''

    def run(self):
        self.car.run()
        print("在市区街道上行驶")

class SpeedWay(AbstractRoad):
    '''高速公路'''

    def run(self):
        self.car.run()
        print("在高速公路上行驶")


class Car(AbstractCar):
    '''小汽车'''
    def run(self):
        print("小汽车在")

class Bus(AbstractCar):
    '''公共汽车'''
    road = None

    def run(self):
        print("公共汽车在")



#加上人
class Man(People):
    def drive(self):
        print("男人开着")
        self.road.run()
#加上人
class Woman(People):
    def drive(self):
        print("女人开着")
        self.road.run()
if __name__ == "__main__":
    #小汽车在高速上行驶
    road1 = SpeedWay()
    road1.car = Car()
    road1.run()

    #
    road2 = SpeedWay()
    road2.car = Bus()
    road2.run()


    #人开车
    road3 = Street()
    road3.car = Car()

    p1 = Man()
    p1.road = road3
    p1.drive()