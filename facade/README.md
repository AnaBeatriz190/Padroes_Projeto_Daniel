# Padrão Facade

## 1. Visão Pessoal

O Facade é como o controle remoto da TV ou a recepção de um hotel. O sistema por trás pode ser super complexo (luzes, ar condicionado, projetor, sistema de som, limpeza de quarto), mas a fachada me dá um botão simples: "Assistir Filme" ou "Check-in". Ele esconde a complexidade e me dá uma interface limpa

## 2. Panorâmica do Funcionamento

- **Subsistemas:** Várias classes complexas que fazem o trabalho pesado
- **Facade:** Uma classe que conhece os subsistemas e oferece métodos simples (ex: `iniciar_sistema()`) que internamente chamam vários métodos dos subsistemas na ordem certa

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Simplicidade:** Isola o cliente da complexidade dos componentes
- **Desacoplamento:** Se os subsistemas mudarem, você só precisa arrumar a Facade, não o código do cliente inteiro

**Desvantagens:**
- **God Class:** A classe Facade pode acabar ficando grande demais e sabendo de "tudo" dentro do programa se não for bem gerenciada