# Padrão Flyweight

## 1. Visão Pessoal

O Flyweight é o padrão da "economia de RAM"

## 2. Panorâmica do Funcionamento

- **Estado Intrínseco (Compartilhado):** Dados que não mudam (ex: a cor da árvore, o modelo 3D)
- **Estado Extrínseco (Único):** Dados que mudam (ex: a coordenada onde a árvore está plantada)
- **Fábrica Flyweight:** Gerencia o cache dos objetos compartilhados

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Memória:** Reduz drasticamente o uso de RAM em sistemas com muitos objetos repetidos
  
**Desvantagens:**
- **Complexidade:** O código fica mais difícil de ler, pois o estado do objeto é separado em dois lugares