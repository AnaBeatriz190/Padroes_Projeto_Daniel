# Padrão Proxy

## 1. Visão Pessoal

O Proxy é como um "porteiro" ou um "cache". Se você quer falar com o Chefe (objeto real), você fala com a secretária (Proxy) antes

## 2. Panorâmica do Funcionamento

- **Interface:** A mesma interface para o Proxy e o Objeto Real
- **RealSubject:** O objeto que faz o trabalho de verdade
- **Proxy:** Mantém uma referência ao RealSubject e controla o acesso a ele

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Segurança:** Controla quem acessa o objeto
- **Performance:** Pode carregar o objeto real apenas quando necessário (Lazy Loading)

**Desvantagens:**
- **Latência:** Introduz um passo a mais na chamada, o que pode atrasar levemente a resposta