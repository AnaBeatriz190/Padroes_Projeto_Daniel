# Padrão Observer

## 1. Visão Pessol

O Observer funciona como uma assinatura de Newsletter ou Canal do YouTube. Existe um criador de conteúdo (o "Sujeito") e vários inscritos (os "Observadores"). Quando o criador posta algo novo, ele avisa automaticamente todos os inscritos. Eu não preciso ficar entrando no canal toda hora para ver se tem vídeo novo (polling); o canal me avisa quando tiver

## 2. Panorâmica do Funcionamento

- **Subject (Sujeito):** Mantém uma lista de interessados e tem métodos para adicionar/remover inscritos
- **Observer (Observador):** Uma interface que define como o inscrito recebe a atualização (ex: método `update()`)
- **Notificação:** Quando o estado do Sujeito muda, ele percorre a lista e chama o `update()` de cada um

## 3. Vantagens e Desvantagens

**Vantagens:**
- **Reatividade:** Permite que objetos reajam a mudanças em outros objetos sem ficarem fortemente acoplados
- **Dinâmico:** É possível adicionar e remover observadores em tempo de execução

**Desvantagens:**
- **Ordem de execução:** Não se garante a ordem em que os observadores serão notificados
- **Vazamento de memória:** Se você esquecer de remover um observador da lista quando ele não for mais necessário, ele ficará na memória para sempre (o problema do "Lapsed Listener")