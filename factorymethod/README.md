# Padrão Factory Method

## 1. Visão Pessoal

O Factory Method é como uma empresa de logística. A empresa (Fábrica) decide qual transporte fabricar (navio, carro, caminhão) e prepara tudo. O cliente  apenas pede o transporte e a fábrica entrega o objeto pronto para uso

## 2. Panorâmica do Funcionamento

- **Produto:** Uma interface comum para os objetos que serão criados (ex: `Transporte`)
- **Criador (Creator):** Classe que declara o método fábrica
- **Fábricas Concretas:** Classes que estendem o criador e decidem qual objeto específico instanciar (ex: `FabricaMaritima` cria `Navio`)

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Desacoplamento:** O código cliente não conhece as classes concretas (Navio, Caminhão), apenas a interface (Transporte)
- **Extensibilidade:** Para adicionar "Transporte Aéreo", basta criar a classe Avião e sua fábrica, sem mudar o código existente

**Desvantagens:**
- **Complexidade:** Pode levar a muitas subclasses pequenas apenas para criar objetos simples.