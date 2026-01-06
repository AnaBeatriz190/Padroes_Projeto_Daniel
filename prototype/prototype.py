import copy

class Ovelha:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.dna = "ATGC-SEQ-001"

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Ovelha [Nome: {self.nome}, Tipo: {self.tipo}, DNA: {self.dna}]"

if __name__ == "__main__":
    original = Ovelha("Dolly", "Merino")
    print(f"Original: {original}")

    clonada = original.clone()
    clonada.nome = "Dolly Clone"

    print(f"Clonada:  {clonada}")
    print(f"Original Intacta?: {original}")