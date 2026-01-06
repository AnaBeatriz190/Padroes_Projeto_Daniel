class ColecaoCanais:
    def __init__(self):
        self.canais = ["Globo", "SBT", "Band", "Record"]

    def __iter__(self):
        self.indice = 0
        return self

    def __next__(self):
        if self.indice < len(self.canais):
            canal = self.canais[self.indice]
            self.indice += 1
            return canal
        else:
            raise StopIteration

if __name__ == "__main__":
    minha_tv = ColecaoCanais()

    for canal in minha_tv:
        print(f"Assistindo: {canal}")