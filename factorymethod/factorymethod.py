from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass

class Caminhao(Transporte):
    def entregar(self):
        print("Entrega feita por terra em uma caixa")

class Navio(Transporte):
    def entregar(self):
        print("Entrega feita pelo mar em um container")

class Logistica(ABC):
    @abstractmethod
    def criar_transporte(self) -> Transporte:
        pass

    def planejar_entrega(self):
        transporte = self.criar_transporte()
        print("Logística: Iniciando processo...")
        transporte.entregar()

class LogisticaRodoviaria(Logistica):
    def criar_transporte(self) -> Transporte:
        return Caminhao()

class LogisticaMaritima(Logistica):
    def criar_transporte(self) -> Transporte:
        return Navio()

if __name__ == "__main__":
    print("--- Cliente escolhe Via Terrestre ---")
    app_logistica = LogisticaRodoviaria()
    app_logistica.planejar_entrega()

    print("\n--- Cliente escolhe Via Marítima ---")
    app_logistica = LogisticaMaritima()
    app_logistica.planejar_entrega()