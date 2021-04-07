import cv2 as cv
import numpy as np
import math
from time import perf_counter as counter

prevTime = counter()

class ObjectDetection():
    class Tangram():
       def __init__(self):
        self.centerX = None
        self.centerY = None
        self.orientation = None
    
    redTriangle = Tangram()
    blueTriangle = Tangram()
    greenTriangle = Tangram()
    whiteTriangle = Tangram()
    orangeTriangle = Tangram()
    purpleParl = Tangram()
    yellowSquare = Tangram()

    def __init__(self):
        self.frame = None
        self.debug_frame = None
        self.hsv = None
        self.contours = None
        
        self.blueMask = None
        self.yellowMask = None
        self.greenMask = None
        self.purpleMask = None
        self.whiteMask = None
        self.orangeMask = None 
        self.redMask = None

    def videoCapture(self):
        _, frame = cap.read()
        self.frame = frame
        self.debug_frame = frame.copy()
            
    def draw_debug(self, contour, cx, cy, object, collor=(255,0,255), thick = 4):
        cv.drawContours(self.debug_frame, contour,-1,collor,thick)
        cv.putText(self.debug_frame, object, (cx-35,cy+65), cv.FONT_HERSHEY_SIMPLEX, 0.60, collor, thick-2)
        cv.circle(self.debug_frame, (cx,cy), thick, collor,-1)

    def show_debug(self):
        cv.imshow("Debug", self.debug_frame)
        cv.imshow("Original", self.frame)
        # cv.imshow("greenMask", self.greenMask)
        # cv.imshow("yellowMask", self.yellowMask)
        # cv.imshow("blueMask", self.blueMask)
        # cv.imshow("orangeMask", self.orangeMask)
        # cv.imshow("PurpleMask", self.purpleMask)
        # cv.imshow("WhiteMask", self.whiteMask)
        cv.imshow("Red Mask",self.redMask)

    def calibrate(self):

        def nothing(x):
            pass

        cv.namedWindow('marking')
        cv.createTrackbar('H Lower','marking',0,255,nothing)
        cv.createTrackbar('H Higher','marking',255,255,nothing)
        cv.createTrackbar('S Lower','marking',0,255,nothing)
        cv.createTrackbar('S Higher','marking',255,255,nothing)
        cv.createTrackbar('V Lower','marking',0,255,nothing)
        cv.createTrackbar('V Higher','marking',255,255,nothing)
    
        while True:
            object_Detection.videoCapture()
            self.hsv = cv.cvtColor(self.frame, cv.COLOR_BGR2HSV)
            hL = cv.getTrackbarPos('H Lower','marking')
            hH = cv.getTrackbarPos('H Higher','marking')
            sL = cv.getTrackbarPos('S Lower','marking')
            sH = cv.getTrackbarPos('S Higher','marking')
            vL = cv.getTrackbarPos('V Lower','marking')
            vH = cv.getTrackbarPos('V Higher','marking')
            LowerRegion = np.array([hL,sL,vL],np.uint8)
            upperRegion = np.array([hH,sH,vH],np.uint8)
            redObject = cv.inRange(self.hsv,LowerRegion,upperRegion)
            kernal = np.ones((1,1),"uint8")
            red = cv.morphologyEx(redObject,cv.MORPH_OPEN,kernal)
            red = cv.dilate(red,kernal,iterations=1)
            res1=cv.bitwise_and(self.frame, self.frame,mask=red)
            cv.imshow("Test thershold",res1)
        
            key = cv.waitKey(1)
            if key == 27: #press esc to exit
                break
        cap.release()
        cv.destroyAllWindows()
        
    def create_masks(self,Hl,Hu,Sl,Su,Vl,Vu):
        lower = np.array([(Hl),Sl,Vl])
        upper= np.array([(Hu), Su, Vu])
        mask = cv.inRange(self.hsv, lower, upper)
        return mask   
   
    def get_masks(self, blurKernal=(5,5)):

        blur = cv.GaussianBlur(self.frame, blurKernal, 0)
        self.hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
        kernel = np.ones((5,5), np.uint8)
        
        self.blueMask = self.create_masks(85,115,100,255,0,255)
        self.purpleMask = self.create_masks(114,165,58,255,0,255)
        self.yellowMask = self.create_masks(15,65,50,255,180,255)
        self.greenMask = self.create_masks(32,90,86,255,0,255)
        self.purpleMask = self.create_masks(109,139,106,211,83,170)
        self.whiteMask = self.create_masks(0,255,0,14,255,255)
        self.orangeMask = self.create_masks(0,10,90,160,0,255)
        self.redMask = cv.bitwise_or(self.create_masks(160,255,150,255,0,255),self.create_masks(0,5,150,255,0,255))

    def get_contours(self,mask):
        self.contours, h = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    
    def get_oriantation(self,approx,cx,cy):
        p1 = approx[0][0]
        p2 = approx[1][0]
        p3 = approx[2][0]
        if(len(approx)==3): 
            v1 = p1-p2
            v2 = p1-p3
            mv1 = np.linalg.norm(v1)
            mv2 = np.linalg.norm(v2)
            if mv1 > mv2:
                pTop = p3
            else:
                pTop = p2
        if(len(approx) == 4):
            p4 = approx[3][0]
            if(p1[0]>cx and p1[1]<cy):
                pTop = p1
            elif(p2[0]>cx and p2[1]<cy):
                pTop = p2    
            elif(p3[0]>cx and p3[1]<cy):
                pTop = p3
            elif(p4[0]>cx and p4[1]<cy):
                pTop = p4
            else:
                pTop = cx,cy
        # cv.circle(self.debug_frame,tuple(pTop), 6,(0,0,255) ,-1)
        # cv.line(self.debug_frame,(cx,cy), tuple(pTop),(0,0,255))
        orientation = np.arctan2(pTop[1]-cy, pTop[0]-cx)
        orientation = int(-np.degrees(orientation))
        # print(f"top point traingle = {pTop} midpoint = {cx,cy} orientation = {orientation}")
        return orientation
    
    def get_shape(self,mask,collor,epsilon_factor=0.02, maxArea=300):
        self.get_contours(mask)
        global prevTime
        for contour in self.contours:
            area = cv.contourArea(contour)

            if area > maxArea:  #Change value if objects are bigger or smaller
                approx = cv.approxPolyDP(contour,epsilon_factor*cv.arcLength(contour, True),True)
                M = cv.moments(approx)

                if(M['m00'] == 0):
                    M['m00'] = 0.0001
                
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00']) 

                if len(approx) == 3:
                    prevTime = counter()
                    orientation = self.get_oriantation(approx, cx,cy)    
                    self.draw_debug(contour, cx, cy, collor+" Triangle " + str(orientation))
                    if(collor == "Green"):
                        self.greenTriangle.centerX = cx
                        self.greenTriangle.centerY = cy
                        self.greenTriangle.orientation = orientation
                    if(collor == "Red"):
                        self.redTriangle.centerX = cx
                        self.redTriangle.centerY = cy
                        self.redTriangle.orientation = orientation
                    if(collor == "Orange"):
                        self.orangeTriangle.centerX = cx
                        self.orangeTriangle.centerY = cy
                        self.orangeTriangle.orientation = orientation
                    if(collor == "White"):
                        self.whiteTriangle.centerX = cx
                        self.whiteTriangle.centerY = cy
                        self.whiteTriangle.orientation = orientation
                    if(collor == "Blue"):
                        self.blueTriangle.centerX = cx
                        self.blueTriangle.centerY = cy
                        self.blueTriangle.orientation = orientation

                elif len(approx) == 4:
                    prevTime = counter()
                    orientation = self.get_oriantation(approx, cx,cy)  
                    if(collor == "Yellow"):
                        self.draw_debug(contour, cx,cy, collor+" Square "+str(orientation))
                        self.yellowSquare.centerX = cx
                        self.yellowSquare.centerY = cy
                        self.yellowSquare.orientation = orientation
                    if(collor == "Purple"):
                        self.draw_debug(contour, cx,cy, collor+" parl "+str(orientation))
                        self.purpleParl.centerX = cx
                        self.purpleParl.centerY = cy
                        self.purpleParl.orientation = orientation

        else: #if no object is detected for 0.1 seconds, set all value's to 0
            
            if(counter()- prevTime) > 0.1:
                self.greenTriangle.centerX = 0
                self.greenTriangle.centerY = 0
                self.greenTriangle.orientation = 0

                self.blueTriangle.centerX = 0
                self.blueTriangle.centerY = 0
                self.blueTriangle.orientation = 0
                
                self.orangeTriangle.centerX = 0
                self.orangeTriangle.centerY = 0
                self.orangeTriangle.orientation = 0

                self.whiteTriangle.centerX = 0
                self.whiteTriangle.centerY = 0
                self.whiteTriangle.orientation = 0

                self.blueTriangle.centerX = 0
                self.blueTriangle.centerY = 0
                self.blueTriangle.orientation = 0

                self.yellowSquare.centerX = 0
                self.yellowSquare.centerY = 0
                self.yellowSquare.orientation = 0
                                
                self.purpleParl.centerX = 0
                self.purpleParl.centerY = 0
                self.purpleParl.orientation = 0

    def get_object(self):
        self.get_masks()
        self.get_shape(self.greenMask,"Green")
        self.get_shape(self.yellowMask, "Yellow")
        self.get_shape(self.blueMask,"Blue")
        self.get_shape(self.purpleMask,"Purple")
        self.get_shape(self.orangeMask,"Orange")
        self.get_shape(self.whiteMask,"White")
        self.get_shape(self.redMask, "Red")
  
    def send_object(self):
        msg = [self.greenTriangle.centerX, self.greenTriangle.centerY, self.greenTriangle.orientation,
        self.redTriangle.centerX, self.redTriangle.centerY, self.redTriangle.orientation,
        self.blueTriangle.centerX, self.blueTriangle.centerY, self.blueTriangle.orientation,
        self.orangeTriangle.centerX, self.orangeTriangle.centerY, self.orangeTriangle.orientation,
        self.whiteTriangle.centerX, self.whiteTriangle.centerY, self.whiteTriangle.orientation,
        self.yellowSquare.centerX, self.yellowSquare.centerY, self.yellowSquare.orientation,
        self.purpleParl.centerX, self.purpleParl.centerY, self.purpleParl.orientation]
        
    def print_objects(self):

        print(f"YellowSquare: X: {self.yellowSquare.centerX} Y: {self.yellowSquare.centerY}")
        # print(f"greenTriangle:{self.greenTriangle.centerX,self.greenTriangle.centerY}")

cap = cv.VideoCapture(0)
#cap.set(3,width)
#cap.set(4,hight)
print(f"Starting computer vision system resolution: {cap.get(3)} x {cap.get(4)}")

object_Detection = ObjectDetection()

calibrate = False

if(calibrate):
    object_Detection.calibrate()

while True:
    object_Detection.videoCapture()
    object_Detection.get_object()
    object_Detection.send_object()
    object_Detection.show_debug()

    key = cv.waitKey(1)
    if key == 27: #press esc to exit
        break

cap.release()
cv.destroyAllWindows()




 