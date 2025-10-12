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
  