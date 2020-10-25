# --------------------------------------- TTraitement de texte --------------------------------------------------


import re


# Retire les espaces et les caracteres speciaux d'un texte

def TraitementTexte(texte):
    texte_final = re.sub("[^A-Za-z]+", '', texte)
    texte_final = texte_final.upper()
    return texte_final


# Changer les "filename" par le nom du fichier

# texte = open("filename.txt").read()
# texte = TraitementTexte(texte)
#
# file = open("filename_treated.txt", "w")
# file.write(texte)
# file.close()
