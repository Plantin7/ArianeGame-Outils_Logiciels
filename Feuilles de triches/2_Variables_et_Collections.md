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

# Les listes
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
Liste utiliser durant les différents exemples : 
```
# On déclare notre list
lst = [1, 2, 4, 3]
```
Accéder à une intervalle 
```
lst[1:3]  # => [2, 4]

```
Omettre les deux premiers éléments

```
li[2:]  # => [4, 3]
```
Prendre les trois premiers éléments 

```
lst[:3]  # => [1, 2, 4]
```
Sélectionner un élément sur deux 

```
lst[::2]   # =>[1, 4]
```
Avoir une copie de la liste à l'envers

```
li[::-1]   # => [3, 4, 2, 1]
```

Insertion d'un élément

```
mots[2:2] = [9] => [1, 2, 9, 4, 3] 
```

Suppression d'un élément

```
mots[1:3] = [9] => [1, 9, 3] (le 2 et le 4 ont été supprimés) 
```
## Copie de liste

Simple copie

```
new_lst = lst # => new_lst = [1, 2, 4, 3]
lst.append(9) # => lst = [1, 2, 4, 3, 9]
new_lst # => new_lst = [1, 2, 4, 3, 9]
```
Il existe une seul liste dans la mémoire de l'ordinateur, la nouvelle liste est seulement une nouvelle référence sur cette liste.

En utilisant des 'slices'

```
Fait une copie d'une profondeur 
new_lst = lst[:] # => lst = [1, 2, 4, 3] mais (new_lst is lst) vaut False.
```
## Modifier des String en list (voir rappel sur les [String](1_Types_primitifs_et_opérateurs.md))

Pour convertir une chaine de caractère en une sous liste de chaine on utilisera la méthode split()

```
chaine ="je suis une chaine"
lst_chaine = chaine.split() # => ['je', 'suis', 'une', 'chaine]

chaine = "Cet exemple, parmi d'autres, peut encore servir"
chaine.split(",") # => ['Cet exemple', " parmi d'autres", ' peut encore servir']
```
Pour rassemble une liste de chaînes en une seule chaine, on utilisera la méthode join()
```
arr = ["Salut", "les", "copains"]
print( " ".join(arr)) # =>Salut les copains
print("___".join(arr)) # => Salut___les___copains
```

# Les dictionnaires:
Les dictionnaires sont des collections dont chaque élément lui ai associé une clé  

Les clés des dictionnaires doivent être de types immuables  

Elles doivent être convertibles en une valeur constante pour une recherche rapide  


Comment déclarer un dictionnaire ? :
```
empty_dict = {}

# Un dictionnaire pré-rempli :
filled_dict = {"one": 1, "two": 2, "three": 3}

# Les types immuables incluent les ints, floats, strings et tuples.
invalid_dict = {[1,2,3]: "123"} # => Lève une TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}  # Par contre, les valeurs peuvent être de tout type.
```

## Les Opérations sur les dictionnaires

### Accès à un element
On trouve une valeur d'un dictionnaire avec []
```

my_dict = {"one": 1, "two": 2, "three": 3}
my_dict["one"]   # => 1
```
En utilisant les [] l'accès à une clé non-existente lève une KeyError, nous préferons utilisé la méthode get()

```
my_dict = {"one": 1, "two": 2, "three": 3}

# On utilise "get()" pour éviter la KeyError
my_dict.get("one")   # => 1
my_dict.get("four")   # => None
# La méthode get accepte une valeur de retour par défaut en cas de valeur non-existante.
my_dict.get("one", 4)   # => 1
my_dict.get("four", 4)   # => 4

````
### Insérer un element

Insérer une valeur dans un dictionnaire si la clé n'est pas présente.

```
my_dict = {"one": 1, "two": 2, "three": 3}
my_dict.setdefault("five", 5)  # my_dict["five"] devient 5
my_dict.setdefault("five", 6)  # my_dict["five"] est toujours 5
```
Ajouter à un dictionnaire
```
my_dict.update({"four":4}) #=> {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4  # une autre méthode
```

### Récuperer les clés / elements d'un dictionnaire
Pour récupérer les clés utilisés par un dictionnaire on utilise la méthode keys()
Pour récupérer les valeurs memorisées par un dictionnaire on utilise la méthode values()
Pour récupérer les clés et les valeurs d'un dictionnaire on utilise la méthode items()

```
my_dict = {"one": 1, "two": 2, "three": 3}
print (my_dict.keys()) => ['one', 'two', 'three']

