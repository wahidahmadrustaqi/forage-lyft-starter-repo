from battery import Nubbin_battery

import unittest
import datetime

class Test_Nubbin_battery(unittest.TestCase):
    def test_need_service_true(self):
        today = datetime.datetime(2023, 8, 7)
        last_service_date = datetime.datetime(2019, 8, 1)
        battery = Nubbin_battery(today, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_need_service_false(self):
        today = datetime.datetime(2023, 8, 7)
        last_service_date = datetime.datetime(2022, 8, 1)
        battery = Nubbin_battery(today, last_service_date)
        self.assertFalse(battery.needs_service())


