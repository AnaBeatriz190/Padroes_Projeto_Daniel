# Padrão Builder

## 1. Visão Pessoal

O Builder é como a linha de montagem de uma lanchonete (tipo Subway). O produto final é um "Sanduíche", mas ele pode ter muitas variações. Em vez de ter um construtor gigante (`new Sanduiche(pao, queijo, salada, molho, carne...)`), o Builder permite que eu diga: "Põe pão", "Põe queijo", "Sem salada". No final, eu peço "Construir" e recebo o objeto pronto

## 2. Panorâmica do Funcionamento

- **Builder:** Interface que define as etapas de construção (ex: `addParedes`, `addTelhado`)
- **Concrete Builder:** Implementa as etapas para um tipo específico
- **Director (Opcional):** Uma classe que sabe a ordem certa de chamar os passos para criar produtos populare

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Clareza:** O código de construção fica separado da lógica do negócio
- **Controle:** Permite construir objetos passo a passo

**Desvantagens:**
- **Verbosidade:** Exige a criação de classes Builder separadas para cada tipo de produto complexo