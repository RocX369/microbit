# Max7219 8 x 7-Segment Display driver:
from microbit import *

# Communication pin setup
Din = pin
clk = pin
cs = pin

# Control data structures
X0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]      # No opperation : Handy when cascading
X9 = [0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]      # No Decoding (BCD code B)
XA = [0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,1]      # Brightness at +/- 50% duty cycle
XB = [0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0]      # Display digits 0-7
XC = [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1]      # Normal mode (No Shutdown)
XF = [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1]      # Display Test mode

D0 = [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]      # Data to Digit 0
D1 = [0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1]      # Data to Digit 1
D2 = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]      # Data to Digit 2
D3 = [0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1]      # Data to Digit 3
D4 = [0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1]      # Data to Digit 4
D5 = [0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1]      # Data to Digit 5
D6 = [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1]      # Data to Digit 6
D7 = [0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1]      # Data to Digit 7

# Constructor for Max7219 class object
class max7219:
    def __init__ max7219(self, XC, XB, XA, data):
        self.XC = XC
        self.XB = XB
        self.XA = XA
        self.data = [D0,D1,D2,D3,D4,D5,D6,D7]

# Timing : data(bit) into SR at HIGH of clk, cs must be LOW at this time
#          (cs HIGH after or on 16th clk(HIGH) to hold data in SR)
#          ( Data(Din) appear on Dout at clk(LOW) after 16th clk(HIGH)

    def run():
        cs.write_digital(0)                    # Select/enable Device for data reception
        for x in range(16):
            din.write_digital(self.XC[i])      # bit(data)   : Set device to NORMAL mode
            clk.write_digital(1)
            sleep(15)
            clk.write_digital(0)
        for x in range(16):
            din.write_digital(self.XB[i])      # bit(data)   : Set device Scan Limit to scan 0-7 Digits
            clk.write_digital(1)
            sleep(15)
            clk.write_digital(0)
        for x in range(16):
            din.write_digital(self.XA[i])      # bit(data)   : Set device Intensity = +/- 50% Duty cycle
            clk.write_digital(1)
            sleep(15)
            clk.write_digital(0)
        for x in range(16):
            din.write_digital(self.XB[i])      # bit(data)   : Write Data to Digit 
            clk.write_digital(1)
            sleep(15)
            clk.write_digital(0)


# Latch bit into SR
