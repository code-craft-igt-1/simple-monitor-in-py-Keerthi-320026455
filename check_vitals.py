
from time import sleep
import sys

def blink_warning(message, blink_count=6, blink_interval=1):
    """Prints a blinking warning message."""
    print(message)
    for _ in range(blink_count):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(blink_interval)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(blink_interval)

def vitals_ok(temperature, pulseRate, spo2):
    """Checks vital signs and provides warnings if out of range."""
    if temperature > 102 or temperature < 95:
        blink_warning('Temperature critical!')
        return False
    elif pulseRate < 60 or pulseRate > 100:
        blink_warning('Pulse Rate is out of range!')
        return False
    elif spo2 < 90:
        blink_warning('Oxygen Saturation out of range!')
        return False
    return True