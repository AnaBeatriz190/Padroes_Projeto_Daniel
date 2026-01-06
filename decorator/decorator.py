from abc import ABC, abstractmethod

class Bebida(ABC):
    @abstractmethod
    def custo(self):
        pass
    
    @abstractmethod
    def descricao(self):
        pass

class CafeSimples(Bebida):
    def custo(self):
        return 5.0
    
    def descricao(self):
        return "Café"

class AdicionalDecorator(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida 

    @abstractmethod
    def custo(self):
        pass

class Leite(AdicionalDecorator):
    def custo(self):
        return self.bebida.custo() + 2.0
    
    def descricao(self):
        return self.bebida.descricao() + ", Leite"

class Chocolate(AdicionalDecorator):
    def custo(self):
        return self.bebida.custo() + 3.5
    
    def descricao(self):
        return self.bebida.descricao() + ", Chocolate"

if __name__ == "__main__":

    meu_cafe = CafeSimples()
    print(f"{meu_cafe.descricao()} custa R${meu_cafe.custo()}")

    meu_cafe = Leite(meu_cafe)
    print(f"{meu_cafe.descricao()} custa R${meu_cafe.custo()}")

    meu_cafe = Chocolate(meu_cafe)
    print(f"{meu_cafe.descricao()} custa R${meu_cafe.custo()}")