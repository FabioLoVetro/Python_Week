# Le collezioni sono tipi di dati che possiamo utilizzare
# per raggruppare insieme più dati

# immaginiamo di avere 5 persone e dobbiamo lavorare con le informazioni di queste persone
# potremmo creare una variabile per ogni informazione per esempio l'altezza.
# concetto difficile da gestire...

# meglio raggruppare tutte le informazioni "coerenti" in una collezione
# per esempio una Lista
# lista di persone
# lista di altezze
# lista di...

# quando usare le collezioni?
# quando il tipo di informazione da immagazzinare è la stessa

# PRINCIPALI COLLEZIONI CHE PYTHON METTE A DISPOSIZIONE
# LISTE, TUPLE, SET, DICTIONARY

# 1) LISTE  - contengono dati che possono cambiare (MUTABILE)
#           - si definisce con le parentesi quadre
#           - ES. heights = [180, 168, 177, 171, 165]
#           - i valori al suo interno possono cambiare

# 2) TUPLE  - contengono dati che NON possono cambiare (IMMUTABILE)
#           - si definisce con le parentesi tonde
#           - ES. heights = (180, 168, 177, 171, 165)
#           - i valori al suo interno non possono cambiare

# 3) SET    - contengono dati unici non ordinati (non possiamo decidere noi l'ordinamento)
#           - è ordinato secondo una funzione di hashing
#           - si definisce con le parentesi graffe
#           - può contenere solo dati distinti, se proviamo ad aggiungere un duplicato non lo aggiunge
#           - ES. names = {"marco","antonio","giuseppe","","andrea"}

# 4) DICT   - i dizionari o mappe sono una struttura dati del tipo chiave-valore
#           - si definisce con le parentesi graffe
#           - il primo valore corrisponde alla chiave e il secondo al valore separati da :
#           - ES. shopping_list = {"latte":5, "tofu":2, "cereali":3}

