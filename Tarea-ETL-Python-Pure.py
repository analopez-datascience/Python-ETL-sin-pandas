"""Llegir un conjunt de dades d'alumnes ficticis i crear un CSV net.
Treballarem quatre problemes habituals:
  1. Valors absents (missing values).
  2. Espais innecessaris abans o després dels valors.
  3. Valors numèrics fora dels rangs permesos.
  4. Registres duplicats, comparant-los amb TUPLES.
  
Escriure conjunt de dades net en arxiu de sortida"""
import csv
from pathlib import Path

CARPETA = Path(__file__).resolve().parent
ARXIU_ENTRADA = CARPETA / "../Datafiles/dataset_alumnes_brut.csv"
ARXIU_SORTIDA = CARPETA / "../Datafiles/dataset_alumnes_net.csv"

if not ARXIU_ENTRADA.exists():
    raise FileNotFoundError(
        f"No trobo {ARXIU_ENTRADA.name}"
    )

#Carrega del CSV
CAMPS = ["id_alumne","ciutat","edat","hores_estudi_setmana","nota_final","assistencia_pct","modalitat"]
MODALITATS_PERMESES = {"Presencial","Online","Híbrida"}

with ARXIU_ENTRADA.open("r", encoding="utf-8-sig", newline="") as fitxer:
    lector = csv.DictReader(fitxer,delimiter=";")
    if lector.fieldnames != CAMPS:
        raise ValueError(
                f"Les columnes del fitxer no són les correctes."
            )
    dades = list(lector)

print("Registros originals: ", len(dades))
print("Primer registre: ", dades[0])


#Eliminem espais en blanc
comptador_espais = 0
for fila in dades:
    for camp in CAMPS:
        valor_original = fila[camp]
        valor_net = valor_original.strip()
        if valor_original != valor_net:
            comptador_espais += 1
        fila[camp] = valor_net

print("Nº celes corregides amb espais blanc: ", comptador_espais)

dades_completes = [
    fila for fila in dades if all(fila[camp] != "" for camp in CAMPS)
]

eliminades_per_buits = len(dades) - len(dades_completes)
print("Files eliminades: ", eliminades_per_buits)

#Validamos rangos
dades_valides = [ 
    fila for fila in dades_completes if int(fila["edat"]) >= 0 and int(fila["hores_estudi_setmana"]) >= 0  
    and float(fila["nota_final"]) >= 0 and float(fila["assistencia_pct"]) >= 0
]
