# FROM PythonWeek course
# creiamo una struttura dati in grado di contenere i record di diversi studenti.
# la struttura sarà composta da un dizionario, con chiave il nome dello studente e
# come valore una lista. La lista deve contenere delle tuple e ogni tupla deve avere
# in prima posizione il nome della materia ed in seconda posizione il voto ed in
# terza le ore di assenza.
# 1) popola la struttura dati con le informazioni riportate in tabella.
# 2) aggiungi alla struttura dati la pagella di un nuovo studente chiamato Albert einstein,
# con 10 in tutte le materie e nessuna ora di assenza
# 3) aggiungi Fisica a tutte le pagelle con le seguenti votazioni/assenze:
# Giuseppe Gullo 9.5/0,
# Antonio Barbera 8/1,
# Emiliano Ruozzo 8/3,
# Albert Einstein 10/0
# 4) stampa la tupla con le informazioni sulla materia Matematica per Giuseppe Gullo
# 5) stampa la tupla con le informazioni sulla materia Inglese per Emiliano Ruozzo
# 6) stampa solo il voto di Antonio Barbera in Geografia
# Tabella
# Studente          Matematica      Italiano        Inglese         Storia          Geografia
# Giuseppe Gullo    Voto:9,Ass:0    Voto:7,Ass:3    Voto:7.5,Ass:4  Voto:7.5,Ass:4  Voto:5,Ass:7
# Antonio Barbera   Voto:8,Ass:1    Voto:6,Ass:1    Voto:9.5,Ass:0  Voto:8,Ass:2    Voto:8,Ass:1
# Emiliano Ruozzo   Voto:7.5,Ass:2  Voto:6,Ass:2    Voto:4,Ass:3    Voto:8.5,Ass:2  Voto:8,Ass:2

studenti = {
    "Giuseppe Gullo": [
        ("Matematica", 9, 0),
        ("Italiano", 7, 3),
        ("Inglese", 7.5, 4),
        ("Storia", 7.5, 4),
        ("Geografia", 5, 7)
    ],
    "Antonio Barbera": [
        ("Matematica", 8, 1),
        ("Italiano", 6, 1),
        ("Inglese", 9.5, 0),
        ("Storia", 8, 2),
        ("Geografia", 8, 1)
    ],
    "Emiliano Ruozzo": [
        ("Matematica", 7.5, 2),
        ("Italiano", 6, 2),
        ("Inglese", 4, 3),
        ("Storia", 8.5, 2),
        ("Geografia", 8, 2)
    ]
}

print(studenti)

studenti["Albert Einstein"] = [("Matematica", 10, 0), ("Italiano", 10, 0), ("Inglese", 10, 0), ("Storia", 10, 0),
                               ("Geografia", 10, 0)]

print(studenti)

studenti["Giuseppe Gullo"].append(("Fisica", 9.5, 0))
studenti["Antonio Barbera"].append(("Fisica", 8, 1))
studenti["Emiliano Ruozzo"].append(("Fisica", 8, 3))
studenti["Albert Einstein"].append(("Fisica", 10, 0))

print(studenti)

print("Giuseppe Gullo ", studenti["Giuseppe Gullo"][0])
print("Emiliano Ruozzo ", studenti["Emiliano Ruozzo"][2])
print("Antonio Barbera ", "Geografia ", "Voto ", studenti["Antonio Barbera"][4][1])
