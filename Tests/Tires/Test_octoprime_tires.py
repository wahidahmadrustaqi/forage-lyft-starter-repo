import unittest

from Tires.Octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire = [0.8, 0.8, 0.8, 0.7]
        tires = OctoprimeTires(tire)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire = [0.1, 0.2, 0.4, 0.2]
        tires = OctoprimeTires(tire)
        self.assertFalse(tires.needs_service())