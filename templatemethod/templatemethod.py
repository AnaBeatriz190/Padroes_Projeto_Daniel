from abc import ABC, abstractmethod

class ProcessadorDeDados(ABC):
    def processar(self):
        self.abrir_arquivo()
        self.extrair_dados()
        self.analisar_dados()
        self.fechar_arquivo()

    def abrir_arquivo(self):
        print("1. Abrindo arquivo no disco...")

    def fechar_arquivo(self):
        print("4. Fechando arquivo.")

    @abstractmethod
    def extrair_dados(self):
        pass

    @abstractmethod
    def analisar_dados(self):
        pass

class ProcessadorPDF(ProcessadorDeDados):
    def extrair_dados(self):
        print("2. Lendo binário do PDF.")
    
    def analisar_dados(self):
        print("3. Analisando estrutura de texto do PDF.")

class ProcessadorCSV(ProcessadorDeDados):
    def extrair_dados(self):
        print("2. Lendo linhas separadas por vírgula.")
    
    def analisar_dados(self):
        print("3. Somando colunas da planilha CSV.")

if __name__ == "__main__":
    print("--- Processando PDF ---")
    pdf = ProcessadorPDF()
    pdf.processar()

    print("\n--- Processando CSV ---")
    csv = ProcessadorCSV()
    csv.processar()