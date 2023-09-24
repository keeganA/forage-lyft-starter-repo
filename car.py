from abc import ABC, abstractmethod
from serviceable import Servicable


class Car(ABC, Servicable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass
