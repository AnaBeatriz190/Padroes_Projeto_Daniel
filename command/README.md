# Padrão Command

## 1. Visão Pessoal

O Command transforma uma ação em um objeto

## 2. Panorâmica do Funcionamento

- **Command (Interface):** Declara o método `execute()`
- **Concrete Command:** Liga uma ação a um Receiver (quem realmente faz o trabalho)
- **Invoker:** Quem dispara o comando (ex: um botão)
- **Receiver:** Quem executa a lógica de negócio (ex: a lâmpada)

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Desfazer/Refazer:** Facilita muito a implementação de Undo/Redo
- **Desacoplamento:** O botão que você clica não precisa conhecer a lógica da lâmpada, só conhece o comando "Ligar"

**Desvantagens:**
- **Muitas Classes:** Para cada ação possível no sistema, você precisa criar uma classe de Comando nova