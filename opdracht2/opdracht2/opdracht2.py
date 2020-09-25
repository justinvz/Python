import math


class robot:
    """Robot"""


    def __init__(self, x = 0, y = 0, oriant = 0):
        self.x = x
        self.y = y
        self.oriant = oriant

    def position(self):
        print(self.x,self.y)

    def orientation(self):
        print(self.oriant)

    def pose(self):
        print(round(self.x,2),round(self.y,2),round(self.oriant,2))

    def foward(self, distance):
        self.y += distance * math.sin(self.oriant)
        self.x += distance * math.cos(self.oriant)

    def rotate(self, radian):
        self.oriant += radian

    def change_pose(self,x,y,oriant):
        self.x = x;
        self.y = y;
        self.oriant = oriant;

    def reset_pose(self,x,y,oriant):
        self.x = x;
        self.y = y;
        self.oriant = oriant;
    
    def disbetween(self, robot):
        dx = self.x - robot.x
        dy = self.y - robot.y
        return (dx**2 + dy**2)**0.5


def distance(robot1, robot2):
    dx = robot1.x - robot2.x
    dy = robot1.y - robot2.y
    return (dx**2+dy**2)**0.5

for i in range(10):
    roboti = robot()
    print(i)


