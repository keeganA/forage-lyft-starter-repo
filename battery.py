from datetime import datetime
from battery import Battery
from abc import ABC, abstractmethod


class battery(ABC):
    @abstractmethod
    def needs_service():
        pass


nubbin_battery.py
