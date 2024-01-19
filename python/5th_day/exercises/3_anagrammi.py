# FROM HackerRank
# Anagrammi
# Definire una funzione che, prende in input due parole, verifica se le due parole sono anagrammi.

# Suggerimento
# due parole sono anagrammi se sono composte esattamete dalle stesse lettere
# ES. strani/nastri, carino/canori, senatori/estranio

def anagrams(word1="", word2=""):
    if word1 != word2 and len(word1) == len(word2):
        for c in word1:
            if c not in word2 or word1.count(c) != word2.count(c):
                return False
    return True


w1 = input("Inserisci la prima parola: ")
w2 = input("Inserisci la seconda parola: ")
if anagrams(w1, w2):
    print(f"{w2} è un anagramma di {w1}")
else:
    print(f"{w2} non è un anagramma di {w1}")