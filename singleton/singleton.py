class ConexaoBancoDados:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Criando nova conexão com o banco...")
            cls._instancia = super(ConexaoBancoDados, cls).__new__(cls)
            cls._instancia.status = "Conectado"
        else:
            print("Reaproveitando a conexão já existente...")
        
        return cls._instancia

    def executar_query(self, query):
        print(f"Executando query '{query}' na instância {id(self)}")

if __name__ == "__main__":
    conexao1 = ConexaoBancoDados()
    conexao1.executar_query("SELECT * FROM usuarios")

    print("-" * 30)

    conexao2 = ConexaoBancoDados()
    conexao2.executar_query("SELECT * FROM produtos")

    print("-" * 30)
    if conexao1 == conexao2:
        print(f" Sucesso! As conexões são idênticas")
    else:
        print("Erro! São instâncias diferentes")