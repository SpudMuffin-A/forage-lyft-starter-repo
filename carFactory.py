from car import Car

from battery.battery_types.spindler import Spindler
from battery.battery_types.nubbin import Nubbin

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tires.tire_types.carrigan import Carrigan
from tires.tire_types.octoprime import Octoprime


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tires = Carrigan(tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tires = Octoprime(tire_wear)
        car = Car(engine, battery, tires)
        return car    

    @staticmethod
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = SternmanEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tires = Carrigan(tire_wear)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tires = Octoprime(tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = SternmanEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tires = Octoprime(tire_wear)
        car = Car(engine, battery, tires)
        return car
