# Processo Target 😎

Olá, aqui vou dar uma descrição básica sobre o que fiz em cada teste 😁

Adianto, utilizei a linguagem Python🐍, e evitei fazer uso de funções inclusas na propria linguagem 😅. Então acredito que esse desafio vai ser 8 ou 80. Ou vou bem, ou vou muito mal 😢😢

Outro ponto é, talvez a leitura de algumas variáveis e funções pode ficar cansativas por ser extensa 😕. Isso dá para ter uma noção um pouco melhor sobre cada processo, facilitando a análise não precisando compreender o que significa variável 'x' ou 'y' 😉.

Ah, aqui não considero o teste 1. Pois o mesmo é uma verificação de valor dado um pseudo-código, porém o considero nas nomenclaturas.

## Teste 2

### Fibonacci e verificar se um número pertence a sequência

Aqui poderia ser utilizado DP (Dynamic Programming) junto com BS (Binary Search), porém a descrição ao meu entendimento não ficou muito clara,
ele me dava a entender que a cada verificação era necessário refazer a lista, isso foi feito em um algoritmo iterativo que está na ordem de O(n).

## Teste 3

### Dado um Json encontrar o Menor, Maior e dias acima da média

Aqui é carregado um Json, no qual me entrega uma lista de dicionário.

Para cada opção é feita uma função que me retorna o valor necessário,
com um adendo à 'dias_superior_a_media' ela me retorna os dias ao qual é superior a média, porem é visualizado a quantidade de dias no array.

## Teste 4

### Dado os ganhos de cada estado dizer qual a porcentagem em relação ao total

Os dados de ganho foram descritos na própria descrição do problema. Os transcrevi para o código em forma de lista de dicionários.

Para cada dicionário apresento o resultado com F-String. Na primeira interpolação apresento o estado referente e na segunda chamo uma função que calcula a porcentagem.

## Teste 5

### Inverter uma string

Aqui o principal adendo é sobre a forma que Python trata String, pois não é como se fosse uma lista como conhecemos.

Assim, o que foi feito é transformá-lo em uma lista. Opção utilizada é percorrer do fim da string até o início, e concatená-lo a uma string vazia (Assim sendo uma string novamente).

A fim de conhecimento há uma opção mais performática em relação à escolhida. Essa utiliza um método de Two Pointers.
A ideia é ter um index para o início que sempre incrementa, e um index para o fim que sempre decrementa. O ponto de parada seria o meio ou ⌊n⌋ onde n é o tamanha da string.

Por que essa solução é mais performática? Na complexidade assintótica constantes aditivas e multiplicativas em geral não são importantes, assim podem ser desprezadas, assim ambas as soluções possuem complexidade O(n).
Porém quando a entrada é grande o suficiente ela pode gerar pequenas alterações de velocidade de processamento, quando reparamos na contante de cada solução vemos que na solução implementada a constante é C=1, enquanto a constante da solução descrita aqui no README é C=1/2, o que pode ocasionar esse ligeiro incremento de performance.
