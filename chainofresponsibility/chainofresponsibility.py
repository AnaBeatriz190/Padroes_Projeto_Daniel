from abc import ABC, abstractmethod

class Suporte(ABC):
    def __init__(self):
        self.proximo = None

    def definir_proximo(self, proximo):
        self.proximo = proximo
        return proximo

    @abstractmethod
    def resolver(self, problema):
        pass

class RoboAtendimento(Suporte):
    def resolver(self, problema):
        if problema == "senha":
            print("Robô: Resetei sua senha automaticamente.")
        elif self.proximo:
            print("Robô: Não consigo resolver. Passando para Humano...")
            self.proximo.resolver(problema)
        else:
            print("Ninguém pode resolver isso.")

class HumanoAtendimento(Suporte):
    def resolver(self, problema):
        if problema == "reclamacao":
            print("Humano: Registrei sua reclamação no sistema.")
        elif self.proximo:
            print("Humano: Acima da minha alçada. Passando para Gerente...")
            self.proximo.resolver(problema)
        else:
            print("Ninguém pode resolver isso.")

class Gerente(Suporte):
    def resolver(self, problema):
        if problema == "processo":
            print("Gerente: Vamos tratar do processo jurídico.")
        else:
            print("Gerente: Infelizmente não temos solução para isso.")

if __name__ == "__main__":
    robo = RoboAtendimento()
    humano = HumanoAtendimento()
    gerente = Gerente()

    robo.definir_proximo(humano).definir_proximo(gerente)

    print("--- Cliente esqueceu a senha ---")
    robo.resolver("senha")

    print("\n--- Cliente quer processar ---")
    robo.resolver("processo")