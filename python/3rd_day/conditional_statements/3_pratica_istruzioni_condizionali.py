# un pochino di pratica
# ISTRUZIONE IF

if True:
    print("questo testo viene stampato")

if False:
    print("Questo testo non viene stampato")

PRINT_VARIABLE = True

if PRINT_VARIABLE:
    print("questo testo viene stampato")

PRINT_VARIABLE = False

if PRINT_VARIABLE:
    print("questo testo NON viene stampato")


# ISTRUZIONE IF-ELSE

EMAIL = "giuseppe@profession.ai"
PASSWORD = "professionaispacca111"

email = input("Inserisci la tua email: ")
password = input("Inserisci la tua password")

if email == EMAIL:
    if password == PASSWORD:
        print("Hai 5 nuove email!")
    else:
        print("La password non è corretta. Accesso negato!!!")
else:
    print("Indirizzo email inesistente")

# un altro modo

if email == EMAIL and password == PASSWORD:
    print("Hai 5 nuove email!")
else:
    print("Credenziali invalide. Accesso negato!!!")


# ISTRUZIONE ELIF

n = int(input("Inserisci un numero"))

if n % 2 == 0 and n >= 0:
    print(f"{n} è positivo e pari")
elif n % 2 == 1 and n >= 0:
    print(f"{n} è positivo e dispari")
elif n % 2 == 0 and n <= 0:
    print(f"{n} è negativo e pari")
elif n % 2 == 1 and n <= 0:
    print(f"{n} è negativo e dispari")
else:
    print("nessuna delle precedenti -- mai eseguito in questo caso")


# L'ESPRESSIONE IF
# permette di definire una istruzione condizionale su di un unica riga

n = int(input("Inserisci un numero: "))

if n % 2:
    print("numero pari")
else:
    print("numero dispari")

# utilizzando l'espressione if

n = int(input("Inserisci un numero: "))

is_even = True if n % 2 == 0 else False

print(f"{n} è pari? {is_even}")

# ancora più semplificato

is_even = n % 2 == 0
print(f"{n} è pari? {is_even}")

# ancora di più

print(f"{n} è", "pari" if n % 2 == 0 else "dispari")

print(f"{n} è", "dispari" if n % 2 else "pari")

