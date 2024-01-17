# Python utilizza la tipizzazione forte
# non possiamo unire un numero con una stringa

# es.
age = 25
# print("Hai "+age+" anni")  # questo ritornerebbe una eccezione

# facendo il cast tutto funziona
print("Hai "+str(age)+" anni")

# esiste una soluzione diversa
#
# LA FORMATTAZIONE

# tecnica 1
# Operatore di formattazione e carattere di formattazione
# %d - numero intero
# %f - numero con la virgola
# %s - stringa
# nella stringa inseriamo
# l'operatore di formattazone %
# il carattere di formattazione d (d indica numero intero)
# e dopo la stringa la variabile/valore da sostituire hai primi 2

print("Hai %d anni" % age)

print("*************************")
print("tecnica 1 - Operatore di formattazione")

# my_name = input("Come ti chiami? ")
# my_age = int(input("Quanti anni hai? "))
my_name = "Fabio"
my_age = 38
my_born = 2024 - my_age

# questa istruzione restituisce una eccezione perchè se abbiamo più di una
# variabile, dobbiamo passarle come tupla...
# print("Il tuo nome è %s, hai %d anni, quindi sei nato nel %d"
#      % my_name % my_age % my_born)

print("Il tuo nome è %s, hai %d anni, quindi sei nato nel %d"
      % (my_name, my_age, my_born))


# altro esempio
# my_height = float(input("Inserisci la tua altezza in metri: "))
# my_weight = float(input("Inserisci il tuo peso in Kg: "))
my_height = 1.77
my_weight = 90

# print("Altezza=%f Peso=%f" % (my_height, my_weight))
# questa istruzione stamperà
# Altezza=1.770000 Peso=90.000000
# il float inserisce una precisione a 6 numeri dopo la virgola

# impostiamola a 2 decimali per l'altezza, ad 1 per il peso
# ci basta specificarlo tra l'operatore di formattazione
# e il carattere di formattazione inserendo ".2"
# questa operazione arrotonda e non tronca i numeri
print("Altezza=%.2f, Peso=%.1f" % (my_height, my_weight))
# Altezza=1.77 Peso=90.0

# tecnica 2
# utilizzo del metodo format
print("*************************")
print("tecnica 2 - metodo format")
print("Il tuo nome è {name}, hai {age} anni, quindi sei nato nel {born}".format(name=my_name, age=my_age, born=my_born))
print("Altezza={altezza:.2f}, Peso={peso:.1f}".format(altezza=my_height, peso=my_weight))

# tecnica 3
# f-string  (utilizzabile dalla versione 3.6 di python a salire...)
print("*************************")
print("tecnica 3 - f-string")
print(f"Il tuo nome è {my_name}, hai {my_age} anni, quindi sei nato nel {my_born}")
print(f"Altezza={my_height:.2f}, Peso={my_weight:.1f}")
