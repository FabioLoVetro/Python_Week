# Vediamo ora come far ritornare qualcosa alle nostre funzioni
def say_something(something="something"):
    # se non viene passato l'argomento stamperà "something"
    say = "Say " + something
    return say


# funzione richiamata senza argomento
print(say_something())
print(say_something("qualcosa"))


# NOTA
# le funzioni che ritornano qualcosa vengono dette FRUITFUL FUNCTION
# le funzioni che non ritornano qualcosa vengono dette VOID FUNCTION
# in realtà non ci sono funzioni che non ritornano nulla
# quelle che non ritornano nulla ritornano un "None"... (cioè nulla) °_0

# proviamo a verificare questa cosa

def say_something_return_none(something="something"):
    # se non viene passato l'argomento stamperà "something"
    say = "Say " + something


var = say_something_return_none()
print(var)
# questa stampa None
