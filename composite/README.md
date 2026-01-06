# Padrão Composite

## 1. Visão Pessoal

O Composite é o padrão da "Árvore". Pense nas pastas do seu computador. Uma pasta pode conter arquivos OU outras pastas

## 2. Panorâmica do Funcionamento

- **Componente:** Interface comum (ex: `mostrarDetalhes`)
- **Folha (Leaf):** O objeto final que não tem filhos (ex: Arquivo)
- **Composite:** O objeto que tem filhos (ex: Pasta) e repassa a ação para eles

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Recursividade:** Facilita muito lidar com estruturas de árvore (menus, sistemas de arquivos)
- **Polimorfismo:** O cliente não precisa saber se está lidando com um item ou uma lista de itens

**Desvantagens:**
- **Generalização excessiva:** Pode tornar o design muito genérico, permitindo combinações que não deveriam existir