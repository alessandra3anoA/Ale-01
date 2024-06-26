class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def frear(self, distancia):
        print(f"{self.marca} {self.modelo} freou por {distancia} metros")
    def acelerar(self, velocidade):
        print(f"{self.marca} {self.modelo} acelerando para {velocidade} km/h")
class Veiculo:
    def __init__(self, marca):
        self.marca = marca

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca)
        self.modelo = modelo
        self.cor = cor
    def frear(self, distancia):
        print(f"{self.marca} {self.modelo} freou por {distancia} metros")
    def acelerar(self, velocidade):
        print(f"{self.marca} {self.modelo} acelerando para {velocidade} km/h")
if __name__=="__main__":
  carro1 = Carro(marca=input("Insira a marca: "), modelo=input("Insira o modelo: "), cor=input("Insira a cor do carro: "))
  z=input("Insira quantos quilometros você quer percorrer até parar: ")
  y=input("Insira a velocidade que você deseja alcançar: ")
carro1.frear(z)
carro1.acelerar(y)

class Veiculo:
    def __init__(self, marca):
        self.marca = marca

class Moto(Veiculo):
    def __init__(self, marca, cor, cilindada, enpinar):
        super().__init__(marca)
        self.cor = cor
        self.cilindada = cilindada
        self.enpinar = enpinar

    def empinar(self, vezes):
        print(f"A moto da marca {self.marca} empinou {vezes} vezes!")


if __name__=="__main__":
 marca = input("Insira a marca da moto: ")
 cor = input("Insira a cor da moto: ")
 cilindada = input("Insira a cilindrada da moto: ")
 enpinar = input("Insira a capacidade de empinar da moto: ")
 vezes_empinar = int(input("Quantas vezes a moto irá empinar? "))
moto1 = Moto(marca=marca, cor=cor, cilindada=cilindada, enpinar=enpinar)
moto1.empinar(vezes_empinar)
