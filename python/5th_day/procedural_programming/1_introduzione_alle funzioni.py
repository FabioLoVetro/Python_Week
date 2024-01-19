# Vedremo ora il paradigma della programmazione procedurale
# introduciamo quello che è il suo elemento centrale: la funzione
#
# la programmazione procedurale è un paradigma di programmazione, in cui la logica del codice viene valutata dall'alto verso il basso (top-down)
# il punto centrale è la funzione chiamata anche procedura (da qui il nome programmazione procedurale)
#
# le FUNZIONI sono dei blocchi di codice adibiti a uno scopo specifico che sono totalmente utilizzabili tramite un alias
#
# proviamo a definire una funzione per il calcolo della media di una lista di numeri

def mean(vals):  # la prima riga prende il nome di "definizione della funzione"
    vals_sum = 0
    for val in vals:
        vals_sum += val
    vals_mean = vals_sum / len(vals)
    return vals_mean

# ANATOMIA di una funzione
# def - keyword utilizzata per definire una funzione
# nome - il nome da dare alla funzione
# (lista parametri) - la lista dei parametri che vogliamo passare alla funzione, tra parentesi tonde
# la funzione non deve necessariamente avere dei parametri in ingresso
# corpo della funzione - blocco di codice da eseguire
# return valore - il valore da ritornare (la funzione non deve necessariamente ritornare un valore)

# CHIAMATA A FUNZIONE è il processo di chiamare una funzione


lista = [12, 9, 4, 21, 11, 5, 17, 8, 22, 10]
l_mean = mean(lista)
print(l_mean)  # 11.9

# differenza tra PARAMETRO e ARGOMENTO
# il PARAMETRO è un placeholder che utilizziamo durante la definizione della funzione
# l'ARGOMENTO è l'effettivo valore che passiamo alla funzione

# FUNZIONI FATTE BENE
# le funzioni per essere fatte bene devono fare una e una cosa soltanto
# assolvere un unico compito logico
# si dice che la funzione deve essere "SPECIALIZZATA"
# ES funzione sintatticamente corretta, ma non specializza. NON VA BENE
def mean_and_max(vals):
    vals_sum = 0
    vals_max = None
    for val in vals:
        vals_sum = vals_sum+val
        if vals_max is None or val > vals_max:
            vals_max = val
    vals_mean = vals_sum/len(vals)
    return vals_mean, vals_max

# Soluzione -> si divide in due funzioni
# una che calcola la media
# una che calcola il max

# Come capire se va creata una Funzione?
# Se usi stesse istruzioni per fare una stessa operazione in più parti del codice,
# allora è molto probabile che tu debba creare una funzione.

