from microbit import *

ldr1 = pin0
ldr2 = pin1
led1 = pin8
led2 = pin12

distance = 40			# ldr sensors are 40cm appart
count = 0
start = 1

while True:
    val_1 = ldr1.read_analog()
    if ldr1.read_analog() > 400:
        start = 1
    while start == 1:
        sleep(10)
        count = count + 1
        if ldr2.read_analog() > 400:
            t = count/100
            start = 0
            break
    print(val_1)
    
speed = distance/t
print(val_1)
#wihan