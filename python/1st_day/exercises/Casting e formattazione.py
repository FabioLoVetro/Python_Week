# FROM PythonWeek course
# Un programma che richiede dei dati in input e li stampa con qualcosa in più
# - dati in input:
#   nome e cognome
#   anno di nascita
#   luogo di nascita
#   altezza in metri, 2 decimali
#   peso in kg, 2 decimali
# - data da calcolare
#   età, approssimata senza mese e giorno

CURRENT_YEAR = 2024
name = input("Type the name ")
surname = input("Type the surname ")
year = int(input("Type the year of birth "))
city = input("Type the city of birth ")
height = float(input("Type the height in meters "))
weight = float(input("Type the weight in Kg "))
age = CURRENT_YEAR - year

print(f"{name} {surname}, age {age}, born in {city} "
      f"in {year}, height {height:.2f} meters, weight {weight:.2f} Kg")
