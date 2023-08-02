from car import Car
from abc import ABC


class Capulet_engine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000

class sternman_engine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on
    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False

class willoughby_engine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000