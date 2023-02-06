# definition de plaque

def validate_plate (plaque):
    if len(plaque) != 7:
        return False
    if not plaque[0:2].isdigit():
        return False
    if not plaque[3:7].isalpha():
        return False
    if plaque[2] != '-':
        return False
    return True

plate = input("Entrez une plaque d'immatriculation sous la forme AA-BBBB : ")
if validate_plate(plate):
    print("Plaque valide")
else:
    print("Plaque non valide")
