#!/bin/sh

# get auxiliary functions
. ./aux.sh 

# compile romanos
fst transdutores/romanos/transdutorRomanos.txt

# compile transdutor 1

python3 material_apoio/scripts/compact2fst.py transdutores/1/palavras_compact.txt > transdutores/1/palavras.txt; 
fstc transdutores/1/palavras.txt;
fstc transdutores/1/underscore.txt;
fstconcat transdutores/1/palavras.fst transdutores/1/underscore.fst > transdutores/1/palavras_.fst;
fstconcat transdutores/romanos/transdutorRomanos.fst transdutores/1/underscore.fst > transdutores/1/romanos_.fst
fstunion transdutores/1/romanos_.fst transdutores/1/palavras_.fst > transdutores/1/uniao.fst;
#fstd transdutores/1/uniao.fst;
fstclosure transdutores/1/uniao.fst > transdutores/1/transdutor1.fst
fstd transdutores/1/transdutor1.fst

# compile transdutor 2
python3 material_apoio/scripts/compact2fst.py transdutores/2/transdutor2_compact.txt > transdutores/2/transdutor2.txt; 
fst transdutores/2/transdutor2.txt;

# compile transdutor 3
python3 material_apoio/scripts/compact2fst.py transdutores/3/transdutor3_compact.txt > transdutores/3/transdutor3.txt; 
fst transdutores/3/transdutor3.txt;

# codificador

fstarcsort transdutores/1/transdutor1.fst > transdutores/codificador/1.fst
fstarcsort transdutores/2/transdutor2.fst > transdutores/codificador/2.fst
fstarcsort transdutores/3/transdutor3.fst > transdutores/codificador/3.fst

fstcomp transdutores/codificador/1.fst transdutores/codificador/2.fst /tmp/aux.fst;
#echo "1";
fstcomp /tmp/aux.fst transdutores/codificador/3.fst transdutores/codificador/codificador.fst;
#echo "2";
fstd transdutores/codificador/codificador.fst

#codificar mensagem
fstcomp transdutores/codificador/exemplos/biblioteca_do_palacio_de_monserrate_na_estante_a_esquerda_no_dia_14_de_novembro_pelas_10_23_de_maio_.fst\
	transdutores/codificador/codificador.fst\
	transdutores/codificador/mail1.fst; 
fstd transdutores/codificador/mail1.fst


