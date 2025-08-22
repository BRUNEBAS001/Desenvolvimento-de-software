class Carro:
    marca = "Genérica"
    modelo = "Padrão"

    __ano = 2020
    __valor = 50000.0

    def __init__(self, marca, modelo, ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.__ano = ano
        self.__valor = valor

    def __str__(self):
        return (f"Carro: {self.marca} {self.modelo}\n"
                f"Ano: {self.__ano}\n"
                f"Valor: R$ {self.__valor:,.2f}")

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor


carro1 = Carro("Toyota", "Corolla", 2022, 120000)
carro2 = Carro("Honda", "Civic", 2021, 115000)

print(carro1)
print(carro2)
