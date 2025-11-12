import string

def brute_force_cesar(texte_chiffre):
    alphabet = string.printable
    for decalage in range(len(alphabet)):
        resultat = ""
        for caractere in texte_chiffre:
            if caractere in alphabet:
                index = alphabet.index(caractere)
                index_decale = (index - decalage) % len(alphabet)
                resultat += alphabet[index_decale]
            else:
                resultat += caractere
        print(f"Décalage {decalage} : {resultat}")


texte_chiffre = "GtsotzwQjRtsij678&"
brute_force_cesar(texte_chiffre)