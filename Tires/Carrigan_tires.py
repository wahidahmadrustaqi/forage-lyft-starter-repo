from Tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire):
        self.tire = tire

    def needs_service(self):
        for tire in self.tire:
            if tire >= 0.9:
                return True
        return False