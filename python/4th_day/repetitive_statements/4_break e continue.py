# istuzioni break e continue

# BREAK interrompe il flusso di esecuzione del ciclo ed esce.
# CONTINUE interrompe solo l'esecuzione corrente del ciclo passando alla successiva.

shopping_list = ["gelato di soia", "yogurt", "pasta", "gelato al cioccolato", "biscotti al cioccolato", "patate"]

print("La mia lista della spesa con l'uso del BREAK")
print("Lista completa:", shopping_list)
for index, item in enumerate(shopping_list):
    # in questo caso break interrompe il ciclo for ed esce
    # in questo modo l'ultimo elemento "patate" non verrà stampato...
    if "cioccolato" in item:
        break
    print(index, "-", item)



print("La mia lista della spesa con l'uso del CONTINUE")
print("Lista completa:", shopping_list)
for index, item in enumerate(shopping_list):
    # in questo caso break interrompe il ciclo for ed esce
    # in questo modo l'ultimo elemento "patate" non verrà stampato...
    if "cioccolato" in item:
        continue
    print(index, "-", item)

