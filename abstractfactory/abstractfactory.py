from abc import ABC, abstractmethod

class Cadeira(ABC):
    @abstractmethod
    def sentar(self): pass

class Sofa(ABC):
    @abstractmethod
    def deitar(self): pass

class CadeiraVitoriana(Cadeira):
    def sentar(self): print("Sentando em uma cadeira vitoriana luxuosa.")

class SofaVitoriano(Sofa):
    def deitar(self): print("Deitando em um sofá vitoriano de veludo.")

class CadeiraModerna(Cadeira):
    def sentar(self): print("Sentando em uma cadeira moderna minimalista.")

class SofaModerno(Sofa):
    def deitar(self): print("Deitando em um sofá moderno simples.")

class FabricaMoveis(ABC):
    @abstractmethod
    def criar_cadeira(self) -> Cadeira: pass
    @abstractmethod
    def criar_sofa(self) -> Sofa: pass

class FabricaVitoriana(FabricaMoveis):
    def criar_cadeira(self): return CadeiraVitoriana()
    def criar_sofa(self): return SofaVitoriano()

class FabricaModerna(FabricaMoveis):
    def criar_cadeira(self): return CadeiraModerna()
    def criar_sofa(self): return SofaModerno()

def cliente(fabrica: FabricaMoveis):
    cadeira = fabrica.criar_cadeira()
    sofa = fabrica.criar_sofa()
    cadeira.sentar()
    sofa.deitar()

if __name__ == "__main__":
    print("--- Cliente quer móveis modernos ---")
    cliente(FabricaModerna())
    
    print("\n--- Cliente quer móveis vitorianos ---")
    cliente(FabricaVitoriana())