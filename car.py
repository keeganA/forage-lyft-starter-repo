from abc import ABC, abstractmethod
from serviceable import Servicable
# imports requrired for engine, battery and tyre?


class Car(ABC, Servicable):
    def __init__(self, engine, battery, tyre):
        self.engine = engine
        self.battery = battery
        self.tyre = tyre

    @abstractmethod
    def needs_service(self):
        if self.engine.needs_service or self.battery.needs_service() or self.tyre.needs_service():
            return True
