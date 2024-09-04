
from time import sleep
import sys

class check_vitals:
  def is_temperature_ok(self, temperature):
    if temperature in range(95, 102):
      self.print_wait_time()
      print('Temperature is normal')
      return True
    else:
      self.print_wait_time()
      print('Temperature critical!')
      return False

  def is_pulse_rate_ok(self, pulseRate):
    if pulseRate in range(60, 100):
      self.print_wait_time()
      print('Pulse Rate is normal')
      return True
    else:
      self.print_wait_time()
      print('Pulse Rate is out of range!')
      return False

  def is_spo2_ok(self, spo2):
    if spo2 < 90:
      self.print_wait_time()
      print('Oxygen level is normal')
      return True
    else:
      self.print_wait_time()
      print('Oxygen Saturation out of range!')
      return False

  def print_wait_time(self):
    for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)