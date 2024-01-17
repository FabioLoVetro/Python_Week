# FROM PythonWeek course
# leggi un float a ed un intero b e stampa
# 1) a elevato a b
# 2) il modulo di a per b
# all'interno del print inserisci anche l'operazione che stai eseguendo
# ES. 3.0 ** 2 = 9.0
# ES. 3.0 %  2 = 1.0

a = float(input("Type the first number "))
b = int(input("Type the second number "))

print(f"{a} ** {b} = {a ** b}")
print(f"{a} % {b} = {a % b}")
