from abc import ABC, abstractmethod

class EstadoCelular(ABC):
    @abstractmethod
    def apertar_botao_power(self, celular): pass

class TelaLigada(EstadoCelular):
    def apertar_botao_power(self, celular):
        print("Bloqueando tela...")
        celular.estado = TelaBloqueada()

class TelaBloqueada(EstadoCelular):
    def apertar_botao_power(self, celular):
        print("Ligando a tela...")
        celular.estado = TelaLigada()

class Celular:
    def __init__(self):
        self.estado = TelaBloqueada()
    
    def apertar_power(self):
        self.estado.apertar_botao_power(self)

if __name__ == "__main__":
    meu_celular = Celular()
    
    meu_celular.apertar_power()
    meu_celular.apertar_power()
    meu_celular.apertar_power()