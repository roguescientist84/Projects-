#Python Code for ADC output from analog input on the VERY user friendly Raspberry Pi Pico
#Python 3.4.0 
#MicroPython v1.15
#By Butch Dowdy. Feel free to use as you please

from machine import Pin, PWM
from time import sleep

 
#Activate PWM at GPIO 11, 
pwm = PWM(Pin(11))
pwm.freq(1000)


while True:
#Set input at GPIO 26 as analog (ADC)
    transducer = machine.ADC(26)        
    print(transducer.read_u16())
#set readout interval in seconds
    sleep(.1);

#Set PWM parameters for a kinda fast blink
#put 10000 / 60000 in range for a interesting pulse
    for duty in range(60000):
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(60000, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001);
        
        
        