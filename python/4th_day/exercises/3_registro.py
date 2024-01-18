# Hai a disposizione un record di N studenti.
# Ogni record contiene in nome dello studente e il suo voto in Matematica, Fisica, Chimica.
# I voti possono essere numeri con la virgola.
# Un utente inserisce un intero N seguito da il nome e i voti di N studenti.
# Il programma deve salvare i record in un dizionario.
# Alla fine l'utente inserirà il nome di uno studente,
# il programma dovrà dare in output la media dei voti di tale studente
# arrotondata a due cifre dopo la virgola.
#
# Es. input
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
#
# Malika
#
# Es. output
# 56.00

n = int(input("Inserisci il numero degli studenti "))
studenti = {}
i = 0
while i < n:
    studente = input(f"Inserisci i dati dello studente numero {i+1} ")
    studente = studente.split()
    studenti[studente[0]] = list(map(float, studente[1:]))
    i += 1

print(studenti)
studente = input("Inserisci il nome dello studente di cui vuoi conoscere la media ")

print(f"La media di {studente} è : {sum(studenti[studente])/len(studenti[studente]):.2f}")
