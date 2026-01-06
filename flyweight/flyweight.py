import random

class TipoArvore:
    def __init__(self, nome, cor, textura):
        self.nome = nome
        self.cor = cor
        self.textura = textura
    
    def desenhar(self, x, y):
        print(f"Desenhando {self.nome} ({self.cor}) na posição [{x}, {y}]")

class FabricaArvores:
    _tipos = {}

    @staticmethod
    def get_tipo_arvore(nome, cor, textura):
        key = f"{nome}_{cor}"
        if key not in FabricaArvores._tipos:
            print(f"--> Criando novo tipo: {nome}")
            FabricaArvores._tipos[key] = TipoArvore(nome, cor, textura)
        return FabricaArvores._tipos[key]

class Arvore:
    def __init__(self, x, y, tipo: TipoArvore):
        self.x = x
        self.y = y
        self.tipo = tipo
    
    def desenhar(self):
        self.tipo.desenhar(self.x, self.y)

if __name__ == "__main__":
    floresta = []
    
    print("Plantando floresta...")
    for i in range(5):
        tipo = FabricaArvores.get_tipo_arvore("Pinheiro", "Verde", "TexturaPinheiro")
        floresta.append(Arvore(random.randint(0,100), random.randint(0,100), tipo))

    for i in range(5):
        tipo = FabricaArvores.get_tipo_arvore("Carvalho", "Marrom", "TexturaCarvalho")
        floresta.append(Arvore(random.randint(0,100), random.randint(0,100), tipo))
    
    print(f"\nTotal de árvores plantadas: {len(floresta)}")
    print(f"Total de objetos 'TipoArvore' na memória: {len(FabricaArvores._tipos)}")