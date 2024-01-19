# Qualche altra funzione

def compute_area_triangle(b, h):
    return b*h/2


# b = float(input("Inserisci la base del triangolo: "))
# h = float(input("Inserisci l'altezza del triangolo: "))
b = 10
h = 5
area = compute_area_triangle(b, h)
print(f"L'are del triangolo di base {b} e altezza {h} è pari a {area}")

# altra funzione
def print_shopping_list(shopping_list, owner="Fabio"):
    print("La lista della spesa di", owner)
    for i, entry in enumerate(shopping_list):
        print(f"{i+1} {entry}")


shopping = ["pizza", "latte", "pane", "riso"]

print_shopping_list(shopping)
