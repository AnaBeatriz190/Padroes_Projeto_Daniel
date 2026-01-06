# Padrão Adapter

## 1. Visão Pessoal

O Adapter é exatamente como um adaptador de tomada de viagem. Se eu tenho um notebook com plugue de 3 pinos (o cliente) e chego numa casa que só tem tomada de 2 pinos (o serviço existente), eu não posso quebrar a parede nem mudar o plugue do notebook. Eu uso um adaptador no meio

## 2. Panorâmica do Funcionamento

- **Alvo (Target):** A interface que o seu código espera usar (ex: `conectarHDMI`)
- **Adaptado (Adaptee):** A classe que já existe mas tem uma interface incompatível (ex: `conectarVGA`)
- **Adaptador:** A classe que implementa o Alvo e, por dentro, chama o método do Adaptado, fazendo a tradução necessária

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Reutilização:** Permite usar classes existentes (legado) sem modificá-las
- **Integração:** Facilita a integração de bibliotecas de terceiros que não seguem o padrão do seu projeto

**Desvantagens:**
- **Excesso de código:** Criar uma classe nova apenas para adaptar uma chamada simples pode parecer exagero em projetos pequenos