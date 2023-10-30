"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
# LowFuelError исключение
class LowFuelError(Exception):
    """Исключение вызывается, кода отсутсвует топливо"""
    pass
# NotEnoughFuel исключение
class NotEnoughFuel(Exception):
    """Исключение вызывается, кода не достаточно топлива"""
    pass
# CargoOverload исключение
class CargoOverload(Exception):
    """Исключение вызывается, кода возникает перегрузка"""
    pass
