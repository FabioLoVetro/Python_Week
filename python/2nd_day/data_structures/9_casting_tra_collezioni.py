# Abbiamo già visto come passare da un tipo di collezione a un altro
# tramite il casting... vediamo meglio come si fa...

name = ["fabio", "giuseppe", "carlo", "nicola", "carlo", "giuseppe"]
print(name)

# convertiamo la lista in tupla, diventa immutabile
t_name = tuple(name)
print(t_name)

# se passiamo da tupla a set
# perdiamo i duplicati e l'ordine
s_name = set(t_name)
print(s_name)

# da tupla di tuple a dizionario
# il primo valore della tupla diventerà la chiave, il secondo il valore
t_name_age = (("fabio", 39), ("giuseppe", 30), ("carlo", 33), ("nicola", 27))
d_name_age = dict(t_name_age)
print(d_name_age)

# da liste a dizionario
name = ["fabio", "giuseppe", "carlo"]
age = [39, 30, 33]
# non possiamo passare direttamente da liste a dizionari
# ma dobbiamo passare da liste a tuple e poi a dizionari
# python ci mette a disposione una funzione per fare questo
# la funzione è zip() che ritorna un generatore
# un generatore è un tipo di oggetto che python utilizza per ottenere
# dei valori soltanto quando questi valori servono effettivamente

t_name_age = zip(name, age)  # <zip object at 0x00000286843C2AC0>
print(t_name_age)
# per passare dal generatore alla tupla facciamo il casting
# t_name_age = tuple(t_name_age)  # (('fabio', 39), ('giuseppe', 30), ('carlo', 33))
# print(t_name_age)

# ma possiamo passare direttamente anche dal generatore al dizionario
d_name_age = dict(t_name_age)
print(d_name_age)
