# Le liste
# per creare una nuova lista
# CREAZIONE
nome_lista = [1, 2, 3, 4, 5]

lista_stringhe = ["abc", "def"]

# ACCESSO AGLI ELEMENTI
# indexing (l'indice parte da 0)
print(nome_lista[0])  # 1
print(nome_lista[1])  # 2

# anche a ritroso (l'indice parte da -1 e non da 0)
print(nome_lista[-1])  # 5
print(nome_lista[-2])  # 4

# SLICING [0:2] [::-1] --> start incluso, end escluso
print(nome_lista[0:2])  # [1,2] (primo indice incluso, secondo indice escluso)
print(nome_lista[:])   # tutti gli elementi
print(nome_lista[2:])  # [3, 4, 5] dall'indice 2 a fine
print(nome_lista[:3])  # [1, 2, 3] dall'indice 0 al 3
print(nome_lista[-2:])  # [4, 5] dal -2 a fine
# Nota
print(nome_lista[::-1])  # [5, 4, 3, 2, 1] tutta la lista invertita
print(nome_lista[:2:-1])   # [5, 4] da 0 al 2 della lista invertita
