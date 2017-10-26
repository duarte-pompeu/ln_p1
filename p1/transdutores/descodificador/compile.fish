#!/usr/bin/fish

fstinvert ../codificador/codificador.fst > descodificador.fst
fstd descodificador.fst

fstcomp exemplos/Xs_21_pm_32111_d9_d9z97r0_3332111_3412_312_n_13_32111_31_0_.fst descodificador.fst mail1.fst; fstd mail1.fst
fstcomp exemplos/3332111_3412_321_n_13_2111_321_0_3311_d9_jXn9Vr0_p9lXs_312_h_.fst descodificador.fst mail2.fst; fstd mail2.fst


