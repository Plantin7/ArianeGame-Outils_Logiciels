1 - Types primitifs et opérateurs
=========================

# Les types primitifs

## Les entiers type int
Un int s'écrit avec les chiffres de 0 à 9. Il y a 3 manières d'écrires un int :
* la base décimale : le littéral devra commencer par un chiffre entre 1 et 9
* la base octale (base 8) : le littéral devra commencer par 0 suivi de chiffres de 0 à 7
* la base hexadécimale (base 16): le littéral devra commencer par 0x suivi de chiffres de 0 à 9 et de lettres de A à F (en minuscule ou majuscule)

Exemples : 

```
x=1
x=0
x=-33
x=4566
x=2147483647
x=076 #équivalent à x=62
x=0xFF #équivalent à x=255
x=0xa1 #équivalent à x=161
```
## Les entiers type long
Il existe deux manières d'utiliser des long :
* il faut rajouter L ou l à la fin d'un littéral entier pour qu'il soit automatiquement long
* lorsque le résultat d'une opération dépasse la capacité de stockage d'un int, alors, ce résultat est automatiquement convertit en long

Exemples :

```
x=1L
x=-45l
x=121212121212121212121212121 #Automatiquement converti en long
x=2147483647+1
```
## Les nombres virgules flotantes (float)
On déclare un flotant par caractère point pour indiquer la séparation entre la partie entière et la partie décimale ou la lettre 'e' ou 'E' pour spécifier l'exposant. 

Exemples : 
```
x = 1.234
x = 1.0 #Notons qu'un entier peut être un flottant
x = 1.
x = 1.234e54 
x = 1.234E54
x = -1.454e-2
```

## Les booléens
En python les booléens s'écrivent comme suit :
```
True
False
```
# Les Opérateurs Mathématiques
|    Symboles      |     Opération      |  Types                             |
|  :------------:  |   :-------------:  | :-------------:                    | 
| **+**            |   Addition         | entier, réel, chaîne de caractères |
| **-**            |   Soustraction     | entier, réel                       |
| **`*`**          |   Multiplication   | entier, réel, chaîne de caractères |
| **`**`**         |   Puissance        | entier, réel                       |
| **/**            |   Division         | entier, réel                       |
| **//**           |   Division entière | entier, réel                       |
| **%**            |   Modulo           | entier, réel                       |

Exemple :

```
# Les calculs sont ce à quoi on s'attend
1 + 1  # => 2
"a" + "b"== "ab" 
8 - 1  # => 7
10 * 2  # => 20

# Sauf pour la division qui retourne un float (nombre à virgule flottante)
35 / 5  # => 7.0
6/4 == 1 (Python 2) 1.5 (Python 3)
6./4 == 1.5 

# Résultats de divisions entières tronqués pour les nombres positifs et négatifs
5 // 3     # => 1
5.0 // 3.0 # => 1.0 # works on floats too
-5 // 3  # => -2
-5.0 // 3.0 # => -2.0

# Quand on utilise un float, le résultat est un float
3 * 2.0 # => 6.0
3 * "s" == "sss" 

# Modulo (reste de la division)
7 % 3 # => 1

# Exponentiation (x**y, x élevé à la puissance y)
2**4 # => 16

# Forcer la priorité de calcul avec des parenthèses
(1 + 3) * 2  # => 8
```

# Les Opérateurs Logiques 

Les expressions avec un opérateur logique sont évaluées à "True" ou "False".

* A **or** B (OU Logique) :
Si A est Vrai alors B n'est pas évalué, sinon l'expression est évalué à la valeur booléenne  de B

* A **and** B (ET Logique) :
Si A est Faux alors l'expression est fausse et B n'est pas évalué, sinon l'expression est évalué à la valeur booléenne de B

* **not** B (NON Logique) :
Si A est Faux alors **not** est Vrai et vice versa

Exemples : 

```
# Opérateurs booléens
True and False #=> False
False or True #=> True

# Négation avec not
not True  # => False
not False  # => True

# Utilisation des opérations booléennes avec des entiers :
0 and 2 #=> 0
-5 or 0 #=> -5
0 == False #=> True
2 == True #=> False
1 == True #=> True
```
# Les Opérateurs de comparaison
Tout comme les opérateurs logiques, les opérateurs de comparaison renvoient une valeur booléenne "True" ou "False".

|    Opérateurs    |     Description                             |
|  :------------:  |   :-------------:                           |
| **<**            |   strictement inférieur                     |
| **>**            |   strictement supérieur                     |
| **<=**           |   inférieur ou égal                         |
| **>=**           |   supérieur ou égal                         |
| **==**           |   égal                                      |
| **!=**           |   différent                                 |
| **<>**           |   différent, on utilisera de préférence !=  |
| **A is B**       |   A et B représentent le même objet.        |
| **A is not B**   |   A et B ne représentent pas le même objet. |

Il est possible d'enchaîner les opérateurs : X < Y < Z, c'est Y qui est pris en compte pour la comparaison avec Z et non pas l'évaluation de (X < Y)

Exemple : 

```
# On vérifie une égalité avec ==
1 == 1  # => True
2 == 1  # => False

# On vérifie une inégalité avec !=
1 != 1  # => False
2 != 1  # => True

# Autres opérateurs de comparaison
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# On peut enchaîner les comparaisons
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) is vérifie si deux variables pointent sur le même objet, mais == vérifie
# si les objets ont la même valeur.
a = [1, 2, 3, 4] # a pointe sur une nouvelle liste, [1, 2, 3, 4]
b = a # b pointe sur a
b is a # => True, a et b pointent sur le même objet
b == a # => True, les objets a et b sont égaux
b = [1, 2, 3, 4] # b pointe sur une nouvelle liste, [1, 2, 3, 4]
b is a # => False, a et b ne pointent pas sur le même objet
b == a # => True, les objets a et b ne pointent pas sur le même objet

```
Pour creer des listes voir : [Variables et Collections](2_Variables_et_Collections.md)
