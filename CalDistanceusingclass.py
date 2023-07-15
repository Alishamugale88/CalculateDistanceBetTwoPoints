#using class and function
import math

"""class cal_distance:
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
print(ans) """

class cal_distance:
    def distance(self,x1,x2,y1,y2):
        x=x1-x2
        x=x*x
        y=y1-y2
        y=y*y
        return math.sqrt(x+y)
    
obj=cal_distance()
ans=obj.distance(4,5,3,5)
print(f"Distance between points is {ans}")    


