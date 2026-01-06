# Padrão Abstract Factory

## 1. Visão Pessoal

Factory Method é uma fábrica de um produto só, o Abstract Factory é um complexo industrial. Imagine uma loja de móveis: você pode comprar uma Cadeira ou um Sofá. Mas eles precisam combinar. Se eu escolho o estilo "Vitoriano", tanto a cadeira quanto o sofá devem ser vitorianos

## 2. Panorâmica do Funcionamento

- **Fábrica Abstrata:** Define métodos para criar cada produto da família (ex: `criarCadeira`, `criarSofa`)
- **Fábricas Concretas:** Implementam a criação para uma variante específica (ex: `FabricaVitoriana`, `FabricaModerna`)
- **Cliente:** Usa apenas a interface abstrata, então não importa qual fábrica concreta está rodando, os móveis sempre combinarão

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Consistência:** Garante que os produtos usados juntos sejam compatíveis
- **Isolamento:** O código cliente não toca nas classes concretas

**Desvantagens:**
- **Rigidez:** É difícil adicionar um novo tipo de produto (ex: "Mesa") porque você teria que alterar todas as fábricas existentes