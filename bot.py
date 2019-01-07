#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import pyautogui as pygui
import time, PIL.ImageGrab, PIL.ImageOps, numpy

class Bot:

    def __init__(self):
        self.pyauto = pygui
        self.np = numpy
        self.grabimg = PIL
        self.coods=(643,431)
        self.obstacle=(430,460)
    
    def reply(self):
        time.sleep(3)
        auto = self.pyauto
        auto.click(self.coods)
    
    def grab_image(self):
        np = self.np
        
        grabber = self.grabimg
        front_box = (self.coods[0], self.coods[1], self.coods[0]+223,self.coods[1]+29)
        imgObj = grabber.ImageGrab.grab(front_box)
        cvt_gray = grabber.ImageOps.grayscale(imgObj)
        arr = np.array(cvt_gray)
        return arr.sum()


    def press_space(self):
        
        

        # listener = dina_bot.AI()


        a = self.pyauto
        img = self.grabimg




        for f in a.KEYBOARD_KEYS:
            print(f)
        # listener.listen()
        while True :
            shot = a.screenshot(imageFilename="screenshot.jpg", region=(0,0,623,185))

            print("[+] Image Object: ", shot)
            a.press('space')
            print("[+] Pressed Key: Space")





                                    
my_bot = Bot()
my_bot.press_space()


