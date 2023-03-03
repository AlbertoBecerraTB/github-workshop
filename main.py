import os
import sys

sys.path.append(os.getcwd())
from src.antonio_pares import antonio_pares
from src.alba_suma_lista import suma_lista
from src.feature_dustin import adding
from src.funcion_ias import suma_ias
from src.guillermo_dibujo_diamante import guillermo_diamante
from src.ismael_multiplica_divide import multiplica_divide
from src.jose_cuentadias import dia_semana
from src.julio_suma_cuadrados import suma_cuadrados
from src.miguel_suma_min_max import suma_valor_min_max

ls = [1, 2, 3, 4, 5, 10]

ls_idx = antonio_pares(ls)

print(suma_lista(ls_idx))

from src.perro import Perro

tuno = Perro("Podenco", 3, "Tuno")
print(tuno.edad)
print(tuno.cumpleanios())
print(tuno.edad)