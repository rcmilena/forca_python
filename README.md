# forca_python
**Título:** Jogo da Forca em Python

**Nível:** Iniciante

**Objetivo:** Criar um jogo da forca em Python, onde o jogador tenta adivinhar uma palavra oculta, revelando letras uma por uma. O jogo deve ser capaz de exibir a forca conforme o jogador faz tentativas erradas.

**Dicas:**

1. **Escolhendo uma palavra secreta:**
   - Crie uma lista de palavras que serão usadas no jogo.
   - Use a biblioteca `random` para escolher uma palavra aleatória da lista como a palavra secreta.

2. **Criando a interface do jogo:**
   - Pense em como você deseja representar a forca e a palavra oculta na tela do jogador. Você pode usar texto ASCII para desenhar a forca e underscores (_) para ocultar as letras da palavra.

3. **Loop principal:**
   - Use um loop para permitir que o jogador adivinhe letras até acertar a palavra ou esgotar todas as tentativas.
   - Exiba a forca atualizada após cada tentativa errada.
   - Solicite que o jogador insira uma letra como palpite.
   - Verifique se o palpite é uma letra válida (não um número ou uma palavra, por exemplo).
   - Verifique se o palpite já foi dado antes.

4. **Verificando os palpites:**
   - Compare o palpite do jogador com a palavra secreta para ver se a letra está presente na palavra.
   - Se o palpite estiver correto, revele a letra na palavra oculta.
   - Se o palpite estiver errado, diminua o número de tentativas restantes e desenhe a próxima parte da forca.

5. **Fim do jogo:**
   - Verifique se o jogador venceu (adivinhou todas as letras da palavra) ou perdeu (esgotou todas as tentativas).
   - Mostre uma mensagem de vitória ou derrota.
   - Dê a opção ao jogador de jogar novamente.

**Passo a passo geral:**

1. Defina uma lista de palavras.
2. Escolha uma palavra aleatória como a palavra secreta.
3. Crie a interface do jogo (forca inicial e palavra oculta).
4. Inicie um loop para o jogo principal.
   - Exiba a forca atual.
   - Solicite um palpite ao jogador.
   - Verifique se o palpite é válido.
   - Verifique se o palpite já foi dado antes.
   - Verifique se o palpite está correto ou errado.
   - Atualize a forca e a palavra oculta.
   - Repita até que o jogador ganhe ou perca.
5. Mostre uma mensagem de vitória ou derrota.
6. Pergunte ao jogador se deseja jogar novamente.

Este exercício irá ajudá-lo a consolidar conceitos fundamentais de programação, como loops, condicionais, listas e entrada/saída de dados, enquanto cria um jogo divertido.

## Tutorial com mais detalhes:
**Título:** Jogo da Forca em Python para Iniciantes

**Nível:** Iniciante

**Objetivo:** Criar um jogo de adivinhação da palavra (Jogo da Forca) em Python, onde o jogador tenta adivinhar uma palavra oculta letra por letra.

**Passo a Passo:**

**Passo 1: Preparação**
- **Instalação do Python:** Se o Python não estiver instalado, siga este guia para instalá-lo no seu sistema: [Guia de Instalação do Python](https://www.python.org/downloads/)

- **Instalação do VSCode (Visual Studio Code):** Se você não tiver um ambiente de desenvolvimento, pode instalar o VSCode, um editor de código Python amigável: [Instalação do VSCode](https://code.visualstudio.com/)

**Passo 2: Criando um Novo Projeto**
- Abra o VSCode.
- Crie uma nova pasta para o seu projeto em um local fácil de encontrar no seu computador.

**Passo 3: Escrevendo o Código**
- Dentro do VSCode, crie um novo arquivo chamado `jogo_da_forca.py`.

**Passo 4: Definindo a Palavra Secreta**
- Escolha uma palavra e anote-a em um papel.
- No código, defina a palavra secreta como uma variável.

**Passo 5: Desenhando a Forca**
- Para desenhar a forca, você pode usar uma representação visual simples em texto ASCII. Copie e cole um exemplo de desenho da forca no seu código.

**Passo 6: Obtendo o Palpite do Jogador**
- No código, use a função `input()` para obter um palpite do jogador. Peça a ele para adivinhar uma letra da palavra.

**Passo 7: Verificando o Palpite**
- Crie uma estrutura de decisão para verificar se o palpite do jogador está correto.
- Se o palpite estiver correto, atualize a palavra oculta com a letra correta revelada.
- Se o palpite estiver errado, atualize a forca e informe ao jogador quantas tentativas restantes ele tem.

**Passo 8: Repetindo o Jogo**
- Use um loop para permitir que o jogador continue adivinhando letras até acertar a palavra ou esgotar todas as tentativas.
- No final do jogo, exiba uma mensagem de vitória ou derrota.

**Passo 9: Rodando o Jogo**
- Execute o código no VSCode para jogar o jogo que você criou.

**Passo 10: Experimentando e Melhorando**
- Depois de terminar o projeto básico, experimente adicionar recursos extras ao jogo, como:
   - Mensagens de início e fim mais atraentes.
   - Gerar palavras aleatórias a partir de uma lista.
   - Contagem de pontos ou tentativas.
   - Gráficos ASCII mais elaborados para a forca.

Lembre-se de que a prática é a chave para aprender programação, então não tenha medo de experimentar e cometer erros. Este exercício é uma ótima maneira de começar a construir uma base sólida em Python e programação em geral. Divirta-se e aproveite o processo de aprendizado!
