from abc import ABC, abstractmethod

class ArquivoComponente(ABC):
    @abstractmethod
    def mostrar(self, identacao=""): pass

class Arquivo(ArquivoComponente):
    def __init__(self, nome):
        self.nome = nome
    
    def mostrar(self, identacao=""):
        print(f"{identacao}- Arquivo: {self.nome}")

class Pasta(ArquivoComponente):
    def __init__(self, nome):
        self.nome = nome
        self.filhos = []
    
    def adicionar(self, componente):
        self.filhos.append(componente)
    
    def mostrar(self, identacao=""):
        print(f"{identacao}+ Pasta: {self.nome}")
        for filho in self.filhos:
            filho.mostrar(identacao + "  ")

if __name__ == "__main__":
    pasta_raiz = Pasta("Meus Documentos")
    pasta_trabalho = Pasta("Trabalho")
    
    arquivo1 = Arquivo("Curriculo.pdf")
    arquivo2 = Arquivo("Planilha.xls")
    arquivo3 = Arquivo("Foto_Familia.jpg")

    pasta_trabalho.adicionar(arquivo1)
    pasta_trabalho.adicionar(arquivo2)
    
    pasta_raiz.adicionar(pasta_trabalho)
    pasta_raiz.adicionar(arquivo3)

    pasta_raiz.mostrar()