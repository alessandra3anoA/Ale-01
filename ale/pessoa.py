class Pessoa:
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf

if __name__ == '__main__':
     pessoa1 = Pessoa("João", "M", "123456")
     pessoa2 = Pessoa("Maria", "F", "45964")
print(pessoa1.nome,pessoa1.sexo,pessoa1.cpf)
print(pessoa2.nome,pessoa2.sexo,pessoa2.cpf)

def comer(self):
    return f"(self.nome) está comendo."

def beber(self):
    return f"(self.nome) está bebendo."

def falar(self):
    return f"(self.nome) está falando:(mensagem)"

def correr(self):
    return f"(self.nome) está correndo."