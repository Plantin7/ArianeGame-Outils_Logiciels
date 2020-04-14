1.Types primitifs et opérateurs
=========================

# Les types primitifs


# Les booléens
En python les booléens s'écrivent comme suit :
```
True
False
```

# Les Opérateurs Logiques 

Les expressions avec un opérateur logique sont évaluées à "True" ou "False".

* A **or** B (OU Logique) :
Si A est Vrai alors B n'est pas évalué, sinon l'expression est évalué à la valeur booléenne  de B

* A **and** B (ET Logique) :
Si A est Faux alors l'expression est fausse et B n'est pas évalué, sinon l'expression est évalué à la valeur booléenne de B

* **not** B (NON Logique) :
Si A est Faux alors **not** est Vrai et vice versa

Exemple : 

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
