#!python2

import Leap
import sys
from keyboard import press_and_release
#import threading
import pyautogui
from time import sleep
pyautogui.FAILSAFE = False

canvas_width = 1920
canvas_height = 1080

w = None

class ThetaListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connection Established."
        controller.config.set("Gesture.Circle.MinRadius", 4.0)
        controller.config.set("Gesture.Circle.MinArc", 2)

        controller.config.set("Gesture.Swipe.MinLength", 150.0)
        controller.config.set("Gesture.Swipe.MinVelocity", 1000)
        controller.config.save()
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        self.hasswiped = False
        self.flickUp = False
        self.flickDown = False


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
        hand = frame.hands.rightmost
        pitch = hand.direction.pitch
        #print(pitch)
        #print(self.flickDown)

        #"""
        if pitch >= 1 and not self.flickUp and not pitch > 2:
            self.flickUp = True
            print("Flicked Up")
        if pitch < 1:
            self.flickUp = False

        if pitch <= -0.2 and not self.flickDown and not pitch > 2:
            self.flickDown = True
            print("Flicked Down")
            press_and_release("alt + space")
            sleep(0.05)
            press_and_release("n")
        if pitch > -0.2:
            self.flickDown = False
        #"""


        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_CIRCLE:
                print gesture.hands
                circle = Leap.CircleGesture(gesture)

                print("circle")



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


def main():
    # Create a sample listener and controller
    listener = ThetaListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Stop with enter."
    #"""
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        controller.remove_listener(listener)
    finally:
        controller.remove_listener(listener)
    #"""

main()