import math

#opdracht 1 python


uur = 3600
minuut = 60

#1.1
#input: uren, minuten en seconden output: seconden
def time(uren, minuten, seconden):
    tijd = (uren*uur) + (minuten*minuut) + (seconden)
    return ("aantal seconden: ", tijd)

#input: seconden output: uren minuten en seconden
def inv_time(tijd):
    uren = 0
    minuten = 0
    
    if(tijd >= uur): uren = tijd/uur
    tijd = tijd - int(uren)*uur

    if(tijd >= minuut): minuten = tijd/minuut
    tijd = tijd - int(minuten)* minuut
    
    return('Aantal uren: ', int(uren),"aantal minuten: ", int(minuten),"aantal seconden: ", tijd)


#print("inv_time ", inv_time(8000))
#print("time ", time(3,20,40))

#1.2
def rad2degree(rad):
    pi = math.pi
    degree = (rad/(2*pi))*360
    return degree

def degree2rad(degree):
    pi = math.pi
    rad = (degree/360)*(2*pi)
    return rad

#print(rad2degree(3.14))
#print(degree2rad(180))

def rpm2hz(rpm):
    hz = rpm/60
    return hz

def hz2rpm(hz):
    rpm = hz*60
    return rpm


#print(rpm2hz(60))
#print(hz2rpm(1))





#input is an quadratic formula like this: #ax^2 + bx + c.
#anwsers can be displayed in the real and complex domain.

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
    print("oplossing 1: ", x1, "oplossing 2:", x2)
    
quadraticSolve(1,0,5)

