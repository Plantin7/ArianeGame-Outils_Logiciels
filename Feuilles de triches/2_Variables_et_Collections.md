2 - Variables et Collections
==========================


# Afficher du texte
En python il existe une fonction pour afficher du texte : print()
Note : Par défaut, la fonction print() affiche aussi une nouvelle ligne à la fin.

Exemple : 
```
print("Hello World !")
```
Il est possible d'utiliser le deuxième argument de la fonction print() pour changer de caractère de fin

```
# print le message sans aller à la ligne 
print("Hello World !", end="")

# le saut de ligne est remplacé par "!"
print("Hello, World", end="!") # => Hello, World!
```

# Les listes:
Les listes sont des collections d'objets séparés par des virgules.

Comment déclarer une liste ? :
```
lst = []

# Initialiser une liste pré-remplie
other_lst = [1, 2, 3]
```
Les éléments d'une liste peuvent contenir des types variés
```
other_lst = ['lundi', 'martin', 476, 3.65]
```

## Les Opérations sur les listes

### Accès à un element
Pour accéder à un élément d'une liste il suffit de faire comme suit :

```
# On déclare notre list
lst = [1, 7, 10]

lst[0] => 1

# Accès au dernier élément :
lst[-1]  # => 10

# Accéder à un élément en dehors des limites lève une IndexError
lst[3]  # Lève une IndexError

```

### Ajouter un element
La methode append() permet d'ajouter des objets à la fin d'une liste

```
# On déclare notre list
lst = []

# On ajoute des objets
lst.append(1)    # lst vaut maintenant [1]
lst.append(2)    # lst vaut maintenant [1, 2]
lst.append(4)    # lst vaut maintenant [1, 2, 4]
lst.append(3)    # lst vaut maintenant [1, 2, 4, 3]

```
### Supprimer un element
La methode pop(i) permet de retirer l'élément d'une liste à l'index i. Si i est vide on retire le dernière element.

```
# On déclare notre list
lst = [1, 2, 4, 3]

# On enlève des objets
lst.pop()     # lst vaut maintenant [1, 2, 4]
lst.pop(0)    # lst vaut maintenant [2, 4]
lst.pop(1)    # lst vaut maintenant [4]

```
## Autre manière de modifier les listes (Slicing)




# Les dictionnaires:

## Les Opérations sur les dictionnaires

# Les tuples:

## Les Opérations sur les tuples

# Les sets:

## Les Opérations sur les sets
