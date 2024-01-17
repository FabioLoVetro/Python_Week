# Le istruzioni condizionali
# ci permettono di eseguire istruzioni solo se
# delle condizioni sono verificate

a = float(input("Inserisci il dividendo: "))
b = float(input("Inserisci il divisore: "))
# c = a / b
# print(f"{a}/{b}={c}")

# che succede se b è = 0?
# python ritorna una eccezione
# possiamo gestire la situazione con una istruzione condizionale
# se b è diverso da 0 eseguiamo l'operazione altrimenti no

# if b != 0:
#     c = a/b
#     print(f"{a}/{b}={c}")

# Nota
# python utilizza l'indentazione per capire il contesto delle istruzioni
# indentazione e spazzi sono necessari

# potremmo gestire la situazione in cui b = 0 nell'else

if b != 0:
    c = a/b
    print(f"{a}/{b}={c}")
else:
    print("Non puoi dividere per zero")
