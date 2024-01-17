# vediamo all'opera il casting

# da int a float
var = 1
var = float(var)  # castato a float
print(var, type(var))

# da float a int
var = int(var)
print(var, type(var))
# quando andiamo ad eseguire il casting il float non viene arrotondato
# viente TRONCATO

# PER ARROTONDARE DOBBIAMO UTILIZZARE LA FUNZIONE round()

# da int a string
var = 5
var = str(var)
print(var, type(var))

# da string a int
var = int(var)  # possibile perché il contenuto rappresenta un numero altrimenti eccezione
print(var, type(var))
