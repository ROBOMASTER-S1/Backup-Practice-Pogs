import RPi.GPIO as GPIO
from time import sleep as wait

# Breadboard Metod:
# Actual GPIO Pinouts

red_leds=[11,13,15,19,21,23,29,31,33,35]

yellow_leds=[7,37]

RGB_led=[18,16,12]

RGB_mix=[[18,12],[18,16],[16,12]]

RGB_logic=[18,16,12,[18,16],
[18,12],[12,16],[18,16,12,16]]

hz=500 # LED dimmer herz value

led_speed=.1

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

for i in red_leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)
    
for i in RGB_led:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)
    
for i in yellow_leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)

def RGB_led_twinkle():
    
    for i in range(7):
        GPIO.output(RGB_logic[i],0)
        wait(led_speed)
        GPIO.output(RGB_logic[i],1)
        
    for i in range(5,-1,-1):
        GPIO.output(RGB_logic[i],0)
        wait(led_speed)
        GPIO.output(RGB_logic[i],1)
        
RGB_led_twinkle()