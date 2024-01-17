# abbiamo visto come riassegnare diversi tipi di valore
# perchè python è un linguaggio non tipizzato

var = 5
var = 0.5
var = "stringa"

# python usa la tipizzazione forte
# quindi non è possibile passare da un tipo di dato ad un altro implicitamente

a = 1
b = "2"
# print(a+b)   il risultato sarà una eccezione

# bisogna eseguire un casting

print(a+int(b))  # ok, abbiamo eseguito il casting --> int(b)

# PER CONOSCERE IL TIPO DI UNA VARIABILE PYTHON FORNISCE UNA FUNZIONE APPOSITA

# FUNZIONE type()
type(a)
type(b)

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>

# PER CONOSCERE IL PESO IN BYTE DI UNA VARIABILE PYTHON FORNISCE UNA FUNZIONE APPOSITA

# FUNZIONE getsizeof()      bisogna importare la funzione dalla standard library sys
from sys import getsizeof
getsizeof(a)
getsizeof(b)

print(getsizeof(a))  # 28
print(getsizeof(b))  # 50

# PER CONTARE I CARATTERI DI UNA STRINGA PYTHON FORNISCE UNA FUNZIONE APPOSITA

# FUNZIONE len()
len(b)

print(len(b))

stringa = "questa è una prova"
print("lunghezza della stringa: ", stringa, ":", len(stringa), "con peso : ", getsizeof(stringa))
