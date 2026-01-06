from abc import ABC, abstractmethod

class Dispositivo(ABC):
    @abstractmethod
    def ligar(self): pass
    @abstractmethod
    def desligar(self): pass
    @abstractmethod
    def set_volume(self, percent): pass

class TV(Dispositivo):
    def ligar(self): print("TV ligada")
    def desligar(self): print("TV desligada")
    def set_volume(self, percent): print(f"TV Volume: {percent}%")

class Radio(Dispositivo):
    def ligar(self): print("Rádio ligado")
    def desligar(self): print("Rádio desligado")
    def set_volume(self, percent): print(f"Rádio Volume: {percent}%")

class ControleRemoto:
    def __init__(self, dispositivo: Dispositivo):
        self.dispositivo = dispositivo
    
    def power(self):
        print("Botão Power pressionado.")
        self.dispositivo.ligar()

class ControleAvancado(ControleRemoto):
    def mutar(self):
        print("Botão Mute pressionado.")
        self.dispositivo.set_volume(0)

if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    controle_tv = ControleAvancado(tv)
    controle_tv.power()
    controle_tv.mutar()

    print("--- Trocando dispositivo ---")
    controle_radio = ControleRemoto(radio)
    controle_radio.power()