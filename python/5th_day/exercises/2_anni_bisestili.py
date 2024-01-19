# FROM HackerRank
# Anni bisestili
# Ogni 4 anni aggiungiamo un giorno al mese più breve dell'anno,
# cioè Febbraio, quest'anno è chiamato bisestile.
# I criteri utilizzati per definire se un anno è bisestile sono i seguenti:
# - L'anno è divisibile per 4, allora è bisestile a meno che:
# -- l'anno è divisibile per 100, allora non è bisestile a meno che:
# --- l'anno è divisibile per 400
#
# Es. 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600 sono tutti anni non bisestili
# Es. 1600, 2000, 2024, 2400 anni bisestili
# scrivi uan funzione per verificare se un anno è bisestile

def is_leap_year(anno):
    bisestile = False
    if anno % 4 == 0:
        if anno % 100 != 0:
            bisestile = True
        elif anno % 400 == 0:
            bisestile = True
    return bisestile


anno = int(input("digita un anno "))
if is_leap_year(anno):
    print(f"L'anno {anno} è Bisestile")
else:
    print(f"L'anno {anno} non è Bisestile")
