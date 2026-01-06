# Padrão Template Method

## 1. Visão Pessoal

O Template Method é como uma receita de bolo industrial. A estrutura geral é fixa: bater, assar, decorar. Ninguém pode mudar essa ordem. Porém, o sabor da massa (chocolate ou baunilha) e o tipo de decoração são definidos nas etapas específicas

## 2. Panorâmica do Funcionamento

- **Classe Abstrata:** Define o método principal (Template) que chama os passos (passo1, passo2, passo3)
- **Passos Abstratos:** Métodos que as subclasses SÃO obrigadas a implementar
- **Hooks (Ganchos):** Métodos opcionais que as subclasses podem ou não sobrescrever

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Reuso de Código:** A parte comum do algoritmo fica num lugar só (na classe pai)
- **Controle:** A classe pai controla a ordem de execução

**Desvantagens:**
- **Rigidez:** As subclasses ficam presas ao esqueleto definido pelo pai
- **Complexidade:** Pode ser difícil entender o fluxo se houver muitos níveis de herança