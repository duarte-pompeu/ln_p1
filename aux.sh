#!/bin/sh
# defines absolute location for syms.txt and auxiliary functions

SYMS=$(pwd)/material_apoio/syms.txt
echo $SYMS

pdf(){
	# your systems pdf reader
	evince $@
}

fst(){
	src=$1
	base=$(echo $src | cut -f 1 -d '.')

	fstc $src > $base.fst; 
	fstdraw --isymbols=$SYMS --osymbols=$SYMS --portrait $base.fst | dot -Tpdf > $base.pdf;
	pdf $base.pdf > /dev/null &
}

fstc(){
	src=$1
	base=$(echo $src | cut -f 1 -d '.')
	fstcompile --isymbols=$SYMS --osymbols=$SYMS $src > $base.fst;
}

fstcomp(){
	src_1=$1
	src2=$2
	dest=$3
	base_dest=$(echo $dest | cut -f 1 -d '.')

	fstcompose $src_1 $src2 > $dest;
	fstdraw --isymbols=$SYMS --osymbols=$SYMS --portrait $dest | dot -Tpdf > $base_dest.pdf;
	pdf $base_dest.pdf  > /dev/null &
}

fstd(){
	src=$1
	base=$(echo $src | cut -f 1 -d '.')
	
	draw;
	fstdraw --isymbols=$SYMS --osymbols=$SYMS --portrait $src | dot -Tpdf > $base.pdf;
	pdf $base.pdf
}
