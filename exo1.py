import random

mystery_number = random.randint(0, 123)

while True:
    guess = int(input("Devinez le nombre mystère (entre 0 et 123) : "))
    
    if guess == mystery_number:
        print("Bravo, vous avez trouvé le nombre mystère !")
        break
    elif guess < mystery_number:
        print("Le nombre que vous avez saisi est trop petit.")
    else:
        print("Le nombre que vous avez saisi est trop grand.")
