# Padrão Visitor

## 1. Visão Pessoal

O Visitor é útil quando você tem várias classes diferentes e quer adicionar uma funcionalidade nova nelas sem mexer no código delas. Imagine um inspetor de vigilância sanitária (O Visitor)

## 2. Panorâmica do Funcionamento

- **Visitor:** Interface que declara métodos de visita para cada tipo de elemento (`visitRestaurante`, `visitHotel`)
- **Elemento:** Interface que declara o método `aceitar(visitor)`
- **Concrete Visitor:** Implementa o que fazer em cada visita

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Extensibilidade:** Adiciona operações novas (ex: "ExportarXML", "GerarRelatorio") sem mudar as classes dos elementos
- **Organização:** Agrupa operações relacionadas num só lugar

**Desvantagens:**
- **Quebra de Encapsulamento:** O visitador muitas vezes precisa acessar dados internos dos elementos
- **Manutenção:** Se adicionar um novo tipo de Elemento, tem que atualizar todos os Visitors