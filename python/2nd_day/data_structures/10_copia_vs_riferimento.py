# differenza tra copia e riferimento

lista = ["cane", "gatto", "topo"]
print("lista", lista)

lista2 = lista
print("lista2", lista2)
lista2[2] = "tigre"
print("lista2", lista2)
print("lista", lista)

# lista2 è stata inizializzata con un riferimento che punta allo stesso oggetto di lista
# quindi modificando una delle due il risultato lo si vede da entrambe

# possiamo verificare se si tratta dello stesso oggetto con la funzione ID
print("id(lista)", id(lista))
print("id(lista2)", id(lista2))
print("********************************+")
lista = ["cane", "gatto", "topo"]
print("lista", lista)
# shallow copy
lista2 = lista.copy()
print("lista2 = lista.copy()", lista2)
lista2[2] = "tigre"
print("lista2[2] = tigre", lista2)
print("lista", lista)

# adesso lista2 è stata inizializzata con una copia di lista, quindi non è lo stesso oggetto
# modificando una l'altra rimane invariata

print("id(lista)", id(lista))
print("id(lista2)", id(lista2))
