# Le tuple
# si definisce tra parentesi tonde
# è un oggetto immutabile, cioè una volta creato non può essere modificato,
# quindi può essere solo interrogato.
# per il resto è simile a una lista
# posso usare metodi come: count(), index(), IN
# INDEXIG, SLICING...

t = (1, 3, 5, 7, 9)

print(type(t), t)  # <class 'tuple'> (1, 3, 5, 7, 9)

# se proviamo ad aggiungere o riassegnare un valore, otteniamo una eccezione

# le tuple possono essere utilizzate anche per contenere elementi di tipo differente

t = ("stringa", 1, True)  # elementi di tipo differente

# tupla di tuple
subjects_vote = (("italiano", 7), ("greco", 4), ("matematica", 10))

subjects_vote[2][1]  # 10

# lista di tuple
subjects_vote = [("italiano", 7), ("greco", 4), ("matematica", 10)]

# le stringhe sono collezioni di caratteri ed è immutabile
