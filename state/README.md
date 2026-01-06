# Padrão State

## 1. Visão Pessoal

O padrão State permite que um objeto mude sua "personalidade" quando seu estado muda

## 2. Panorâmica do Funcionamento

- **Contexto:** A classe principal (ex: Celular) que mantém uma referência ao estado atual
- **Interface State:** Define os métodos que mudam de acordo com o estado
- **Concrete States:** Implementam a lógica específica para aquele estado

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Limpeza:** Remove condicionais complexas (`if estado == A... if estado == B`)
- **Coesão:** A lógica de cada estado fica isolada em sua própria classe

**Desvantagens:**
- **Excesso de Classes:** Se o sistema tiver poucos estados e poucas mudanças, criar classes para cada um pode ser exagero