Le mot clé list() pour avoir une liste Note: l'ordre n'est pas garanti.
list(filled_dict.keys())   # => ["three", "two", "one"]

print (my_dict.values()) => [1, 2, 3]
Là aussi, il faut utiliser list() pour avoir une liste.
Note : l'ordre n'est toujours pas garanti.
list(filled_dict.values())   # => [3, 2, 1]


#La méthode items() extrait du dictionnaire une liste équivalente de tuples
print (my_dict.items()) => [("one", 1), ("two", 2), ("three", 3)]
```

### Copier un dictionnaire
La méthode copy() permet d'effectuer une vraie copie d'un dictionnaire.

```
my_dict = {"one": 1, "two": 2, "three": 3}
new_dict = my_dict.copy()
new_dict["four"] = 4

my_dict # => {"one": 1, "two": 2, "three": 3}
new_dict # => {"one": 1, "two": 2, "three": 3, "four": 4}

```


# Les tuples:

## Les Opérations sur les tuples

# Les sets:

## Les Opérations sur les sets

# Les fonctions
Les fonctions suivantes s'appliquent sur les listes, les dictionnaires, les tuples et les set:

## Savoir si un element est dans une collection
Pour savoir si un element est dans une collection on utilise le mot clé in

```
lst = [1, 2, 4, 3]
2 in lst => True

my_dict = {"one": 1, "two": 2, "three": 3}
# On vérifie la présence d'une clé dans un dictionnaire avec "in"
"one" in my_dict   # => True
1 in my_dict   # => False

tup = (1, 2)
2 in tup => True

my_set = {3, 4, 5, 6}
2 in my_set => False
3 in my_set => True
```

## Connaitre la taille d'une collection
Pour connaitre la taille d'une collection on utilise le mot clé len()

```
lst = [1, 2, 4, 3]
len(lst) => 4

my_dict = {"one": 1, "two": 2, "three": 3}
len(my_dict) => 3

tup = (1, 2)
len(tup) => 2

my_set = {3, 4, 5, 6}
len(set) => 4
```
## Supprimer un élément d'une collection
Pour supprimer un élément d'une collection il existe le mot clé del

```
lst = [1, 2, 4, 3]
del lst[2] # => [1, 2, 3] 

my_dict = {"one": 1, "two": 2, "three": 3}
del my_dict["one"] => dict = {"two": 2, "three": 3}

tup = (1, 2, 3)
del tup[0] # => (2, 3)

On ne peut pas utiliser del sur des set, on utilisera la méthode remove() de set
my_set = {3, 4, 5, 6}
del set[1] => 'set' object doesn't support item deletion
```
## Minimun et maximun d'une collection
Pour récupérer le minimum et le maximum il existe deux méthodes
* min(ma_collection)
* max(ma_collection)

```
lst = [1, 2, 4, 3]
min(lst) => 1
max(lst) => 4

my_dict = {"one": 1, "two": 2, "three": 3}
min(my_dict) => "one"
max(my_dict) => "two"

tup = (1, 2, 3)
min(tup) => 1
max(tup) => 3

my_set = {3, 4, 5, 6}
min(tup) => 3
max(tup) => 6

```
## Manipuler des séquences de nombre
On peut créer des séquences de nombre avec la méthode range()

```
range(10) # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(5,13) # => [5, 6, 7, 8, 9, 10, 11, 12]
range(3,16,3) # => [3, 6, 9, 12, 15]

```

