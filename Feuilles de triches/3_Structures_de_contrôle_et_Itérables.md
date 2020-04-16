3 - Structures de contrôle et Itérables
=======================================
Dans cette partie nous aborderons les structures de controles (if) et les itérables (for)
Je vous conseille d'avoir vu la fiche sur les [listes](2_Variables_et_Collections.md) pour suivre cette fiche

# if /elif /else

Voici une condition "if". L'indentation est significative en Python!

Exemple :
```
var = 5
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:    # La clause elif ("sinon si") est optionelle
    print("some_var is smaller than 10.")
else:                  # La clause else ("sinon") l'est aussi.
    print("some_var is indeed 10.")
```
# Itérer sur une liste
Pour parcourir une liste nous faisons comme suit :
```
"""
Les boucles "for" itèrent sur une liste
Affiche:
    chien est un mammifère
    chat est un mammifère
    souris est un mammifère
"""
for animal in ["chien", "chat", "souris"]:
    # On peut utiliser format() pour interpoler des chaînes formattées
    print("{} est un mammifère".format(animal))
```
# Itérer sur un dictionnaire
Pour parcourir un dictionnaire nous faisons comme suit :
```
filled_dict = {"one": 1, "two": 2, "three": 3}

# On peut boucler dessus
for i in filled_dict.keys():
    print(i)    # Affiche one, two, three
```

# Itérer avec le mot clé [range()](2_Variables_et_Collections.md)
Un exemple a déja été donné dans la fiche précedente mais le code ici est plus complet.
```
"""
"range(nombre)" retourne un itérable de nombres
de zéro au nombre donné
Affiche:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(debut, fin)" retourne un itérable de nombre
de debut à fin.
Affiche:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)

"""
"range(debut, fin, pas)" retourne un itérable de nombres
de début à fin en incrémentant de pas.
Si le pas n'est pas indiqué, la valeur par défaut est 1.
Affiche:
    4
    6
    8
"""
for i in range(4, 8, 2):
    print(i)
"""
```
# La boucle while()
La boucle while c'est comme une boucle for

```
Les boucles "while" bouclent jusqu'à ce que la condition devienne fausse.
Affiche:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # Raccourci pour x = x + 1
```

# Iterer sur chaque ligne d'un fichier 
On itère sur un fichier avec une boucle for
```
# Au lieu de try/finally pour nettoyer les ressources, on peut utiliser with
with open("myfile.txt") as f:
    for line in f:
        print(line)
 ```
 
 # L'objet itérable
 On peut creer un itéreteur sur un objet avec le mot clé iter()
 ```
filled_dict = {"one": 1, "two": 2, "three": 3}
it = filled_dict.keys
next(it)  #=> "one"

# Il garde son état quand on itère.
next(it)  #=> "two"
next(it)  #=> "three"

# Après que l'itérateur a retourné toutes ses données, il lève une exception StopIterator
next(it) # Lève une StopIteration
 ```
 
 # Creer une matrice
 ```
 Une autre manière d'utiliser les for pour creer une matrice
 [[o for _ in range(10)] for _ in range(10)]
 ```
 
 # Ajouter un compteur à un itérable : enumerate
```
l = ["eat","sleep","repeat"] 
  
for i, el in enumerate(l): 
    print (i) # 0 puis 1 puis 2
    print (el) # "eat", "sleep", "repeat"
```
