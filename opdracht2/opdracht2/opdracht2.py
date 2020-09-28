import math


class Robot:
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
        print("x: %.2f  y: %.2f oriantation: %.2f" %self.x, self.y, self.oriant)

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

def iniRobots(list):
    k = -1
    row = 0

    for i in range(100):
        list.append(i)
        list[i] = Robot()
        list[i].oriant = math.pi/2
        k += 1
        if (k == 10):
            row += 1
            k = 0
        list[i].x = k*2
        list[i].y = row*2

robots = []
iniRobots(robots)


