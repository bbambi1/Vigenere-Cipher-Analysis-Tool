# --------------------------------------- TP Cryptographie --------------------------------------------------


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Liste contenant la fréquence relative de chaque lettre en anglais
frequence_lettres_anglais = [0.0808, 0.0167, 0.0318, 0.0399, 0.1256, 0.0217, 0.018, 0.527, 0.0724, 0.0014, 0.0063,
                             0.0404, 0.0260, 0.0738, 0.0747, 0.0191, 0.0009, 0.0642, 0.0659, 0.0915, 0.0279, 0.01,
                             0.0189, 0.0021, 0.0165, 0.0007]

LongueurCleMax = 25
LongueurCleMin = 5

IC_anglais = 0.065


# --------------------------------------------------------------------------------------------------------------------------------
# Calcul de la longueur de la cle
# --------------------------------------------------------------------------------------------------------------------------------

# Renvoie une liste des distances entre les sequences repetees (de 5 a 10 caracteres)

def get_RepeatingSquences_Spacings(message):
    distances = list()
    len_texte = len(message)
    for longueur_sequence in range(5, 11):
        for debut_sequence in range(0, (len_texte - longueur_sequence)):
            sequence = message[debut_sequence: debut_sequence + longueur_sequence]
            # On calcule l'indice de la 1re repetition de la sequence
            indice_occurrence = message[debut_sequence + 1:].find(sequence) + 1
            # .find() renvoie -1 si aucune repetition n'est trouvee
            if indice_occurrence >= 1:
                distances.append(indice_occurrence)
    return distances


# Renvoie la liste des diviseurs d'un nombre compris entre les longueurs min et max de la cle
def getDividers(nombre):
    diviseurs = list()
    for diviseur in range(LongueurCleMin, LongueurCleMax + 1):
        if nombre % diviseur == 0:
            diviseurs.append(diviseur)
    return diviseurs


# Etant donne une liste, on retourne une liste de couples (valeur, nb d'occurrences de "valeur" dans la liste)
# triee selon l'ordre decroissant des occurrences
def getOccurrences(liste):
    res = [(x, liste.count(x)) for x in set(liste)]
    res.sort(key=lambda x: x[1], reverse=True)
    return res


# Calcul de l'indice de coincidence d'un texte

def IndiceCoincidence(texte):
    occurrence = dict()
    n = len(texte)
    for char in texte:
        if char in occurrence:
            occurrence[char] += 1
        else:
            occurrence[char] = 1
    indice_coincidence = 0
    for char in occurrence:
        indice_coincidence += (occurrence[char] * (occurrence[char] - 1)) / (n * (n - 1))
    return indice_coincidence


# Renvoie la longueur probable de la cle

def LongueurCleProbable(message):
    MeilleureLongueur = 0
    # On cree une liste avec les distances entre sequences repetees
    DistancesSequences = get_RepeatingSquences_Spacings(message)
    # Liste qui va contenir tous les diviseurs des distances entre sequences repetees
    diviseursDistancesSequences = list()
    for distance in DistancesSequences:
        diviseursDistancesSequences.extend(getDividers(distance))
    # Liste qui va contenir les longueurs et leurs nb d'occurrences
    LongueursOccurrences = getOccurrences(diviseursDistancesSequences)
    # On retient le nb d'occurrences de la longueur qui divise le plus de distances
    maxOccurrence = LongueursOccurrences[0][1]
    # On cree une liste avec les "meilleures" longueurs (les plus probables)
    LongueursProbables = list()
    for couple in LongueursOccurrences:
        if couple[1] == maxOccurrence:
            LongueursProbables.append(couple[0])
    # On utilise notre heuristique pour choisir entre les longueurs probables
    # On retient la longueur qui donne l'IC le plus proche de l'anglais
    indice = 0
    for longueur in LongueursProbables:
        # On construit le sous_texte T1
        sous_texte1 = message[1::longueur]
        IC_T0 = IndiceCoincidence(sous_texte1)
        if IC_T0 >= indice:
            indice = IC_T0
            MeilleureLongueur = longueur
    return MeilleureLongueur


# Autre methode pour trouver la longueur de la cle (avec les Indices de Coincidence)

# def LongueurCleProbable_withIC(message) :
#     ListeLongueurs = list()
#     for longueur in range(LongueurCleMin, LongueurCleMax + 1) :
#         texte = get_SousTexte_i(0, message, longueur)
#         IC_texte = IndiceCoincidence(texte)
#         ListeLongueurs.append(abs(IC_texte - IC_anglais))
#     return ListeLongueurs.index(min(ListeLongueurs)) + LongueurCleMin


# --------------------------------------------------------------------------------------------------------------------------------
# Decouverte de la cle
# --------------------------------------------------------------------------------------------------------------------------------


