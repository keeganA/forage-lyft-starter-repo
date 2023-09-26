from datetime import datetime
from tyre import Tyre


class OctoprimeTyre(Tyre):
    def __init__(self, tyre_readings):
        self.tyre_readings = tyre_readings

    def needs_service(self):
        self.total_damage = 0
        for i in range(len(self.tyre_readings)):
            self.total_damage = self.total_damage + self.tyre_readings[i]
        if self.total_damage >= 3:
            return True
        else:
            return False
