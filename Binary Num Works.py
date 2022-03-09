import time,RPi.GPIO as GPIO,drivers,threading
from datetime import datetime
from time import sleep as wait

# Breadboard Metod:
# Actual GPIO Pinouts

red_leds=[11,13,15,19,21,23,29,31,33,35]

green_power_led=22

yellow_leds=[7,37]

RGB_led=[18,16,12]

RGB_mix=[[18,12],[18,16],[16,12]]

RGB_logic=[18,16,12,[18,16],
[18,12],[12,16],[18,16,12,16]]

hz=500 # LED dimmer herz value

led_speed=.1

delay=30

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

# setup the button, while invoking the built-in
# Raspberry Pi 4 resistor for safe protection
# along with a 10K resistor for added protection.

GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_UP)

display=drivers.Lcd() # enable the LCD display
display.lcd_clear() # clear the LCD screen
display.lcd_backlight(1)

for i in red_leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)
    
for i in RGB_led:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)
    
for i in yellow_leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)
    
GPIO.setup(22,GPIO.OUT)

red_binary_leds=[13,15,19,21,23,29,31,33]


    
    

'''
for i in range(0,256):
    display.lcd_display_string(f'Binary: {i:b}',1)
    display.lcd_display_string(f'Hex: {i:X} Dec: {i:d}',2)
    wait(1)'''
