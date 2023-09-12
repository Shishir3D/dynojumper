import pyautogui
from PIL import Image
import serial  

def main():
    
    arduino = serial.Serial('COM3', 9600)  

    while True:
        screenshot = pyautogui.screenshot()
        pixel_color1 = screenshot.getpixel((423, 640))
        pixel_color2 = screenshot.getpixel((473, 640))
        pixel_color3 = screenshot.getpixel((523, 640))
        
        if pixel_color1==(83,83,83)or pixel_color2==(83,83,83)or pixel_color3 == (83,83,83):
            print("Black pixel detected!")
            arduino.write(b'1')             
        else:
            arduino.write(b'0')  


main()
