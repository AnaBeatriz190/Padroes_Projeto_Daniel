class FornoAntigo:
    def ligar_tomada_dois_pinos(self):
        print("Forno: Plugando na tomada de dois pinos. Aquecendo...")

class TomadaTresPinosPadrao:
    def ligar_tres_pinos(self):
        pass

class AdaptadorTomada(TomadaTresPinosPadrao):
    def __init__(self, forno_antigo):
        self.forno = forno_antigo

    def ligar_tres_pinos(self):
        print("Adaptador: Convertendo 3 pinos para 2 pinos...")
        self.forno.ligar_tomada_dois_pinos()

if __name__ == "__main__":
    forno_velho = FornoAntigo()

    adaptador = AdaptadorTomada(forno_velho)
    
    print("Usuário: Tentando plugar o forno...")
    adaptador.ligar_tres_pinos()