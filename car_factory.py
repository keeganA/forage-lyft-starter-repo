from datetime import datetime
from car import Car
from nubbin_battery import NubbinBattery
from spindler_battery import Spindlerbattery
from capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine
from carrigan_tyre import CarriganTyre
from octoprime_tyre import OctoprimeTyre


class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tyre_readings):
        tyre = CarriganTyre(tyre_readings)
        battery = Spindlerbattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        car = Car(engine, battery, tyre)
        return car

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tyre_readings):
        tyre = OctoprimeTyre(tyre_readings)
        battery = Spindlerbattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        car = Car(engine, battery, tyre)
        return car

    def create_palindrome(current_date, last_service_date, warning_light_on, tyre_readings):
        tyre = CarriganTyre(tyre_readings)
        battery = Spindlerbattery(last_service_date, current_date)
        engine = SternmanEngine(warning_light_on)
        car = Car(engine, battery, tyre)
        return car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tyre_readings):
        tyre = OctoprimeTyre(tyre_readings)
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        car = Car(engine, battery, tyre)
        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tyre_readings):
        tyre = CarriganTyre(tyre_readings)
        battery = Spindlerbattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        car = Car(engine, battery, tyre)
        return car
