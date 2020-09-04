import math
import operator as op

#opdracht 1 python
#Functions: use help(function) 
#1.1
#time()
#inv_time()
#1.2
#rad2degree()
#degree2rad()
#rpm2hz()
#hz2rpm()
#1.3
#quadraticSolve()
#truthTable()

#1.1
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



#f(x) = (f(x) - f(x-h))/h when lim h -> 0

def derevative(function,x,h= 1e-10):
    
    d = (function(x) - function(x-h))/h

    
    print("input: ", function(x))
    print("output: ", d)


