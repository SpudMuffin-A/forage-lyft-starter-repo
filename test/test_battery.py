import unittest
import datetime

from battery.battery_types.nubbin import Nubbin
from battery.battery_types.spindler import Spindler

class TestNubbinBattery(unittest.TestCase):
    def battery_needs_service(self):
        current_date = datetime.datetime.now()
        last_service_date = datetime.datetime(2019, 1, 8)
        battery = Nubbin(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def battery_does_not_need_service(self):
        current_date = datetime.datetime.now()
        last_service_date = datetime.datetime(2021, 1, 8)
        battery = Nubbin(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def battery_needs_service(self):
        current_date = datetime.datetime.now()
        last_service_date = datetime.datetime(2019, 1, 8)
        battery = Spindler(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def battery_does_not_need_service(self):
        current_date = datetime.datetime.now()
        last_service_date = datetime.datetime(2021, 1, 8)
        battery = Spindler(current_date, last_service_date)
        self.assertFalse(battery.needs_service())