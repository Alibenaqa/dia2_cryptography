import string
def chiffre_cesar(text, decalage):
    alphabet = string.printable
    result = " "
    for caractere in text:
        if caractere in alphabet:
         index = alphabet.index(caractere)
         index_decale = (index + decalage) % len(alphabet)
         result += alphabet[index_decale]
    else :
         result += caractere

         return result
def dechiffre_cesar(text, decalage):
    return chiffre_cesar(text, -decalage)


def brute_force_cesar(texte_chiffre):
    return dechiffre_cesar(text, decalage)
text = "Bonjour Le Monde 123!"
decalage = 10
print(dechiffre_cesar("GtsotzwQjRtsij678&", 5))