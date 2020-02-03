#!/usr/bin/python3
from ina219 import INA219
from ina219 import DeviceRangeError
import os
import time
import threading

SHUNT_OHMS = 0.025
MAX_EXPECTED_AMPS = 1.0
ADDRESS = 0x40

class ina219_pi_seelab(object):
    def __init__(self, address=ADDRESS, shunt_ohms=SHUNT_OHMS,
                       max_expected_amps=MAX_EXPECTED_AMPS, filename=None):
        self.ina = INA219(shunt_ohms, max_expected_amps, address=address)
        self.ina.configure(self.ina.RANGE_16V)
        self.filename = filename
        self.f = None
        self.loop_thread = None
        self.interval = 0.0 # ms
        self.callback = None

    def log(self, str):
        if self.f is not None:
            self.f.write(str)
            self.f.write('\n')
        else:
            print(str)

    def read_power(self):
        return self.ina.power()

    def read_voltage(self):
        return self.ina.voltage()

    def read_current(self):
        return self.ina.current()

    def test_read(self):
        while True:
            print("Bus Voltage: %.3f V" % self.ina.voltage())
            try:
                print("Bus Current: %.3f mA" % self.ina.current())
                print("Power: %.3f mW" % self.ina.power())
                print("Shunt voltage: %.3f mV" % self.ina.shunt_voltage())
            except DeviceRangeError as e:
                # Current out of device range with specified shunt resister
                print(e)

