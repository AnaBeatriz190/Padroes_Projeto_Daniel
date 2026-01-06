# Padrão Interpreter

## 1. Visão Pessoal

O Interpreter é usado para criar uma linguagem própria para um problema específico

## 2. Panorâmica do Funcionamento

- **Expressão Abstrata:** Declara o método `interpretar()`
- **Expressão Terminal:** Os elementos básicos (números, variáveis)
- **Expressão Não-Terminal:** As regras combinadas (soma, subtração)

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Flexibilidade:** Fácil mudar e estender a gramática
- **Domínio Específico:** Ótimo para tarefas repetitivas descritas por regras de texto

**Desvantagens:**
- **Performance:** Fica lento se a gramática for muito complexa
- **Complexidade:** Difícil de manter para linguagens com muitas regras