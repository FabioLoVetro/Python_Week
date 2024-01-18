# Istruzioni cicliche
# ci permettono di eseguire istruzioni in maniera ciclica (ripetuta)

# vediamo subito un esempio del perché sono importanti

# data una lista di valori vogliamo fare la media
vals = [12, 1, 5, 7, 8, 3]
vals_sum = vals[0] + vals[1] + vals[2] + vals[3] + vals[4] + vals[5]
vals_mean = vals_sum / len(vals)

# come si vede per sommare tutti i valori dobbiamo estrapolarli uno a uno
# e se i valori fossero 100??? 1000??? 100000000000000000???
# e se fossero diverse liste???
# chiaramente si deve trovare un modo per rendere il tutto trasparente
# LE ISTRUZIONI RIPETITIVE (I CICLI)

# PYTHON mette a disposizione due tipi di istruzioni cicliche
# il ciclo WHILE e il ciclo FOR

# WHILE
vals = [12, 1, 5, 7, 8, 3]
vals_sum = 0
i = 0

while i < len(vals):
    vals_sum = vals_sum + vals[i]
    i += 1

vals_mean = vals_sum / len(vals)

# FOR  (non gestiamo l'indice)
vals = [12, 1, 5, 7, 8, 3]
vals_sum = 0

for val in vals:
    vals_sum = vals_sum + val

vals_mean = vals_sum / len(vals)

print(vals_sum, " ", len(vals), " ", vals_mean)
