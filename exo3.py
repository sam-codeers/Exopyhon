def validate_plate(plate):
    if len(plate) != 7:
        return False
    if not plate[0:2].isdigit():
        return False
    if not plate[3:7].isalpha():
        return False
    if plate[2] != '-':
        return False
    return True

plate = input("Entrez une plaque d'immatriculation sous la forme AA-BBBB : ")
if validate_plate(plate):
    print("Plaque valide")
else:
    print("Plaque non valide")

