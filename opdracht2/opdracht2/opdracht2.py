class place:
    """een punt in 2d ruimte en orientatie in radiant.
    attributes: x, y, oriant
    """
    def __init__(self, x = 0, y = 0, oriant = 0):
        self.x = x
        self.y = y
        self.oriant = oriant

    def position(robot):
        print(robot.x,robot.y)
    def orientation(robot):
        print(robot.oriant)
    def pose(robot):
        print(robot.x,robot.y,robot.oriant)

    def foward(robot):
        robot.y += 1;

    def rotate():
        pass

    def change_pose():
        pass

    def reset_pose():
        pass




         
robot1 = place()
robot1.x = 5.0
robot1.y = 2.0
robot1.oriant = 3.14

robot1.pose()

