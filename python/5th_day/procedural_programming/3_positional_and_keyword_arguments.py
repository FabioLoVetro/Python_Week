# Se non passiamo l'argomento ad una funzione con parametro
# questa ritornerà una eccezione
# python mette a disposizione la possibilità di definire dei valori di default
# in caso in cui non vengano passati gli argomenti
# per farlo basta assegnare un valore di default in fase di definizione della funzione
# ES. def say_something(something="something"):

print("*********************************")


def say_something(something="something"):
    # se non viene passato l'argomento stamperà "something"
    print(something)


# funzione richiamata senza argomento
say_something()

# se invece volessimo passare l'argomento dobbiamo fare in questo modo
say_something(something="argomento")
# cioè dobbiamo richiamare il parametro di cui vogliamo passare l'argomento
# questo tipo di parametri vengono detti KEYWORD ARGUMENTS
# quando la funzione utilizza parametri senza default,
# quei parametri vengono chiamati POSITIONAL ARGUMENTS
print("*********************************")

# NOTA
# è possibile definire una funzione sia con positional arguments che con keyword arguments insieme
# l'unica cosa da ricordare in questo caso è che prima si passa il valore dei positional arguments
# e dopo si passano i valori dei keyword arguments
# altrimenti python ritorna una eccezione
