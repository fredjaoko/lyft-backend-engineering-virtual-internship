from tires.tires import Tire



class CarriganTire(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array


    def service_carrigan_tires(self):
        for wear in self.tire_wear_array:
            if wear >= 0.9:
                return True
        return False