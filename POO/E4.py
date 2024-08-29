class Vehiculo():
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_año(self):
        return self.__año

    def set_año(self, año):
        self.__año = año

    def detener(self):
        print(f"El vehículo {self.get_marca()} {self.get_modelo()} se está deteniendo.")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.__puertas = puertas

    def get_puertas(self):
        return self.__puertas

    def set_puertas(self, puertas):
        self.__puertas = puertas

    def acelerar(self):
        print(f"El auto {self.get_marca()} {self.get_modelo()} está acelerando.")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.__cilindrada = cilindrada

    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def acelerar(self):
        print(f"La moto {self.get_marca()} {self.get_modelo()} con cilindrada de {self.get_cilindrada()}cc está acelerando.")

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.__capacidad_carga = capacidad_carga

    def get_capacidad_carga(self):
        return self.__capacidad_carga

    def set_capacidad_carga(self, capacidad_carga):
        self.__capacidad_carga = capacidad_carga

    def acelerar(self):
        print(f"La camioneta {self.get_marca()} {self.get_modelo()} con capacidad de carga {self.get_capacidad_carga()} está acelerando.")

    def detener(self):
        print(f"La camioneta {self.get_marca()} {self.get_modelo()} se está deteniendo.")

if __name__ == "__main__":
    vehiculos = {
    "Camry": Auto("Toyota", "Camry", 2020, 4),
    "YZF-R3": Moto("Yamaha", "YZF-R3", 2019, 321),
    "Ranger": Camioneta("Ford", "Ranger", 2023, 1200)
    }

    for modelo, vehiculo in vehiculos.items():
        vehiculo.acelerar()