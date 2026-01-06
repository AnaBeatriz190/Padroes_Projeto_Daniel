class ProdutoComida:
    def __init__(self, preco):
        self.preco = preco
    
    def aceitar(self, visitor):
        return visitor.visitar_comida(self)

class ProdutoEletronico:
    def __init__(self, preco):
        self.preco = preco
    
    def aceitar(self, visitor):
        return visitor.visitar_eletronico(self)

class ImpostoVisitor:
    def visitar_comida(self, comida):
        imposto = comida.preco * 0.05
        print(f"Imposto Comida (5%): R${imposto}")
    
    def visitar_eletronico(self, eletronico):
        imposto = eletronico.preco * 0.20
        print(f"Imposto Eletrônico (20%): R${imposto}")

if __name__ == "__main__":
    carrinho = [ProdutoComida(10), ProdutoEletronico(100)]
    calculadora = ImpostoVisitor()

    for item in carrinho:
        item.aceitar(calculadora)