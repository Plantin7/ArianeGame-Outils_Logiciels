5 - Classes
===========

# Créer une classe 
On utilise l'opérateur "class" pour définir une classe
```
class Human:
    ...
```
# Le constructeur
Le constructeur est appelé quand la classe est instanciée.
```
def __init__(self, name):
# Assigner l'argument à l'attribut de l'instance
  self.name = name
```
# Une méthode d'instance
Une méthode de l'instance prend "self" comme premier argument.
```
def say(self, msg):
    return "{name}: {message}".format(name=self.name, message=msg)
```
# Les méthodes statiques
Une méthode statique est appelée sans référence à une instance ni à une classe. Elle est déclaré en dehors de la class
