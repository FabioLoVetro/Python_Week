# Leggi una stringa in input all'interno di un loop.
# Se la stringa è uguale a "stop" interrompi il programma,
# altrimenti verifica se la stringa è un palindromo,
# in caso positivo stampa "PAROLA è un palindromo" inserendo la parola inserita in input al posto di PAROLA,
# altrimenti stampa "PAROLA non è un palindromo".
#
# Suggerimento
# Un palindromo è una parola che può essere letta allo stesso modo in entrambi i sensi
# Es. radar, osso, aerea

msg = ""
while msg != "stop":
    msg = input("scrivi una parola ")
    if msg == "stop":
        print("Ciao a presto!")
        break
    if msg == msg[::-1]:
        print(f"{msg} è un palindromo")
    else:
        print(f"{msg} non è un palindromo")

