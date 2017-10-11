#!/bin/sh

# get auxiliary functions
. ./aux.sh 

# compile romanos
fst transdutores/romanos/transdutorRomanos.txt

# compile transdutor 1

python3 ./material_apoio/scripts/compact2fst.py transdutores/1/palavras_compact.txt > transdutores/1/palavras.txt; 
fst transdutores/1/palavras.txt;
fst transdutores/1/underscore.txt;
fstconcat transdutores/1/palavras.fst transdutores/1/underscore.fst > transdutores/1/palavras_.fst;
fstconcat transdutores/romanos/transdutorRomanos.fst transdutores/1/underscore.fst > transdutores/1/romanos_.fst
fstunion transdutores/1/romanos_.fst transdutores/1/palavras_.fst > transdutores/1/uniao.fst;
#fstd transdutores/1/uniao.fst;
fstclosure transdutores/1/uniao.fst > transdutores/1/transdutor1.fst
fstd transdutores/1/transdutor1.fst
