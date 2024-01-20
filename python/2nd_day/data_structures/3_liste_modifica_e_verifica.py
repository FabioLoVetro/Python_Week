# ASSEGNAZIONE

lista = [1, 2, 3, 5, 9, 13, 21]
print(lista)

lista[4] = 10  # [1, 2, 3, 5, 10, 13, 21]
print(lista)

# anche con lo slicing
lista[1:3] = [90, 100]  # [1, 90, 100, 5, 10, 13, 21]
print(lista)

# AGGIUNTA - metodo append(obj), aggiunge un elemento alla fine della lista

lista.append(22)  # [1, 90, 100, 3, 5, 10, 13, 21, 22]
print(lista)
lista.append(23)  # [1, 90, 100, 3, 5, 10, 13, 21, 22, 23]
print(lista)

# AGGIUNDA - metodo insert(index, obj), aggiunge l'elemento all'indice passato

lista.insert(2, 0)  # [1, 90, 0, 100, 3, 5, 10, 13, 21, 22, 23]
print(lista)

# RIMOZIONE ELEMENTO - metodo remove(obj)

lista.remove(13)  # [1, 90, 0, 100, 3, 5, 10, 21, 22, 23]
print(lista)

# RIMOZIONE - metodo pop(index), rimuove l'elemento all'indice passato
# ritorna l'elemento rimosso

lista.pop(0)  # [90, 0, 100, 3, 5, 10, 21, 22, 23]
print(lista)

# VERIFICA SE UN ELEMENTO è CONTENUTO NELLA LISTA
# keyword IN --> ritorna True se è presente, False altrimenti

check = 100 in lista  # True
print(check)

# metodo index, ritorna l'indice della prima occorrenza dell'elemento
print(lista.index(100))  # 2

# metodo count, ritorna il numero di occorrenze dell'elemento passato come parametro
print(lista.count(100))  # 1
lista.append(100)  # [90, 0, 100, 5, 10, 21, 22, 23, 100]
print(lista.count(100))  # 2
