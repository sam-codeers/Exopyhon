def fill_prefix(registration):
    prefix = registration.split("-")[0]
    if len(prefix) < 2:
        prefix = prefix + " " * (2 - len(prefix))
    return prefix

registration = input("Entrez l'immatriculation de l'avion : ")
prefix = fill_prefix(registration)
print("Préfixe :", prefix)
