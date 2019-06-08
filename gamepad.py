from inputs import get_gamepad
from time import time

buttons = {"BTN_SOUTH":"A","BTN_EAST":"B","BTN_NORTH":"Y","BTN_WEST":"X"}


def mainG():


    while True:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Key":
                if event.state == 1:
                    print(buttons[event.code])

if __name__ == "__main__":
    mainG()
