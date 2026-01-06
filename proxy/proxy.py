from abc import ABC, abstractmethod

class Internet(ABC):
    @abstractmethod
    def conectar(self, site): pass

class InternetReal(Internet):
    def conectar(self, site):
        print(f"Conectando ao site: {site}")

class ProxyInternet(Internet):
    def __init__(self):
        self.internet_real = InternetReal()
        self.sites_bloqueados = ["jogos.com", "virus.com"]

    def conectar(self, site):
        if site in self.sites_bloqueados:
            print(f"ACESSO NEGADO: O site '{site}' foi bloqueado pelo Proxy.")
        else:
            self.internet_real.conectar(site)

if __name__ == "__main__":
    internet = ProxyInternet()
    
    internet.conectar("google.com") 
    internet.conectar("jogos.com")  