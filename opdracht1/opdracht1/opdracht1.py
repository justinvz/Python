import math
import operator as op

#opdracht 1 python
#Functions: use help(function) for examples

#1.1
#time(hours, minuts, seconds)
#inv_time(seconds)
#1.2
#rad2degree(radians)
#degree2rad(degrees)
#rpm2hz(rpm)
#hz2rpm(hertz)
#1.3
#quadraticSolve(a,b,c)
#truthTable(xor)
#fruitfullTruthTable(op.xor)
#derevative(function, x_value, deltaH)

#1.1s
def time(hours, minutes, seconds):
    """Input time(hour, minut, second) Output seconds"""
    hour = 3600
    minute = 60
    elapsedSec = (hours*hour) + (minutes*minute) + (seconds)
    return ("seconds: ", elapsedSec)

#input: seconden output: uren minuten en seconden
def inv_time(seconds):
    """Input inv_time(seconds) Outputs hours, minuts, seconds """
    hour = 3600
    minut = 60
    hours = 0
    minutes = 0
    if(seconds >= hour): hours = seconds/hour
    seconds = seconds - int(hours)*hour

    if(seconds >= minut): minutes = seconds/minut
    seconds = seconds - int(minutes)* minut
    
    return('hours: ', int(hours),"minutes: ", int(minutes),"seconds: ", seconds)

#1.2
#A
def rad2degree(rad):
    """Input radians, output Degree"""
    pi = math.pi
    degree = (rad/(2*pi))*360
    return degree

def degree2rad(degree):
    """Input degree radians, output radians"""
    pi = math.pi
    rad = (degree/360)*(2*pi)
    
    return rad
#B
def rpm2hz(rpm):
    """Input rpm, output hertz"""
    hz = rpm/60
    return hz

def hz2rpm(hz):
    """Input hertz, output rpm"""
    rpm = hz*60
    return rpm

#1.3
def quadraticSolve(a, b, c):
    """Solves a quadratic formula. expects a input of ax^2 + bx + c: quadraticSolve(a,b,c)"""
    D = (b**2 - (4 * a * c))

    if(D > 0):
        x1 = (-b + math.sqrt(D))/(2 * a)
        x2 = (-b - math.sqrt(D))/(2 * a)
    elif(D < 0):
        x1 = complex((-b/(2 * a)), ((math.sqrt(abs(D)))/(2 * a)))
        x2 = complex((-b/(2 * a)), - ((math.sqrt(abs(D)))/(2 * a)))
    elif(D == 0):
        x1 = x2 = (-b / (2 * a))

    print("discriminante: ", D)
    print("solution 1: ", x1, "Solution 2:", x2)
#1.4
#A & B
def truthTable(x):
    """Inputs a logic operator en outputs the truth table of it. 'and' 'or' 'xor' """
    if x == "and":
        print("A     | B    |",x)
        print("False | False|",op.and_(False,False))
        print("True  | False|",op.and_(True,False))
        print("False | True |",op.and_(False,True))
        print("True  | True |",op.and_(True,True))
        
    if x == "or":
        print("A     | B    |",x)
        print("False | False|",op.or_(False,False))
        print("True  | False|",op.or_(True,False))
        print("False | True |",op.or_(False,True))
        print("True  | True |",op.or_(True,True))
        
    if x == "xor":
        print("A     | B    |",x)
        print("False | False|",op.xor(False,False))
        print("True  | False|",op.xor(True,False))
        print("False | True |",op.xor(False,True))
        print("True  | True |",op.xor(True,True))

def trippleAnd(a, b, c):
    if a and b and c:
        return True
    else:
        return False

def trippleOr(a,b,c):
    if a or b or c:
        return True
    else:
        return False

def trippleXor(a,b,c):
    if a == b == c:
        return False
    else:
        return True
#1,4 C & D
def fruitfullTruthTable(logicOperator, argument):
    """"Input is a logic operator, outputs the truth table fruitfullTruthTable(Logicoperator, arguments). argument = 2: and_, or_, xor argument = 3: trippleAnd, trippleOr, trippleXor """
    if argument == 2:
        ff = False,False,logicOperator(False,False)
        tf = True,False,logicOperator(True,False)
        ft = False,True,logicOperator(False,True)
        tt = True,True,logicOperator(True,True)
        return ff,tf,ft,tt
    elif argument == 3:
        fff = False,False, False,logicOperator(False,False,False)
        tff = True,False, False,logicOperator(True,False,False)
        ftf = False,True, False,logicOperator(False,True,False)
        ttf = True,True, False,logicOperator(True,True,False)
        fft = False,False, True,logicOperator(False,False,True)
        tft = True,False, True,logicOperator(True,False,True)
        ftt = False,True, True,logicOperator(False,True,True)
        ttt = True,True, True,logicOperator(True,True,True)
        return fff,tff,ftf,ttf,fft,tft,ftt,ttt
#1.5
#A
def derevative(function,x,h= 1e-12):
    """"Differentiat the given function. derevative(function, x value, delta h) """
    d = (function(x) - function(x-h))/h
    return d
#B F(x)  = F(x−h) + ∆F(x)
def euler_backward_deltaF(function,x,h=1e-6):
    return function(x)*h


def intergral(function,x1,x2,h=1e-6,deltaF = euler_backward_deltaF):
    
    
    deltaF(function,x2)


    return 0
#1.6
