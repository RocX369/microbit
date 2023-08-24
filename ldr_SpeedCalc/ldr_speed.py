from microbit import *

ldr1 = pino
ldr2 = pin1
led1 = pin8
led2 = pin12

distance = 40			# ldr sensors are 40cm appart
count = 0
start = 1

while True:
    if ldr1.read_analog() > 300:
        start = 1
    while sart == 1:
        sleep(10)
        count = count + 1
        if ldr2.read_analog() > 300:
            t = count/100
            start = 0
            break

speed = distance/t
print(speed)
#wihan