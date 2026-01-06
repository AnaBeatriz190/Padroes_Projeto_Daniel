# Padrão Decorator

## 1. Visão Pessoal

Decorator é como "vestir camadas de roupa" ou "montar uma pizza". Você tem o objeto base (o corpo ou a massa) e vai adicionando comportamentos (casaco, cachecol ou queijo, orégano) em volta dele

## 2. Panorâmica do Funcionamento

- **Componente:** A interface base
- **Decorador Base:** Mantém uma referência ao objeto original
- **Decoradores Concretos:** Adicionam o comportamento extra antes ou depois de chamar o método do objeto original

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Flexibilidade:** Adiciona funcionalidades sem usar herança estática
- **Combinação:** Permite misturar vários comportamentos (ex: café + leite + chocolate) de forma dinâmica

**Desvantagens:**
- **Pequenas classes:** O projeto fica cheio de pequenas classes parecidas
- **Configuração:** Montar o objeto final (instanciar decorador dentro de decorador) pode ficar feio visualmente no código