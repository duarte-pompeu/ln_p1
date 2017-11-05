#!/bin/sh

# TAREFA 1
# testar se frases não desejadas estão a ser filtradas bem
mkdir teste
cat $1 | grep -P "n-é-verbo.*\t" > teste/n_verbo.txt
cat $1 | grep -P "[\t].*\bvir\b.*\bvir\b.*" > teste/2x.txt
cat $1 | grep -P "#.*\t" > teste/erros.txt
cat $1 | grep -P "\?.*\t" > teste/duvidas.txt

# filtrar frases não desejadas
FINAL=$(echo $1 | cut -d . -f 1).final
cat $1 | grep -vP "n-é-verbo.*\t" \
| grep -vP "[\t].*\bvir\b.*\bvir\b.*" \
| grep -vP "#.*\t" \
| grep -vP "\?.*\t" \
> $FINAL

# alterar verbo para lema no inicio da frase
# formato da frase: (lema)\t(texto)(vir)(texto)
sed -E -i 's/(.*)\t(.*)(vir)(.*)/\2\1\4/g' $FINAL

# TAREFA 2
./word_counter.py < virAnotado.final

# TAREFA 3
./lemas.py virUnigramas.txt virBigramas.txt  aux/anotador/foiParametrizacao.txt virFrases.txt > virResultado.txt
