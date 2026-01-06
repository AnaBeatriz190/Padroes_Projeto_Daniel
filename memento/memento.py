class Memento:
    def __init__(self, estado):
        self._estado = estado
    
    def get_estado(self):
        return self._estado

class EditorTexto:
    def __init__(self):
        self._texto = ""

    def escrever(self, texto):
        self._texto = texto

    def salvar(self):
        return Memento(self._texto)

    def restaurar(self, memento):
        self._texto = memento.get_estado()

    def mostrar(self):
        print(f"Texto atual: '{self._texto}'")

if __name__ == "__main__":
    editor = EditorTexto()
    historico = []

    editor.escrever("Versão 1")
    historico.append(editor.salvar())

    editor.escrever("Versão 2 (com erro)")
    editor.mostrar()

    print("Desfazendo...")
    editor.restaurar(historico[0])
    editor.mostrar()