import math
class Circulo:
    _radio = 0.0

    def __init__(self, radio: float):
        self._radio = radio

    def area(self):
        return math.pi*self._radio**2

    def circunferencia(self):
        return 2*math.pi*self._radio