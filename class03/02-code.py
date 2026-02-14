# Una Clase de Tipo Vehiculo
class Vehiculo:
    # Constructor de la Clase
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
    
    # Metodo encender
    def encender():
        print("enceder")

# Se creo un Objeto de Tipo Vehiculo
vehiculo1 = Vehiculo("mercedes", "2026", "v12")
vehiculo2 = Vehiculo("aston martin", "2025", "v10")
vehiculo3 = Vehiculo("cadillac", "2024", "v8")

# Imprimir vehiculos
print(vehiculo1.marca)
print(vehiculo2.marca)
print(vehiculo3.marca)
