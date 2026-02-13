class Vehiculo:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def encender(self):
        print(f"Estas encendido el vehiculo {self.marca}")

    def apagar(self):
        print(f"Estas apagando el vehiculo {self.marca}")


vehiculo1 = Vehiculo("aston martin", "2026", "v12")
vehiculo1.encender()

vehiculo2 = Vehiculo("Mercedes", "2025", "v8")
vehiculo2.encender()
vehiculo2.apagar()
