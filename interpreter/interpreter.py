class Numero:
    def __init__(self, valor):
        self.valor = valor
    
    def interpretar(self):
        return self.valor

class Soma:
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
    
    def interpretar(self):
        return self.esquerda.interpretar() + self.direita.interpretar()

class Subtracao:
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
    
    def interpretar(self):
        return self.esquerda.interpretar() - self.direita.interpretar()

if __name__ == "__main__":
    expressao = Soma(Numero(10), Subtracao(Numero(5), Numero(2)))
    
    resultado = expressao.interpretar()
    print(f"Resultado de '10 + (5 - 2)': {resultado}")