class Amplificador:
    def ligar(self): print("Amplificador ligado")
    def volume(self, nivel): print(f"Amplificador volume: {nivel}")

class Projetor:
    def ligar(self): print("Projetor ligado")
    def modo_wide(self): print("Projetor em modo Widescreen")

class Luzes:
    def desligar(self): print("Luzes da sala desligadas")

class Pipoqueira:
    def estourar(self): print("Pipoqueira estourando milho!")

class HomeTheaterFacade:
    def __init__(self, amp, proj, luz, pipoca):
        self.amp = amp
        self.proj = proj
        self.luz = luz
        self.pipoca = pipoca

    def assistir_filme(self):
        print("\n--- Preparando para assistir filme ---")
        self.pipoca.estourar()
        self.luz.desligar()
        self.proj.ligar()
        self.proj.modo_wide()
        self.amp.ligar()
        self.amp.volume(10)
        print("--- Tudo pronto! Bom filme! ---")

if __name__ == "__main__":
    home_theater = HomeTheaterFacade(Amplificador(), Projetor(), Luzes(), Pipoqueira())
    
    home_theater.assistir_filme()