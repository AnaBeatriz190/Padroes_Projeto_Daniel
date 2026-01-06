# Padrão Strategy

## 1. Visão Pessoal

Strategy funciona como um sistema de "plugins". Imagine uma compra onde você pode trocar a forma de pagamento a qualquer momento. A compra é a mesma, o dinheiro é o mesmo, mas o desconto da compra muda dependendo da forma de pagamento

## 2. Panorâmica do Funcionamento

O padrão é dividido em três partes principais:
1.  **Contexto:** É a classe principal que precisa realizar uma tarefa (ex: processar um pagamento), mas não sabe *como* fazer. Ela delega isso para a estratégia
2.  **Interface (Estratégia Abstrata):** Um contrato comum que define o método que todas as estratégias devem ter (ex: `pagar()`)
3.  **Estratégias Concretas:** As classes que implementam a lógica real (ex: `PagamentoPix`, `PagamentoCartao`)

## 3. Vantagens e Desvantagens

**Vantagens:**
* **Código Limpo:** Evita aqueles blocos gigantes de `if (tipo == 'pix') ... else if (tipo == 'cartao')`
* **Extensibilidade:** É muito fácil criar uma nova forma de pagamento no futuro sem quebrar o que já funciona (princípio Open/Closed)

**Desvantagens:**
* **Complexidade:** Aumenta o número de arquivos e classes no projeto para tarefas que poderiam ser simples
* **Conhecimento do Cliente:** Quem usa o código precisa saber qual estratégia escolher e instanciar