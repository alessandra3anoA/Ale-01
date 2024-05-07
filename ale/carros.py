class Carro:
   def __init__(self, placa, modelo, ano):
      self.placa = placa
      self.modelo = modelo
      self.ano = ano

if __name__=="__main__":
     palio = Carro("kjb-2668","edx","1997")
     vectra = Carro("kir-0932","elite","2008")
     duster = Carro("oyw-4108","dynamic","2015")
print(palio.placa,vectra.placa,duster.placa)