from tyre import Tyre


class CarriganTyre(Tyre):
    def __init__(self, tyre_readings):
        self.tyre_readings = tyre_readings

    def needs_service(self):
        for i in range(len(self.tyre_readings)):
            if self.tyre_readings[i] > 0.9:
                return True
        return False
