# I dizionari
# sono un tipo di collezione che ci permette di salvare i dati sotto forma di
# CHIAVE : VALORE
# si definisce tra parentesi graffe (come i set)
# è mutabile

report = {"Matematica": 9, "Italiano": 6.5, "Fisica": 8}
print(type(report), report)  # <class 'dict'> {'Matematica': 9, 'Italiano': 6.5, 'Fisica': 8}

# ACCESSO - indexig per chiave
voto = report["Matematica"]
print("voto = report[Matematica]", voto)  # voto = report[Matematica] 9

# AGGIORNAMENTO - NUOVA ASSEGNAZIONE
# se esiste la chiave, il valore viene aggiornato
# se la chiave non esiste viene inserita una nuova coppia CHIAVE:VALORE
report["Matematica"] = 10
print(report)
report["Chimica"] = 8
print(report)

# mappa di mappe
report["Inglese"] = {"grammatica": 7, "letteratura": 8}
print(report)

# ottenere tutti i valori
valori = report.values()  # ritorna un dict_values
print(valori)  # dict_values([10, 6.5, 8, 8, {'grammatica': 7, 'letteratura': 8}])
# lo convertiamo in una lista per utilizzarlo
valori = list(valori)
print(valori)  # [10, 6.5, 8, 8, {'grammatica': 7, 'letteratura': 8}]

# ottenere tutte le chiavi
chiavi = report.keys()  # ritorna un dict_keys
print(chiavi)  # dict_keys(['Matematica', 'Italiano', 'Fisica', 'Chimica', 'Inglese'])
# convertiamo in lista
chiavi = list(chiavi)
print(chiavi)  # ['Matematica', 'Italiano', 'Fisica', 'Chimica', 'Inglese']
