from Tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire):
        self.tire = tire

    def needs_service(self):
        return sum(self.tire) >= 3.0