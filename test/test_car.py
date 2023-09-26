import unittest
from datetime import datetime

from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from capulet_engine import CapuletEngine

from nubbin_battery import NubbinBattery
from spindler_battery import Spindlerbattery

from octoprime_tyre import OctoprimeTyre
from carrigan_tyre import CarriganTyre

# Engine Tests


class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage, last_service_mileage = 60001, 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage, last_service_mileage = 60000, 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage, last_service_mileage = 30001, 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage, last_service_mileage = 30000, 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


# Battery Tests
class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = today.replace(year=today.year - 4)
        today = datetime.today().date()
        battery = Spindlerbattery(
            last_service_date=last_service_date, current_date=today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        last_service_date = today.replace(year=today.year - 1)
        today = datetime.today().date()
        battery = Spindlerbattery(
            last_service_date=last_service_date, current_date=today)
        self.assertTrue(battery.needs_service())


class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()

        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(
            last_service_date=last_service_date, current_date=today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = NubbinBattery(
            last_service_date=last_service_date, current_date=today)
        self.assertFalse(battery.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        readings = [0.9, 0.9, 0.9, 0.9]
        tyre = OctoprimeTyre(readings)
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        readings = [0.1, 0.3, 0.4, 0.8]
        tyre = OctoprimeTyre(readings)
        self.assertFalse(tyre.needs_service())


class TestCarrigan(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        readings = [0.9, 0.9, 0.9, 0.9]
        tyre = CarriganTyre(readings)
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        readings = [0.1, 0.3, 0.4, 0.9]
        tyre = CarriganTyre(readings)
        self.assertFalse(tyre.needs_service())


if __name__ == '__main__':
    unittest.main()
