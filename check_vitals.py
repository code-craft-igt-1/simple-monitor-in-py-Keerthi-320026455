
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

def is_temperature_critical(temperature):
    """Checks if the temperature is outside the normal range."""
    return temperature > 102 or temperature < 95

def is_pulse_rate_out_of_range(pulseRate):
    """Checks if the pulse rate is outside the normal range."""
    return pulseRate < 60 or pulseRate > 100

def is_spo2_low(spo2):
    """Checks if the oxygen saturation is below the acceptable range."""
    return spo2 < 90

def vitals_ok(temperature, pulseRate, spo2):
    """Checks vital signs and provides warnings if out of range."""
    if is_temperature_critical(temperature):
        blink_warning('Temperature critical!')
        return False
    if is_pulse_rate_out_of_range(pulseRate):
        blink_warning('Pulse Rate is out of range!')
        return False
    if is_spo2_low(spo2):
        blink_warning('Oxygen Saturation out of range!')
        return False
    return True
