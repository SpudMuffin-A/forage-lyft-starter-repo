from tires.tires import Tires

class Octoprime(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.tire_need_service = 3.0

    def needs_service(self):
        return sum(self.tire_wear) >= self.tire_need_service
