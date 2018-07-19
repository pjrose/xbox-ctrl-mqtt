
import signal
import time
from xbox360controller import Xbox360Controller


def on_button_pressed(button):
    print('Button {0} was pressed'.format(button.name))



#    with Xbox360Controller() as controller:
#        controller.set_rumble(0.5, 0.5, 1000)
#        time.sleep(1)

def on_button_released(button):
    print('Button {0} was released'.format(button.name))


def on_axis_moved(axis):
    print('Axis {0} moved to {1} {2}'.format(axis.name, axis.x, axis.y))

try:
    with Xbox360Controller(0, axis_threshold=0.2) as controller:
        # Button A events
        controller.button_a.when_pressed = on_button_pressed
        controller.button_a.when_released = on_button_released
    
        controller.info()
        controller.set_led(Xbox360Controller.LED_ROTATE)
        time.sleep(1)
        controller.set_led(Xbox360Controller.LED_OFF)

        # Left and right axis move event
        controller.axis_l.when_moved = on_axis_moved
        controller.axis_r.when_moved = on_axis_moved

        signal.pause()
except KeyboardInterrupt:
    pass
