class Casa:
    def __init__(self):
        self.partes = []
    
    def adicionar(self, parte):
        self.partes.append(parte)
    
    def mostrar(self):
        print(f"Casa construída com: {', '.join(self.partes)}")

class CasaBuilder:
    def __init__(self):
        self.casa = Casa()
    
    def construir_paredes(self):
        self.casa.adicionar("Paredes de Tijolo")
        return self
    
    def construir_telhado(self):
        self.casa.adicionar("Telhado Colonial")
        return self
    
    def construir_piscina(self):
        self.casa.adicionar("Piscina")
        return self
        
    def get_result(self):
        return self.casa


if __name__ == "__main__":
    
    builder = CasaBuilder()
    casa_luxo = builder.construir_paredes().construir_telhado().construir_piscina().get_result()
    
    print("Casa de Luxo:")
    casa_luxo.mostrar()

    builder2 = CasaBuilder()
    casa_simples = builder2.construir_paredes().construir_telhado().get_result()
    
    print("\nCasa Simples:")
    casa_simples.mostrar()