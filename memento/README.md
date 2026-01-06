# Padrão Memento

## 1. Visão Pessoal

O Memento é o "Save Point" de um jogo ou o "Ctrl+Z" do editor de texto. Ele permite tirar uma fotografia (snapshot) do estado atual de um objeto e guardar essa foto numa gaveta. Se eu fizer besteira depois, posso pegar a foto e restaurar o objeto exatamente como ele estava naquele momento, sem violar o encapsulamento (sem mexer nas variáveis privadas diretamente)

## 2. Panorâmica do Funcionamento

- **Originator:** O objeto cujo estado queremos salvar (ex: Editor)
- **Memento:** O objeto que guarda os dados salvos (a caixa fechada)
- **Caretaker:** Quem cuida dos Mementos (o histórico), mas não pode mexer no conteúdo deles

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Recuperação:** Facilita a implementação de "Desfazer"
- **Encapsulamento:** O estado interno do objeto não é exposto publicamente

**Desvantagens:**
- **Memória:** Se o estado do objeto for grande e salvarmos muitas vezes, a RAM vai encher rápido