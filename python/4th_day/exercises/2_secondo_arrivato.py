# Ricevi in input una lista con i punteggi dei partecipanti alla giornata dello sport universitaria,
# trova il punteggio del secondo classificato.
# ES. input
# 2 3 6 6 5
#
# ES. output
# 5
#
# Suggerimenti
# Tramite il metodo .split() possiamo dividere gli elementi di una stringa in base agli spazzi.
# Possiamo applicare una trasformazione a tutti gli elementi di  una collezione utilizzando la funzione map,
# questa funzione ritorna un generatore che possiamo riconvertire in una collezione.

# punteggi = input("inserisci i punteggi")
punteggi = "1 5 6 9 7 6"
punteggi = punteggi.split()
# punteggi = set(map(int, punteggi))  # in questo modo tolgo i duplicati ma perdo l'ordine originale
# punteggi = dict.fromkeys(map(int, punteggi))  # se avessimo voluto mantenere l'ordine originale togliendo i duplicati
punteggi = list(map(int, punteggi))
punteggi.sort(reverse=True)
print(punteggi)
print(punteggi[1])
