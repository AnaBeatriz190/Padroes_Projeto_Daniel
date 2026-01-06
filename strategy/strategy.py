from abc import ABC, abstractmethod

class EstrategiaPagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class PagamentoPix(EstrategiaPagamento):
    def pagar(self, valor):
        print(f"Pagamento de R${valor} realizado via PIX. (Desconto aplicado!)")

class PagamentoCartaoCredito(EstrategiaPagamento):
    def pagar(self, valor):
        print(f"Pagamento de R${valor} processado no Cartão de Crédito.")

class PagamentoBoleto(EstrategiaPagamento):
    def pagar(self, valor):
        print(f"Boleto gerado no valor de R${valor}. Aguardando compensação.")

class CarrinhoDeCompras:
    def __init__(self):
        self._estrategia_pagamento = None

    
    def definir_estrategia(self, estrategia: EstrategiaPagamento):
        self._estrategia_pagamento = estrategia

    def finalizar_compra(self, valor):
        if not self._estrategia_pagamento:
            print("Erro: Nenhuma forma de pagamento selecionada.")
            return
        
        print("Processando compra...")
        self._estrategia_pagamento.pagar(valor)

if __name__ == "__main__":
    carrinho = CarrinhoDeCompras()
    valor_compra = 100

    print("--- Teste 1: Cliente escolheu PIX ---")
    carrinho.definir_estrategia(PagamentoPix())
    carrinho.finalizar_compra(valor_compra)
    
    print("\n--- Teste 2: Cliente mudou para Cartão ---")
    carrinho.definir_estrategia(PagamentoCartaoCredito())
    carrinho.finalizar_compra(valor_compra)