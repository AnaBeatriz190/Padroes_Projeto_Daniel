# Padrão Prototype

## 1. Visão Pessoal

O Prototype é literalmente a "clonagem"

## 2. Panorâmica do Funcionamento

- **Interface Prototype:** Declara o método `clone()`
- **Implementação:** A classe concreta implementa o método clone copiando seus valores atuais para uma nova instância

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Performance:** Evita processos de inicialização caros
- **Simplicidade:** Cria objetos complexos mais facilmente do que configurar via construtor

**Desvantagens:**
- **Referências circulares:** Clonar objetos que têm referências para outros objetos (Deep Copy vs Shallow Copy) pode ser bem complicado