# Padrão Bridge

## 1. Visão Pessoal

O Bridge (Ponte) serve para evitar a explosão de classes cartesianas. Imagine que tenho `ControleRemoto` e `TV`

## 2. Panorâmica do Funcionamento

- **Abstração (Controle):** Define a lógica de alto nível
- **Implementação (Dispositivo):** Define a lógica de baixo nível (ligar, mudar canal)
- **A Ponte:** A Abstração possui um objeto da Implementação

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Desacoplamento:** Posso criar novos Controles sem mexer nas TVs, e novas TVs sem mexer nos Controles
- **Organização:** Evita herança múltipla ou excessiva

**Desvantagens:**
- **Complexidade:** Adiciona camadas que podem parecer desnecessárias em sistemas muito simples