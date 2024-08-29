class Vehiculo():
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def detener(self):
        print(f"El vehículo {self.get_marca()} {self.get_modelo()} se está deteniendo.")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.__puertas = puertas

    def detener(self):
        print(f"El auto {self.get_marca()} {self.get_modelo()} se está deteniendo.")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.__cilindrada = cilindrada

    def detener(self):
        print(f"La moto {self.get_marca()} {self.get_modelo()} se está deteniendo.")

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.__capacidad_carga = capacidad_carga

    def detener(self):
        print(f"La camioneta {self.get_marca()} {self.get_modelo()} se está deteniendo.")

if __name__ == "__main__":
    vehiculos = {
    "Camry": Auto("Toyota", "Camry", 2020, 4),
    "YZF-R3": Moto("Yamaha", "YZF-R3", 2019, 321),
    "Ranger": Camioneta("Ford", "Ranger", 2023, 1200)
    }


    for modelo, vehiculo in vehiculos.items():
        vehiculo.detener()