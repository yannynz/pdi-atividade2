## Questão 1

Essa questão consiste em identificar bandeiras de vários países em imagens. Um processo anterior já removeu o fundo, então só nos resta dizer qual é qual. Iremos analisar os seguintes países. Veja na pasta `q1/img` exemplos de todas essas bandeiras nas imagens de teste.

1. Mônaco
2. Peru
3. Singapura
4. Irlanda
5. Itália

Você deve trabalhar no arquivo `q1.ipynb` para realizar essa questão. 

Neste notebook, você deve implementar a função `identifica_bandeira` para identificar as bandeiras. A função recebe uma imagem e retorna uma lista de tuplas no formato:

```
# exemplo de tupla
(PAIS, (x1, y2), (x2, y2)`)

# exemplo de lista de tupla
[(PAIS, (x1, y2), (x2, y2)`),(PAIS, (x1, y2), (x2, y2)`),(PAIS, (x1, y2), (x2, y2)`)]
```

onde:


- `PAIS` é uma string com o nome do país tratado (em minúsculas e sem espaços). Se você não conseguiu identificar uma bandeira, pode retornar uma lista.
- `(x1, y1)` é o ponto do topo esquerdo do retângulo em que a bandeira está inserida
- `(x2, y2)` é o ponto baixo direito do retângulo em que a bandeira está inserida


Você pode criar funções auxiliares para manter o código organizado e facilitar a implementação.

Use mas não altere a função `draw_bandeiras`, está função serve para desenhar na imagem o resultado encontrado pela função `identifica_bandeira`.


**A ordem dos elementos da lista não é importante, apenas seu conteúdo**


Os critérios de avaliação são os seguintes:

R1 até **2** pontos: encontrou o canto de todas as bandeiras
R2 até **3,4** pontos: Fez R1 e identificou uma (1) bandeira e acertou seus cantos em `todas` imagens de testes.
R3: Fez R2 e **+0.4** pontos e para cada `nova` bandeira acertada corretamente em todas as imagens de testes. (ao todo 4 x 0,4 = 1,6)