# Renvoie le sous texte Ti tq Ti = T[i], T[i+longueurCle], T[i+2longueurCle]...
# (Attention!!! on va de T0 a Tn-1)

def get_SousTexte_i(i, message, longueurCle):
    lettres = message[i:: longueurCle]
    return lettres


# --------------------------------------------------------------------------------------------------------------------------------
# Analyse de frequence (a commenter ou decommenter si on veut tester cette methode ou non)
# --------------------------------------------------------------------------------------------------------------------------------


# Analyse de frequence (on calcule les ecarts relatifs des frequences avec une loi de Khi-2)
# En realite le choix de la statistique importe peu. L'algorithme marche tout aussi bien
# en faisant simplement la difference des frequences en valeur absolue

def analyse_frequence(sous_texte):
    n = len(sous_texte)
    all_differences = [0] * 26
    # Pour chaque decalage, on calcule la frequence des lettres du sous_texte decode avec ce decalage
    for i in range(26):
        ecart_global = 0
        # sous_texte en clair
        decalage_sequence = [chr(((ord(sous_texte[j]) - ord('A') - i) % 26) + ord('A')) for j in range(len(sous_texte))]
        frequence_lettre_sequence = [0] * 26
        # On calcule la frequence de chaque lettre du sous_texte en clair
        for lettre in decalage_sequence:
            frequence_lettre_sequence[ord(lettre) - ord('A')] += 1 / n
        # On calcule l'ecart (global) entre les frequences obtenues pour les lettres du sous_texte et leurs
        # frequences en anglais (avec une statistique du Khi-2 par exemple)
        for k in range(26):
            ecart_global += ((frequence_lettre_sequence[k] - frequence_lettres_anglais[k]) ** 2) / (
                frequence_lettres_anglais[k])
            # On peut aussi calculer une simple difference en valeur absolue
            # ecart_global += abs(frequence_lettre_sequence[k] - frequence_lettres_anglais[k])
        # Pour chaque decalage i, on enregistre l'ecart global obtenu
        all_differences[i] = ecart_global
    # Le bon decalage est celui avec le plus petit ecart
    decalage = all_differences.index(min(all_differences))
    return chr(decalage + ord('A'))


# Renvoie la cle probable a partir de la longueur obtenue

def DecouverteCle(message, longueurCle):
    cle = str()
    for i in range(longueurCle):
        sous_texte = get_SousTexte_i(i, message, longueurCle)
        cle += analyse_frequence(sous_texte)
    return cle


# --------------------------------------------------------------------------------------------------------------------------------
# Indice de coincidence (a commenter ou decommenter si on veut tester cette methode ou non)
# --------------------------------------------------------------------------------------------------------------------------------


# # Applique un decalage d sur le texte en argument (chiffrement monoalphabetique)
#
# def DecalageTexte_d(texte, d):
#     texte_final = str()
#     for char in texte:
#         texte_final += chr(((ord(char) - ord('A') + d) % 26) + ord('A'))
#     return texte_final
#
#
# # Renvoie la cle qui possede la plus grande valeur dans un dictionnaire
#
# def KeyWithMaxValue(dictionnaire):
#     return max(dictionnaire, key=lambda k: dictionnaire[k])
#
#
# # Renvoie la cle probable a partir de la longueur obtenue et des indices de coincidence
#
# def DecouverteCle(message, longueurCle):
#     # On determine T0
#     sous_texte0 = get_SousTexte_i(0, message, longueurCle)
#     all_decalages = [0]
#     # On cree un texte qui va contenir T0 qu'on concatene avec tous les Ti auxquels on applique leur decalage relatif)
#     texte_avec_decalages_relatifs = sous_texte0
#     # On cherche les decalages relatifs pour chaque "lettre" de la cle
#     for i in range(1, longueurCle):
#         indice = 0
#         decalage = 0
#         # On determine Ti
#         sous_textei = get_SousTexte_i(i, message, longueurCle)
#         # On s'interesse au decalage qui maximise l'IC de T0 + Ti(auquel on applique le decalage)
#         for d in range(26):
#             # On concatene T0 avec Ti auquel on applique le decalage d
#             t = sous_texte0 + DecalageTexte_d(sous_textei, d)
#             IC_t = IndiceCoincidence(t)
#             # On retient le decalage qui correspond au plus grand IC
#             if IC_t > indice:
#                 indice = IC_t
#                 decalage = d
#         texte_avec_decalages_relatifs += DecalageTexte_d(sous_textei, decalage)
#         all_decalages.append(decalage)
#     occurrences = {}
#     # On cherche le caractere le plus frequent dans le texte qu'on a construit
#     for char in texte_avec_decalages_relatifs:
#         if char in occurrences:
#             occurrences[char] += 1
#         else:
#             occurrences[char] = 1
#     # Le caractere le plus frequent correspond a la lettre E
#     plus_frequent_char = KeyWithMaxValue(occurrences)
#     # On determine ainsi le decalage global (en faisant attention au cas ou l'ecart entre le plus
#     # frequent caractere et E est negatif, et en veillant a ne jamais depasser 26 (exclus))
#     dg = (26 + ord(plus_frequent_char) - ord('E')) % 26
#     cle = str()
#     for d in all_decalages:
#         # On retire, pour chaque lettre de la cle, son decalage relatif
#         cle += alphabet[((26 + dg - d) % 26)]
#     return cle


