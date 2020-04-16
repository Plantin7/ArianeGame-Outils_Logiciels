4 - Fonctions
=============

# Creer une foncion

On utilise "def" pour créer des fonctions
```
def add(x, y):
    print("x est {} et y est {}".format(x, y))
    return x + y    # On retourne une valeur avec return
    
# Appel d'une fonction avec des paramètres :
add(5, 6)   # => affiche "x est 5 et y est 6" et retourne 11

# Une autre manière d'appeler une fonction : avec des arguments
add(y=6, x=5)   # Les arguments peuvent être dans n'importe quel ordre.
```
# Retourner plusieurs valeurs
Il est possible en python de retourner plusieurs valeurs.

```
def maFonction(n):
    a = 2 + n
    b = 3 * n
    return a, b
```
# Fonction avec des argument optionel 
```
def maFonction (a = 10, b = 20):
     return a + b # => 30
```

# Définir une fonction qui prend un nombre variable d'arguments

```
def varargs(*args):
    return args

varargs(1, 2, 3)   # => (1, 2, 3)
```

# Définir une fonction qui prend un nombre variable de paramètres.
```
def keyword_args(**kwargs):
    return kwargs
    
keyword_args(big="foot", loch="ness")   # => {"big": "foot", "loch": "ness"}
```
# La portée des fonctions
```
x = 5

def setX(num):
    # La variable locale x n'est pas la même que la variable globale x
    x = num # => 43
    print (x) # => 43

def setGlobalX(num):
    global x
    print (x) # => 5
    x = num # la variable globale x est maintenant 6
    print (x) # => 6

setX(43)
setGlobalX(6)

```
# Les fonctions anonymes
```
(lambda x: x > 2)(3)   # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1) # => 5

filter(lambda x: x > 5, [3, 4, 5, 6, 7])   # => [6, 7]
```
