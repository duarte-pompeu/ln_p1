#!/usr/bin/fish

fstarcsort ../1/closure.fst  > 1.fst
fstarcsort ../2/transdutor2.fst  > 2.fst
fstarcsort ../3/transdutor3.fst  > 3.fst

fstcomp 1.fst 2.fst /tmp/aux.fst;
and echo "1";
and fstcomp /tmp/aux.fst 3.fst codificador.fst;
and echo "2";
and fstd codificador.fst


fstcomp exemplos/biblioteca_do_palacio_de_monserrate_na_estante_a_esquerda_no_dia_14_de_novembro_pelas_10_23_de_maio_.fst codificador.fst mail1.fst; 
fstd mail1.fst
