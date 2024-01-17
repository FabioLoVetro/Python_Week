# FROM PythonWeek course
# Lo swapping consiste nell'invertire il valore di due variabili
# 1) leggi 2 valori in input
# 2) stampali
# 3) scambiali
# 4) stampali

a = int(input("Type a "))
b = int(input("Type b "))
print(f"a= {a} and b= {b}")
# c = a
# a = b
# b = c
# usando l'assegnazione multipla
a, b = b, a
print(f"a= {a} and b= {b}")
