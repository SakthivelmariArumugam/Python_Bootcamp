import math
class Problem1:
  def __init__(self,coor1,coor2):
    self.coor1=coor1
    self.coor2=coor2
  
  def distance(self):
    print(math.sqrt((self.coor2[0]-self.coor1[0])**2+(self.coor2[1]-self.coor1[1])**2))
  
  def slope(self):
    print((self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0]))


p1=Problem1((3,2),(8,10))
p1.distance()
p1.slope()

class Cylinder:
  def __init__(self,height=1,radius=1):
    self.height=height
    self.radius=radius
  
  def volume(self):
    print(2*math.pi*self.radius*self.radius)
  
  def surface_area(self):
    print((2*math.pi*self.radius*(self.radius+self.height)))

c1=Cylinder(2,3)
c1.volume()
c1.surface_area()