
from time import sleep
import sys

def blink_warning(message, blink_count=6, blink_interval=1):
    """Prints a blinking warning message."""
    print(message)
    for _ in range(blink_count):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(blink_interval)
        print('\r  ', end='')
        sys.stdout.flush()
        sleep(blink_interval)

def check_vital_sign(condition, message):
    """Checks a condition and blinks a warning if the condition is true."""
    if condition:
        blink_warning(message)
        return False
    return True

def vitals_ok(temperature, pulseRate, spo2):
    """Checks vital signs and provides warnings if out of range."""
    # Check each vital sign and combine results
    temperature_ok = check_vital_sign(temperature > 102 or temperature < 95, 'Temperature critical!')
    pulse_rate_ok = check_vital_sign(pulseRate < 60 or pulseRate > 100, 'Pulse Rate is out of range!')
    spo2_ok = check_vital_sign(spo2 < 90, 'Oxygen Saturation out of range!')

    return temperature_ok and pulse_rate_ok and spo2_ok