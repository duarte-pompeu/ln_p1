#!/usr/bin/fish

python3 ../../material_apoio/scripts/compact2fst.py palavras_compact.txt > palavras.txt; 
and fst palavras.txt;
and fst underscore.txt;
and fstconcat palavras.fst underscore.fst > palavras_.fst;
and fstconcat ../1/romanos.fst underscore.fst > romanos_.fst
and fstunion romanos_.fst palavras_.fst > uniao.fst;
and fstd uniao.fst;
and fstclosure uniao.fst > closure.fst
and fstd closure.fst

