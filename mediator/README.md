# Padrão Mediator

## 1. Visão Pessoal

O Mediator é a Torre de Controle de um aeroporto. Se cada avião tivesse que falar com todos os outros aviões para não bater, seria o caos total. Em vez disso, os aviões falam apenas com a Torre, e a Torre diz quem pode pousar e quem deve esperar. Ele transforma uma rede de conexões "muitos-para-muitos" em "um-para-muitos"

## 2. Panorâmica do Funcionamento

- **Mediator:** Interface que define a comunicação
- **Concrete Mediator:** Conhece e mantém referências aos colegas e coordena a lógica
- **Colleagues (Colegas):** Os objetos que precisam se comunicar, mas falam apenas com o mediador

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Organização:** Reduz dependências diretas entre classes
- **Simplicidade:** É mais fácil entender o fluxo olhando para o Mediador do que olhando para vários objetos espalhados

**Desvantagens:**
- **Gargalo:** O Mediador pode se tornar um objeto gigante e complexo (God Object) difícil de manter