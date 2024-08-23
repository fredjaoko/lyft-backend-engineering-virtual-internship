from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.Nubbin_battery import NubbinBattery
from battery.Spindler_battery import SpindlerBattery
from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire
from car import Car




class Create_Car():
    @staticmethod
    def create_calliope(current_mileage, last_service_date, last_service_mileage, tire_wear_array):
        Engine = CapuletEngine(current_mileage, last_service_mileage)
        Battery = SpindlerBattery(last_service_date)
        Tires = CarriganTire(tire_wear_array)
        car = Car(Battery, Engine, Tires)
        return car

    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        Battery = SpindlerBattery(last_service_date,)
        Tires = CarriganTire(tire_wear_array)
        car = Car(Battery, Engine, Tires)
        return car

    @staticmethod
    def create_palindrome(warning_light_indicator, last_service_date, tire_wear_array):
        Engine = SternmanEngine(warning_light_indicator)
        Battery = SpindlerBattery(last_service_date)
        Tires = OctoprimeTire(tire_wear_array)
        car = Car(Battery, Engine, Tires)
        return car

    @staticmethod
    def create_roschach(current_mileage, last_service_mileage,last_service_date, current_date, tire_wear_array ):
        Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        Battery = NubbinBattery(last_service_date, current_date)
        Tires = OctoprimeTire(tire_wear_array)
        car = Car(Battery,  Engine, Tires)
        return car

    @staticmethod
    def create_thovex(last_service_date, current_date, current_mileage, last_service_mileage, tire_wear_array):
        Engine = CapuletEngine(current_mileage, last_service_mileage)
        Battery = NubbinBattery(last_service_date, current_date)
        Tires = CarriganTire(tire_wear_array)
        car = Car(Battery, Engine, Tires)
        return car

