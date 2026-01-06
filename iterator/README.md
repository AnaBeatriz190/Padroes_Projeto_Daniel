# Padrão Iterator

## 1. Visão Pessoal

O Iterator é como o botão "Próximo" do controle remoto ou do Spotify

## 2. Panorâmica do Funcionamento

- **Iterator:** Interface com métodos `tem_proximo()` e `proximo()`
- **Coleção:** O objeto que guarda os dados e cria o iterador correspondente

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Padronização:** Permite percorrer listas, árvores ou grafos usando o mesmo laço `for`
- **Simplificação:** A coleção não fica poluída com lógicas de travessia complexas

**Desvantagens:**
- **Exagero:** Em linguagens modernas (como Python), iteradores já são nativos e fáceis, criar classes manuais para isso pode ser redundante