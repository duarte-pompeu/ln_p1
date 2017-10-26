# ln_p1
1st project for Natural Language course

# Some fish commands

$ fst romanos2.txt # compiles and draws the roman FST

$ for i in (seq 100 | shuf)
    echo $i; fstcomp nums_fst/$i.fst romanos2.fst /tmp/out.fst; and read
end # composes a random number and the roman translator, then draws it; press enter to go to the next one, ^C to quit


# Shortcuts for fish shell

set SIMS /home/jubileu/git/ln_p1/material_apoio/syms.txt

function fst
	set src $argv[1]
	set base (echo $src | cut -f 1 -d '.')

	fstc $src > $base.fst; 
	and fstdraw --isymbols=/home/jubileu/git/ln_p1/material_apoio/syms.txt --osymbols=/home/jubileu/git/ln_p1/material_apoio/syms.txt --portrait $base.fst | dot -Tpdf > $base.pdf;
	and open $base.pdf
end

function fstc
	set src $argv[1]
	set base (echo $src | cut -f 1 -d '.')
	fstcompile --isymbols=/home/jubileu/git/ln_p1/material_apoio/syms.txt --osymbols=/home/jubileu/git/ln_p1/material_apoio/syms.txt $src > $base.fst;
end

function fstcomp
	set src_1 $argv[1]
	set src2 $argv[2]
	set dest $argv[3]
	set base_dest (echo $dest | cut -f 1 -d '.')

	fstcompose $src_1 $src2 > $dest;
	and echo "comped";
	and fstdraw --isymbols=/home/jubileu/git/ln_p1/material_apoio/syms.txt --osymbols=/home/jubileu/git/ln_p1/material_apoio/syms.txt --portrait $dest | dot -Tpdf > $base_dest.pdf;
	and open $base_dest.pdf
end

function fstd 
	set src $argv[1]
	set base (echo $src | cut -f 1 -d '.')
	
	echo $draw
	fstdraw --isymbols=/home/jubileu/git/ln_p1/material_apoio/syms.txt --osymbols=/home/jubileu/git/ln_p1/material_apoio/syms.txt --portrait $src | dot -Tpdf > $base.pdf;
	and open $base.pdf
end
