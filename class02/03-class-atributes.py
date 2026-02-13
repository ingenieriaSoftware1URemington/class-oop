class Vehiculo:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor


vehiculo1 = Vehiculo("aston martin", "2026", "v12")
print(vehiculo1.marca)
