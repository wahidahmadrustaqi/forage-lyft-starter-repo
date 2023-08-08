import unittest

from Tires.Carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire = [0.1, 0.3, 0.2, 0.9]
        tires = CarriganTires(tire)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire = [0.1, 0.2, 0.4, 0.2]
        tires = CarriganTires(tire)
        self.assertFalse(tires.needs_service())