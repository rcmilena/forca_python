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
