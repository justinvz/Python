import math
import random
import time



class Robot:
    """Robot"""


    def __init__(self, x = 0, y = 0, oriant = 0):
        self.x = x
        self.y = y
        self.oriant = oriant

    def position(self):
        return self.x,self.y

    def orientation(self):
        return self.oriant

    def pose(self):
        return "x: %.2f  y: %.2f oriantation: %.2f" % (self.x, self.y, self.oriant)

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

def iniRobots(rList):
    k = -1
    row = 0

    for i in range(100):
        rList.append(i)
        rList[i] = Robot()
        rList[i].oriant = math.pi/2
        k += 1
        if (k == 10):
            row += 1
            k = 0
        rList[i].x = k*2
        rList[i].y = row*2

def random_pose(rList, x = 100):
    for i in range(x):
        rList[i].x = random.uniform(0,100)
        rList[i].y = random.uniform(0,100)
        #rList[i].oriant = random.uniform(0,2*math.pi)
    
def get_pose(rList):
    poseList = []
    for i in range(100):
        poseList.append(i)
        poseList[i] = rList[i].pose()
    return poseList

def random_oriant(rList):

    for i in range(100):
        rList[i].oriant = random.uniform(0,2*math.pi)


def shuffle_pose(rList):
    robo = 0
    print(robo)
    while(robo < 10):
        print("loop")
        random_pose(rList, 10)
        robo += 1
        time.sleep(1)

robots = []
iniRobots(robots)
#random_pose(robots)
#print(get_pose(robots))
#random_oriant(robots)   
shuffle_pose(robots)
