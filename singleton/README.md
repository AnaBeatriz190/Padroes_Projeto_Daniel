# Padrão Singleton

## 1. Visão Pessoal

O Singleton garante que uma classe tenha apenas uma única instância (objeto) existindo em todo o programa

## 2. Panorâmica do Funcionamento

- **Controle de Instância:** A classe esconde o construtor padrão e oferece um método estático (geralmente chamado `getInstance`) que verifica: "Já existe uma instância criada?"
- **Lógica:** Se não existe, cria. Se já existe, retorna a que foi criada anteriormente

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Controle de recursos:** Bom para gerenciar conexões com banco de dados ou arquivos de log, evitando abrir múltiplas conexões desnecessárias
- **Acesso global:** Permite um ponto de acesso fácil para essa instância

**Desvantagens:**
- **Acoplamento:** Pode agir como uma variável global "glorificada", escondendo dependências no código
- **Testes:** É difícil de testar (Unit Testing) porque o estado persiste entre os testes