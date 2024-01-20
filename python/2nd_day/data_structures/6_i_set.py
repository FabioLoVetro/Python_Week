# I set
# collezione che contiene elementi UNICI e non ORDINATI
# si definisce tra parentesi graffe

s = {1, 2, 3, 10, 9, 8}
print("s:", s)

# se provo ad aggiungere un elemento già presente, questo non verrà inserito
# non posso definire un ordine per gli elementi
# è ordinato secondo le tabelle di hashing
# nel set gli indici non esistono, quindi non posso usare l'indexing per accedere agli elementi

# ACCESSO AGLI ELEMENTI - metodo add()
s.add(25)
print("add(25):", s)

# RIMOZIONE ELEMENTO - metodo pop()
rimosso = s.pop()  # restituisce l'elemento rimosso
print("s.pop(): rimosso:", rimosso, s)

# metodo remove(obj)
s.remove(3)
print("s.remove(3):", s)
# se l'elemento non è presente = eccezione

# se voglio rimuovere un elemento che non sono sicuro sia presente uso discard()
# in questo caso se l'elemento non è presente non succede nulla
s.discard(100)
print("s.discard(100):", s)

# metodo clear()
# rimuove tutti gli elementi
s.clear()
print("s.clear():", s)

# TIPO PARTICOLARE DI SET
# FROZENSET  --> versione immutabile del set - uso della funzione frozenset()
setImmutabile = {frozenset({"uno", "due", "tre"})}
print(setImmutabile, type(setImmutabile))  # {frozenset({'tre', 'uno', 'due'})} <class 'set'>

