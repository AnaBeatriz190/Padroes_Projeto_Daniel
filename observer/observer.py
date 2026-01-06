from abc import ABC, abstractmethod

class Inscrito(ABC):
    @abstractmethod
    def atualizar(self, video_titulo):
        pass

class InscritoEmail(Inscrito):
    def __init__(self, email):
        self.email = email
        
    def atualizar(self, video_titulo):
        print(f"E-mail para {self.email}: Saiu vídeo novo '{video_titulo}'")

class InscritoPushNotification(Inscrito):
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo

    def atualizar(self, video_titulo):
        print(f"Notificação no {self.dispositivo}: Corre pra assistir '{video_titulo}'")

class CanalYoutube:
    def __init__(self):
        self._inscritos = []
        self._novo_video = None

    def inscrever(self, inscrito: Inscrito):
        self._inscritos.append(inscrito)

    def desinscrever(self, inscrito: Inscrito):
        self._inscritos.remove(inscrito)

    def postar_video(self, titulo):
        self._novo_video = titulo
        print(f"\nCANAL: Postando vídeo '{titulo}'...")
        self._notificar_inscritos()

    def _notificar_inscritos(self):
        for inscrito in self._inscritos:
            inscrito.atualizar(self._novo_video)


if __name__ == "__main__":
    canal = CanalYoutube()

    joao = InscritoEmail("joao@email.com")
    maria = InscritoPushNotification("Celular da Maria")

    canal.inscrever(joao)
    canal.inscrever(maria)

    canal.postar_video("Aprenda Python em 5 minutos")

    canal.desinscrever(joao)
    canal.postar_video("Padrões de Projeto Explicados")