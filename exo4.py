def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

text = input("Entrez un texte : ")
result = is_palindrome(text)
if result:
    print("Le texte est un palindrome.")
else:
    print("Le texte n'est pas un palindrome.")

