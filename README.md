# microbit
microbit micropython device drivers
Developing microbit Micropython device drivers/libraries

1. GPIO (Digital and Analog)  - See Potentiometer folder.
   a. Reading values from analog sensor (10KΩ Potentiometer ; LDR )
       - Read the ADC(10bit) value from the 10KΩ potentiometer.
   b. If the reading is more than 50% of the total value of the potentiometer:
       - Switch on a LED (Digital), only when value > 50% of Pot value.
   c. Use the potentiometer to adjust the brightness of another LED connected via GPIO (Analog).
   d. Write a Python script that will display the following values in the shell window of Thonny:
       - Minimum Value.
       - Current Value.
       - Maximum Value.
   e. Add the following functionality to your code:
       - Use a button_a to reset the minimum value and Button_b to reset the maximum value.
   f. Now upgrade your project to display the values on a 1602_LCD_I2C display.

2. LDR Communication protocol.  -  See LDR Protocol folder.
   a. contruct a circuit consisting of a Microbit, LDR, and LED so that you can read and manipulate the circuit.
       - Your goal is to transfer the following message between two of these circuits: "Hello World".
   