# --------------------------------------------------------------------------------------------------------------------------------
# Code Vigenere
# --------------------------------------------------------------------------------------------------------------------------------


# Algorithme de Vigenere

def code_vigenere(message, cle, to_decode=False):
    texte_sortie = str()
    n = len(message)
    for i in range(n):
        d = ord(cle[i % len(cle)]) - ord('A')
        if to_decode:
            texte_sortie += chr((ord(message[i]) - ord('A') - d) % 26 + ord('A'))
        else:
            texte_sortie += chr((ord(message[i]) - ord('A') + d) % 26 + ord('A'))
    return texte_sortie


# Fonction qui encode un texte (sans espace et en majuscule)

def encode_vigenere(texte):
    print("\n-------------- Encodage --------------")
    cle = input("Entrez la cle :\n")
    while (not cle.isalpha()) or (not cle.isupper()):
        print("La cle rentree n'est pas valide.\nN'utilisez que des lettres en majuscule")
        cle = input("Entrez la cle :\n")
    return code_vigenere(texte, cle)


# Fonction qui decode un texte en connaissant la cle

def decode_vigenere_withKey(encoded_texte, cle):
    return code_vigenere(encoded_texte, cle, True)


# Fonction qui decode un texte sans avoir la cle

def decode_vigenere(message):
    print("\n-------------- Decodage --------------")
    KeyKnown = input("Connaissez-vous la cle ? - Repondez OUI ou NON\n")
    while (KeyKnown.upper() != "OUI") and (KeyKnown.upper() != "NON"):
        print("La reponse rentree est invalide.\n")
        KeyKnown = input("Connaissez-vous la cle ? - Repondez OUI ou NON\n")
    if KeyKnown.upper() == "OUI":
        cle = input("Entrez la cle :\n")
        while (not cle.isalpha()) or (not cle.isupper()):
            print("La cle rentree n'est pas valide.\nN'utilisez que des lettres en majuscule")
            cle = input("Entrez la cle :\n")
        return decode_vigenere_withKey(message, cle)
    print("Tentative de decodage sans la cle...")
    LongueurProbable = LongueurCleProbable(message)
    cle_trouvee = DecouverteCle(message, LongueurProbable)
    message_decode = decode_vigenere_withKey(message, cle_trouvee)
    return message_decode


# ----------------------------------------------------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------------------------------------------------


# ---------------------------------------- Fichier test 1 (901 chars) ----------------------------------------

# print("------------ Fichier test 1 --------------")
#
#
# texte1 = open("Test1.txt").read()
#
#
# encoded_texte1 = Vigenere.encode_vigenere(texte1)
# decoded_texte1 = Vigenere.decode_vigenere(encoded_texte1)
# longueurCle1 = Vigenere.LongueurCleProbable(encoded_texte1)
# cle_found1 = Vigenere.DecouverteCle(encoded_texte1, longueurCle1)
# # assert(texte1 == decoded_texte1)
#
#
# print("Longueur de la clé : ", longueurCle1)
# print("Clé probable : \n", cle_found1, sep="")


# ---------------------------------------- Fichier test 2 (3021 chars)  ----------------------------------------

# print("------------ Fichier test 2 --------------")
#
#
# texte2 = open("Test2.txt").read()
#
#
# encoded_texte2 = Vigenere.encode_vigenere(texte2)
# decoded_texte2 = Vigenere.decode_vigenere(encoded_texte2)
# longueurCle2 = Vigenere.LongueurCleProbable(encoded_texte2)
# cle_found2 = Vigenere.DecouverteCle(encoded_texte2, longueurCle2)
# # assert(texte2 == decoded_texte2)
#
#
# print("Longueur de la clé : ", longueurCle2)
# print("Clé probable : \n", cle_found2, sep="")


# ---------------------------------------- Fichier prof (786 chars) ----------------------------------------

# print("------------ Fichier prof --------------")
#
#
# texte_prof = open("TestProf.txt").read()
#
# longueurCle_prof = Vigenere.LongueurCleProbable(texte_prof)
# cle_found_prof = Vigenere.DecouverteCle(texte_prof, longueurCle_prof)
# decoded_texte_prof = Vigenere.decode_vigenere(texte_prof)
#
#
# print("Longueur de la clé : ", longueurCle_prof)
# print("Clé probable : ", cle_found_prof)
# print("Texte en clair :\n", decoded_texte_prof, sep="")
