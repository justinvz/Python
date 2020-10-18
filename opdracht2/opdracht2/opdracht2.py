import math
import random
import time
import threading

import numpy as np
import matplotlib.pyplot as plt

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

    def change_pose(self,x,y,oriant): #Moet nog aangepast worden. houd geen rekening met de huidige oriantatie
        self.x += x;
        self.y += y;

    def reset_pose(self,x,y,oriant):
        self.x = x;
        self.y = y;
    
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

def random_pose(rList, x=0, y=100):
    for x in range(y):
        rList[x].x = int(random.uniform(0,20))
        rList[x].y = int(random.uniform(0,20))
        #rList[x].oriant = random.uniform(0,2*math.pi)
    
def get_pose(rList):
    poseList = []
    for i in range(100):
        poseList.append(i)
        poseList[i] = rList[i].pose()
    return poseList

def random_oriant(rList, x=0 , y=100):

    for x in range(y):
        rList[x].oriant = random.uniform(0,2*math.pi)

def shuffle_pose(rList, shuffles):
    robo = 0
    x = 0
    y = 0
    while(robo < shuffles):
        x = robo*5
        y = x + 5
        random_pose(rList, x, y)    
        random_oriant(rList, x, y)
        robo += 1
        time.sleep(1)
  
def update_array(robots):
    for i in range(100):
            robots_x[i] = robots[i].x
            robots_y[i] = robots[i].y
            robots_oriant[i] = robots[i].oriant



        #start counter

t = time.perf_counter()


        #creating list if robots

robots = []
iniRobots(robots)

robots_x = np.linspace(1,100,100)
robots_y = np.linspace(1,100,100)
robots_oriant = np.linspace(1,100,100)



        #threading the shuffle function so my program can run multiple thing at a time.
        #i rather thread the draw function (work in progres)

shuffleTime = 20

thread = threading.Thread(target=shuffle_pose, args=[robots, shuffleTime])

thread.start()

#------------------------ Plot(x,y,oriant)
#options. make a list of a list...
#dictionary

fig, ax = plt.subplots()
#label's
#ax.quiverkey(q, X=0.3, Y=1.1, U=1, label='Robots', labelpos='E')


while(t + shuffleTime > time.perf_counter()):

    update_array(robots)


    X = robots_x
    Y = np.array(robots_y)
    U = np.cos(np.array(robots_oriant))
    V = np.sin(np.array(robots_oriant))
    q = ax.quiver(X, Y, U, V)

    plt.draw()
    plt.pause(0.2)
    ax.cla()

 

robo_pose = np.array([[robots_x],[robots_y],[robots_oriant]]) 

robo_pose.mean(axis=0)

robo_pose.std(axis=0)



#Print posistions



#input("press something to exit...........")

print("ellepse time %f" % (time.perf_counter() - t))
    #plot robots & create numpy array's