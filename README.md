# Monta Palavras
A lógica do programa se baseia em ordenar as palavras em uma lista, desde a
de pontuação mais alta até a de pontuação mais baixa e respeitando os critérios
de desempate (tamanho da palavra e ordem alfabética), logo após essa lista é
percorrida até que uma dessas palavras possa ser escrita com as letras digitadas
pelo usuário.
O programa pode ser executado com: 
```python main.py```

### IMPORTANTE!
O pacote "unicodedata" precisa estar instalado para que o programa consiga lidar
com os caracteres especiais. Se o código for executado no Linux esse Pacote
provavelmente já está instalado.

## ARQUIVOS DE ENTRADA
Tanto a lista de palavras quanto as pontuações de cada letra são lidas de
um arquivo .txt tornando assim fácil a alteração dos mesmos.
Caracteres especiais e de pontuação são removidos, a formatação dos dados
de pontuação de cada letra é levada em conta para gerar um Dicionário
que relaciona cada pontuação diferente as letras que tem essa pontuação

## ORDENAÇÃO
Para a ordenação é usada uma Classe Game_Word que contém como atributos a
palavra em si e a sua pontuação calculada por uma função.
Primeiro a lista de palavras é ordenada em ordem alfabética
Depois a coleção de objetos é ordenada levando em conta uma variável
ponderada com a pontuação com um valor maior, descontando o tamanho
da palavra, para que palavras menores tenham prioridade.

## COMPARAÇÕES
A entrada do usuário é comparada com essa lista ordenada de palavras, 
cada palavra é comparada com a entrada até que seja encontrada uma
palavra que pode ser escrita com esses caracteres ou até que a lista
seja toda percorrida.

Na comparação entra uma palavra da lista com a entrada, cada caractere
da palavra é procurado na entrada, se todos forem encontrados, então
a palavra pode ser escrita com aquela entrada, e como a lista é percorrida
da palavra mais valiosa para a menos valiosa, assim que uma palavra for
encontrada sabe-se que é a mais valiosa possível.

## EFICIÊNCIA (ARQUIVOS JSON)
Uma das etapas mais custosas da execução desse programa é ler as palavras
calcular o valor de todas e ordená-las da palavra de maior pontuação para a
de menor pontuação. Porém uma vez que essas etapas foram feitas, elas não
precisam ser repetidas sempre.
Para melhorar a eficiência, essa lista ordenada é armazenada em um arquivo
JSON, assim enquanto a lista de palavras e o valor de cada letra não for
alterado o programa pode se servir desse arquivo e apenas procurar a palavra
mais valiosa, sem repetir essas operações exigentes. Quando uma alteração for
necessária, basta alterar as informações nos arquivos .txt e apagar os arquivos 
JSON que novos arquivos serão gerados pelo programa em sua primeira execução

## TESTES UNITÁRIOS
Para facilitar o desenvolvimento testes unitários automatizados foram gerados 
no arquivo test_main.py isso possibilitou que fosse mais fácil escrever novo 
código sem que as funcionalidades já implementadas fossem prejudicadas.
Os testes cobrem alguns casos interessantes para a função find_highest_value_word()
como palavras não encontradas, empates em valor, etc.
Para rodar os testes é só chamar no terminal: 
```python test_main.py```

Todas as funções relativas ao jogo, a escrita e leitura de arquivos estão
devidamente comentadas em seus módulos.