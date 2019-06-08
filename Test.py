#!python2

import Leap
import sys
from keyboard import press_and_release
import threading
import pyautogui
from time import sleep
pyautogui.FAILSAFE = False
from os import getcwd

from inputs import get_gamepad, devices
from functions import *

running = True

buttons = {"BTN_SOUTH":"A","BTN_EAST":"B","BTN_NORTH":"Y","BTN_WEST":"X"}

#import lowlevelkeys

canvas_width = 1920
canvas_height = 1080

workDir = getcwd()




class ThetaListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connection Established."
        #controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.config.set("Gesture.Circle.MinRadius", 5.0)


        controller.config.set("Gesture.Swipe.MinLength", 150.0)
        controller.config.set("Gesture.Swipe.MinVelocity", 1000)
        controller.config.save()
        #controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        self.hasswiped = False
        self.flickUp = False
        self.flickDown = False
        self.mod1 = False
        self.mod2 = False
        self.mod3 = False
        self.pointUp = False


    def on_frame(self, controller):
        #print(self.hasswiped)
        frame = controller.frame()

        """
        i_box = frame.interaction_box
        front_finger = frame.fingers.frontmost
        normalized_position = i_box.normalize_point(front_finger.stabilized_tip_position)
        app_x = canvas_width * normalized_position.x
        app_y = canvas_height * (1
                                 - normalized_position.y)
        app_z = front_finger.touch_distance
        print app_x
        print app_y
        print app_z
        pyautogui.moveTo(app_x, app_y)
        if app_z < -0.3:
            pyautogui.click(app_x, app_y)
        print "\n"
        #paint(app_x,app_y, w)
        """
        rhand = frame.hands.rightmost
        rpitch = rhand.direction.pitch

        lhand = frame.hands.leftmost
        lpitch = lhand.direction.pitch


        #print(str(rpitch) + "\n" + str(lpitch) + "\n")
        #print(self.flickDown)



        # Manually calibrated values.
        normalmin = -0.4
        normalmax = 1.3

        lfingUp = lhand.fingers.frontmost.direction[1]
        #print lfingUp

        #"""
        left_finger_position = frame.fingers.frontmost.tip_position
        #print(left_finger_position[1])

        #print "Mod1: " + str(self.mod1)
        #print "Mod3: " + str(self.mod3)

        if left_finger_position[0] < 25 and left_finger_position[0] > -2 and not left_finger_position == Leap.Vector(0.0,0.0,0.0):
            self.mod2 = True
        else:
            self.mod2 = False
        #print(self.mod2)

        if left_finger_position[0] <= -120 and left_finger_position[1] >= 250:
            self.mod1 = True
            #print("mod2")
        else:
            self.mod1 = False

        """  
        if left_finger_position[0] <= -120 and left_finger_position[1] <= 100:
            self.mod3 = True
            #print("mod3")
        else:
            self.mod3 = False
        """


        #"""


        if lfingUp >= 0.6 and not self.pointUp and not lfingUp > 3:
            self.pointUp = True
            if self.mod2:
                print("Play/Pause")
                pausePlay()

        if lfingUp < 0.6 and not lfingUp == 0.0:
            self.pointUp = False


        #"""
        if rpitch >= normalmax and not self.flickUp and not rpitch > 2:
            self.flickUp = True
            print("Flicked Up")
            if self.mod1:
                lock()
        if rpitch < normalmax:
            self.flickUp = False

        if rpitch <= normalmin and not self.flickDown and not rpitch > 2:
            self.flickDown = True
            print("Flicked Down")
            if self.mod1:
                press_and_release("alt + f4")
            elif self.mod3:
                press_and_release("win + ctrl + right")
            else:
                press_and_release("alt + space")
                sleep(0.05)
                press_and_release("n")

        if rpitch > normalmin:
            self.flickDown = False
        #"""

        """
        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_CIRCLE:
                if gesture.state is Leap.Gesture.STATE_START:
                    circle = Leap.CircleGesture(gesture)
                    print("circle")

        """



        """
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = Leap.SwipeGesture(gesture)
                if swipe.state == Leap.Gesture.STATE_STOP and self.hasswiped == False:
                    print("Swiped")
                    press_and_release("alt + tab")
                    self.hasswiped = True
                if swipe.state != Leap.Gesture.STATE_STOP:
                    self.hasswiped = False
        """

def check(contr):
    while not contr.is_connected:
        sleep(1)
        if not contr.is_connected:
            print "Device not found, retrying..."
            continue


listener = ThetaListener()
controller = Leap.Controller()

def mainL():
    # Create a sample listener and controller

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Stop with enter."
    #"""

    checker = threading.Thread(target=check,args=(controller,))
    checker.start()

    while running:
        continue
    controller.remove_listener(listener)


    #"""

def mainG():
    while running:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Key":
                if event.state == 1:
                    print(buttons[event.code])



leapThread = threading.Thread(target=mainL)
gpadThread = threading.Thread(target=mainG)
threads = []; threads.append(leapThread); threads.append(gpadThread)
for thread in threads:
    thread.start()

while running:
    try:
        sys.stdin.readline()
    finally:
        print("Exiting...\nProvide gamepad input to quit.")
        running = False

for thread in threads:
    thread.join()



