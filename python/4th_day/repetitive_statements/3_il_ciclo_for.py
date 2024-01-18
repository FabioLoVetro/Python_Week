# ES.
shopping_list = ["tofu", "latte di soia", "riso basmati", "yogurt greco"]

print("La mia lista della spesa")

for item in shopping_list:
    print("-"+item)

# possiamo utilizzare il for per iterare su un indice utilizzando la funzione range()
# range(start, end(not included)) ritorna un insieme di valori
range(10)  # solo con l'indice end
range(1, 10)  # ritorna un oggetto iterabile

# possiamo vederlo in una lista
print(list(range(1, 10)))

# n = int(input("Fino a che numero vuoi stampare? "))
n = 5
for i in range(n):
    if(i % 2):
        print(i, "Dispari")
    else:
        print(i, "Pari")



shopping_list = ["tofu", "latte di soia", "riso basmati", "yogurt greco"]
print("stampa con range()")
print("La mia lista della spesa")

for item in range(len(shopping_list)):
    print(item+1, "-", shopping_list[item])

# esiste un modo migliore... utilizzo della funzione enumerate
# enumerate() ritorna delle tuple con indice ed elemento
print(list(enumerate(shopping_list)))
# [(0, 'tofu'), (1, 'latte di soia'), (2, 'riso basmati'), (3, 'yogurt greco')]
print("stampa con enumerate()")
for tupla_ritornata in enumerate(shopping_list):
    print(tupla_ritornata[0]+1, "-", tupla_ritornata[1])

# oppure posso impostare 2 variabili al for
print("stampa con enumerate() e doppia variabile in for")
for index, item in enumerate(shopping_list):
    print(index+1, "-", item)


