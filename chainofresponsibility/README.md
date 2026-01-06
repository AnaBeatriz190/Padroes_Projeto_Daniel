# Padrão Chain of Responsibility

## 1. Visão Pessoal

O Chain of Responsibility (Corrente de Responsabilidade) funciona como o suporte técnico de uma empresa de telefonia. Primeiro você fala com o robô (Nível 1). Se ele não resolve, passa para o atendente humano (Nível 2). Se for algo grave, passa para o gerente (Nível 3). Quem pede ajuda não sabe quem vai resolver, apenas lança o pedido na corrente e alguém captura

## 2. Panorâmica do Funcionamento

- **Handler (Manipulador):** Interface que define o método de tratamento e a referência para o "próximo" da fila
- **Concrete Handlers:** Verificam se podem resolver o problema. Se sim, resolvem. Se não, passam para o próximo

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Desacoplamento:** Quem envia o pedido não precisa saber quem vai tratar
- **Flexibilidade:** É fácil mudar a ordem da corrente ou adicionar novos níveis de suporte

**Desvantagens:**
- **Incerteza:** Não há garantia de que o pedido será tratado (pode chegar ao fim da corrente sem solução)