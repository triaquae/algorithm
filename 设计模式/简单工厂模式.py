#_*_coding:utf-8_*_
__author__ = 'Alex Li'


class Circle(object):
  def draw(self):
    print('draw circle')

class Rectangle(object):
  def draw(self):
    print('draw Rectangle')

class ShapeFactory(object):
  def create(self, shape):
    if shape == 'Circle':
      return Circle()
    elif shape == 'Rectangle':
      return Rectangle()
    else:
      return None

fac = ShapeFactory()
obj = fac.create('Circle')
obj.draw()