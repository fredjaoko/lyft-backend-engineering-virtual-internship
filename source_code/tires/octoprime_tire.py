import numpy as np
from tires.tires import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear_array) -> None:
        self.tire_wear_array = tire_wear_array


    def needs_service(self):
        total_wear = sum(self.tire_wear_array)
        if total_wear >= 3:
            return True
        return False