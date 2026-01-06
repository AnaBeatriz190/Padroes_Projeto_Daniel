from abc import ABC, abstractmethod

class LampadaInteligente:
    def ligar(self):
        print("Lâmpada: Acesa! ")
    
    def desligar(self):
        print("Lâmpada: Apagada! ")

class Comando(ABC):
    @abstractmethod
    def executar(self):
        pass

class ComandoLigar(Comando):
    def __init__(self, lampada):
        self.lampada = lampada

    def executar(self):
        self.lampada.ligar()

class ComandoDesligar(Comando):
    def __init__(self, lampada):
        self.lampada = lampada

    def executar(self):
        self.lampada.desligar()

class ControleRemoto:
    def __init__(self):
        self.botao = None

    def definir_comando(self, comando):
        self.botao = comando

    def apertar_botao(self):
        print("Clicando no botão...")
        self.botao.executar()

if __name__ == "__main__":
    lampada = LampadaInteligente()
    
    ligar = ComandoLigar(lampada)
    desligar = ComandoDesligar(lampada)
    
    controle = ControleRemoto()

    controle.definir_comando(ligar)
    controle.apertar_botao()

    controle.definir_comando(desligar)
    controle.apertar_botao()