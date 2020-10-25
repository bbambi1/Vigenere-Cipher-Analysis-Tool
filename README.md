# Chiffre de Vigenere

Un script Python qui retrouve la clé de chiffrement et le texte en clair à partir du texte chiffré en effectuant une analyse des indices de coïncidence.



## Installations et Usage

### Installations

Aucune bibliothèque n'a besoin d'être préalablement installée.

### Usage

1. Le fichier Python ("Vigenere_Bienvenu.py") doit se trouver dans le même répertoire (dossier) que le texte à coder/décoder. 
2. Ouvrez le terminal (cmd sous Windows) et utilisez "cd" pour pointer dans le répertoire où se trouvent les fichiers texte à encoder/décoder et le script Python.
3. Utilisez le drapeau "**-e**" pour encoder le fichier et "**-d**" pour décoder. 

En pratique, si les fichiers se trouvent dans le répertoire "*user*", on écrirait (notez les arguments et leur ordre) :
```
C:\Users\user>python Vigenere_Bienvenu.py -e texte.txt
```
si on souhaite **encoder** le fichier *texte.txt* 
```
C:\Users\user>python Vigenere_Bienvenu.py -d texte.txt
```
si on souhaite **décoder** le fichier *texte.txt*

Il ne restera plus qu'à suivre les instructions qui vont dérouler dans le terminal. 



## Retrouver la clé de chiffrement

Ce programme utilise une méthode en deux parties pour déterminer la clé de chiffrement. La première partie utilise la répétition de séquences identiques pour trouver la longueur de la clé, et la seconde partie utilise une analyse de fréquence pour trouver la clé réelle.



### 1. Longueur de la clé :

La première étape consiste à trouver chaque séquence d'au moins 3 lettres qui se répètent dans le texte crypté. Ces séquences pourraient indiquer qu'il s'agit des mêmes lettres du texte en clair chiffrées avec les mêmes sous-parties de la clé.

Après avoir trouvé les séquences répétées, il suffit de relever la "distance" (le nombre de caractères d'écart) entre chaque séquence.

Enfin, pour chaque longueur de clé possible, on s'intéresse à celle qui divise le plus de "distances répétées".



### 2. Découverte de la clé

Une fois la longueur de la clé déterminée, on peut retrouver la clé en utilisant les IC. 
Premièrement, on retrouve les décalages d_i pour lesquels les sous-textes T_1  ,…,T_(n-1)  concaténés chacun avec T_0 forment un texte qui coïncide avec l’anglais.
Il ne reste plus maintenant qu’a fixer l’origine. Pour cela on concatène tous les textes T_i chacun avec son décalage d_i et on cherche la lettre la plus fréquente qui va correspondre alors à "E" ; ce qui nous permet de fixer le décalage global d_g.
