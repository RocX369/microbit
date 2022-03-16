# Seven Segment - Common Cathode Driver
from microbit import *

pins = [pin0, pin1, pin2, pin8, pin13, pin14, pin15]
 
one = [pin1, pin2]
two = [pin0, pin1, pin8, pin13, pin15]
three = [pin0, pin1, pin2, pin8, pin15]
four = [pin1, pin2, pin14, pin15]
five = [pin0, pin2, pin8, pin14, pin15]
six = [pin0, pin8, pin2, pin13, pin14, pin15]
seven = [pin0, pin1, pin2]
eight = [pin0, pin1, pin2, pin8, pin13, pin14, pin15]
nine = [pin0, pin1, pin2, pin8, pin14, pin15]
zero = [pin0, pin1, pin2, pin8, pin13, pin14]

number = [one, two, three, four, five, six, seven, eight, nine, zero]

def clear():
   for i in pins:
    i.write_digital(0) 

def num(n):
    for i in n:
        i.write_digital(1)

for i in number:
   num(i)
   sleep(1000)
   clear()