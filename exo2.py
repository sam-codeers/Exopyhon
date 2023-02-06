x = int(input("Entrez le nombre de colonnes (X) : "))
y = int(input("Entrez le nombre de lignes (Y) : "))

if x < y:
    print("Le nombre de colonnes doit être supérieur au nombre de lignes.")
else:
    for i in range(y):
        print("@" * x)
