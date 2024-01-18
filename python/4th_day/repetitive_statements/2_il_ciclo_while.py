# Es.
msg = "esci"

while msg != "esci":
    # msg = input("scrivi qualcosa ")
    print("hai scritto", msg)

# Es.
# n = int(input("Fino a che numero vuoi contare? "))
n = 2
i = 0
while i <= n:
    print(i)
    i += 1


# l'utilizzo più popolare degli indici è quello di accedere agli elementi di una collezione
shopping_list = ["tofu", "latte di soia", "riso basmati", "yogurt greco"]
i = 0
print("La mia lista della spesa")
while i < len(shopping_list):
    print(f"{i}) {shopping_list[i]}")
    i += 1
