import math
from datetime import date
import random
import calendar

def findPositive():
    num = int(input("enter a num: "))
    if (num > 0):
        return "positive"
    elif(num < 0):
        return "negative"
    else:
        return "zero"

def add(a, b):
    return a + b

def power(base, exp=2):
    return base**exp

def even_odd(num):
    if(num%2 == 0):
        return "even"
    else:
        return "odd"

def slopee():
    x1 = int(input("enter x1: "))
    y1 = int(input("enter y1: "))
    x2 = int(input("enter x2: "))
    y2 = int(input("enter y2: "))
    slope = (y2 - y1)/(x2-x1)
    print("slope of the line is",slope(x1, x2, y1, y2))

def sqrt_sum():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    summ = a + b
    print("square root of the sum = ",math.sqrt(summ))

def gpa_calc():
    studentName = "xyz"
    m1 = random.uniform(0, 100)
    m2 = random.uniform(0, 100)
    m3 = random.uniform(0, 100)
    m4 = random.uniform(0, 100)
    m5 = random.uniform(0, 100)
    avg = (m1 + m2 + m3 + m4 + m5)/5
    gpa = (avg)/10
    
    print("Name: ", studentName)
    print(f"math: {m1:.2f}")
    print(f"physics: {m2:.2f}")
    print(f"chem: {m3:.2f}")
    print(f"cs: {m4:.2f}")
    print(f"english: {m5:.2f}")
    avg = (m1 + m2 + m3 + m4 + m5)/5
    print("avg = ", avg)
    print("gpa: ",gpa)

   
    gpa = (avg)/10

def daysAlive():

    y=int(input("Enter the year you were born in: "))
    m=int(input("Enter the month you were born in: "))    
    d=int(input("Enter the day you were born: "))

    dob=date(y,m,d)

    tdate=date(2025,9,7)

    daysalive=(tdate-dob).days

    print("Days alive: ",daysalive)

def vehicle():
    u = int(input("initial vel: "))
    a = int(input("acceleration: "))
    t = int(input("time: "))
    v = u + a*t
    s = u*t + (a*t*t)/2
    print("final vel: ", v)
    print("acceleration: ", a)

def calendarr():
    y=int(input("Enter year: "))
    m=int(input("Enter month: "))

    print("Calendar: ")
    print(calendar.month(y,m))

def binaryConversion():
    n  = int(input("enter a num: "))
    rem = []
    while(n > 0):
        rem.append(n%2)
        n = n//2    
    print(rem)

def lcmCalc():
    n1 = int(input("enter n1: "))
    n2 = int(input("enter n2: "))
    start = max(n1, n2)
    if(start%n1 == 0 and start%n2 == 0):
        lcm =  start
    else:
        lcm = n1*n2
    print("lcm = ", lcm)

def print_evenOdd():
    n1 = int(input("enter n1: "))
    n2 = int(input("enter n2: "))
    choice = input("even/odd/both: ")
    start = min(n1, n2)
    end = max(n1 ,n2)
    if choice == 'even':        
        for i in range (start, end+1):
            if(i%2 == 0):
                print(i)
            i = i + 1

    elif choice == 'odd':
        for i in range (start, end+1):
            if(i%2 == 1):
                print(i)
            i = i + 1

    elif choice == 'both':
        for i in range (start, end+1):
            print(i)
        i = i + 1

def sum_evenOdd():
    n1 = int(input("enter n1: "))
    n2 = int(input("enter n2: "))
    choice = input("sum of even/odd/both: ")
    start = min(n1, n2)
    end = max(n1 ,n2)
    sum = 0
    if choice == 'even':        
        for i in range (start, end+1):
            if(i%2 == 0):
                sum = sum + i
            i = i + 1
        print(sum)

    elif choice == 'odd':
        for i in range (start, end+1):
            if(i%2 == 1):
                sum = sum +i
                i = i + 1
        print(sum)

    elif choice == 'both':
        for i in range (start, end+1):
            sum = sum + i
            i = i + 1
        print(sum)
    

sum_evenOdd()
