#_*_coding:utf-8_*_
__author__ = 'Alex Li'



class AbstractRoad(object):
    '''公路基类'''
    car = None

class AbstractCar(object):
    '''车辆基类'''

    def run(self):
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
    def run(self):
        print("公共汽车在")


if __name__ == "__main__":
    #小汽车在高速上行驶
    road1 = SpeedWay()
    road1.car = Car()
    road1.run()

    #
    road2 = SpeedWay()
    road2.car = Bus()
    road2.run()