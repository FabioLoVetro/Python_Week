# Validazione di indirizzi
# Realizziamo una funzione che, prendendo in input una lista di indirizzi email,
# ritorni una nuova lista degli indirizzi email validi ordinati alfabeticamente.
#
# un'indirizzo email è valido se:
# - ha il formato nomeutente@dominio.estensione
# - il nome utente contiene soltanto lettere, numeri, lineette (-) e trattini bassi (_)
# - il dominio contiene soltanto lettere e numeri
# - la lunghezza massima dell'estensione è 3 caratteri

def validatore_email(email_list):
    validated_list = []
    for address in email_list:
        if "@" not in address or "." not in address:
            continue
        else:
            user_name = address[:address.index("@")]
            dominio = address[address.index("@") + 1:address.index(".")]
            estensione = address[address.index(".") + 1:]

        if len(user_name) == 0 or len(dominio) == 0 or len(estensione) < 1 or len(estensione) > 3:
            continue
        else:
            for c in user_name:
                is_username_valid = True
                if not c.isalnum() and c not in ["-", "_"]:
                    is_username_valid = False
                    break
            if is_username_valid:
                for c in dominio:
                    is_domain_valid = True
                    if not c.isalpha() and not c.isdigit():
                        is_domain_valid = False
                        break
        if is_username_valid and is_domain_valid:
            validated_list.append(address)
            validated_list.sort()
    return validated_list


lista_email_valide = ["fabiolovetro@gmail.com", "fabiolovetro@gmail3.com", "fabiolovetro3@gmail.com",
                      "fabiolovetro3@gmail3.com", "nome@tiscali.it"]

lista_email_non_valide = ["@gmail.com", "fabio@gmail.", "@.", "fabio.com", "fabiolovetro*@gmail3.com",
                          "fabiolovetro@gmail*.com", " ", ""]

print("*********** VALIDE *************")
print(validatore_email(lista_email_valide))
print()
print("*********** NON VALIDE *************")
print(validatore_email(lista_email_non_valide))
