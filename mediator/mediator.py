class ChatMediator:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
        usuario.mediator = self

    def enviar_mensagem(self, mensagem, usuario_remetente):
        for usuario in self.usuarios:
            if usuario != usuario_remetente:
                usuario.receber(mensagem)

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.mediator = None

    def enviar(self, msg):
        print(f"{self.nome} enviou: {msg}")
        self.mediator.enviar_mensagem(msg, self)

    def receber(self, msg):
        print(f"{self.nome} recebeu: {msg}")

if __name__ == "__main__":
    chat = ChatMediator()

    joao = Usuario("João")
    maria = Usuario("Maria")
    pedro = Usuario("Pedro")

    chat.adicionar_usuario(joao)
    chat.adicionar_usuario(maria)
    chat.adicionar_usuario(pedro)

    joao.enviar("Olá pessoal!")