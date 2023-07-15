""" x1=3 x2=7
    y1=2  y2=8"""

#without using function or class
import math
"""x1=3 
x2=7
y1=2
y2=8

x=x1-x2
y=y1-y2

x=x*x
y=y*y

z=x+y
res=math.sqrt(z)
print(res)"""

#using class and function

class cal_distance:
    x1=22
    x2=92
    y1=18
    y2=90
    def distance(self):
        x=self.x1-self.x2
        x=x*x
        y=self.y1-self.y2
        y=y*y
        return math.sqrt(x+y)
    

obj=cal_distance()
ans=obj.distance()
print(ans)     