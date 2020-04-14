1 - Types primitifs et opérateurs
=========================

# Les types primitifs


# Les booléens
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
8 - 1  # => 7
10 * 2  # => 20

# Sauf pour la division qui retourne un float (nombre à virgule flottante)
35 / 5  # => 7.0

# Résultats de divisions entières tronqués pour les nombres positifs et négatifs
5 // 3     # => 1
5.0 // 3.0 # => 1.0 # works on floats too
-5 // 3  # => -2
-5.0 // 3.0 # => -2.0

# Quand on utilise un float, le résultat est un float
3 * 2.0 # => 6.0

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
