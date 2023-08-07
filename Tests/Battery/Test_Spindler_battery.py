from battery import Spindler_battery

import unittest
import datetime

class Test_Spindler_battery(unittest.TestCase):
    def test_need_service_true(self):
        today = datetime.datetime(2023, 8, 7)
        last_service_date = datetime.datetime(2021, 8, 1)
        battery = Spindler_battery(today, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_need_service_false(self):
        today = datetime.datetime(2023, 8, 7)
        last_service_date = datetime.datetime(2022, 8, 1)
        battery = Spindler_battery(today, last_service_date)
        self.assertFalse(battery.needs_service())