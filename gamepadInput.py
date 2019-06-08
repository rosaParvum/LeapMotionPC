from inputs import get_gamepad
from time import time
import functions

buttons = {"BTN_SOUTH":"A","BTN_EAST":"B","BTN_NORTH":"Y","BTN_WEST":"X"}
combos = {
    "A A B B X Y A ": functions.adminConsole
}


def mainG():
    currentCombo = ""
    timestamps = []

    while True:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Key":
                if event.state == 1:
                    try:
                        if timestamps[-1] >= time() - 1:
                            currentCombo = currentCombo + buttons[event.code] + " "
                            timestamps.append(time())
                            print currentCombo
                            if currentCombo in combos.keys():
                                combos[currentCombo]()

                        else:
                            timestamps = []
                            currentCombo = buttons[event.code] + " "
                            timestamps.append(time())
                            print currentCombo

                    except IndexError:
                        currentCombo = buttons[event.code] + " "
                        timestamps.append(time())
                        print currentCombo

if __name__ == "__main__":
    mainG()