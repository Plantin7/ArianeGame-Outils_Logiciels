Feuille de triche Python
=========================
Dernière mise à jour: 03/03/2020


# A ne pas oublier

1. Definir une fonction 
```
  def maFonction():
     # CODE
```
2. On lance le programme depuis le terminal avec `python3 Exercice1.py`

3. Les commentaires suivent un #

6. Les commentaires sur plusieurs lignes : on utilise les '''

5. Le main en Python
```
if __name__ == '__main__':
# TODO
```
6. En python on peut retourner un couple de valeur dans une fonction. Rien de plus simple, il suffit de faire ceci :

```
def maFonction(n):
    # CODE
    return a, b
```

7. Argument Optionel 
```
def maFonction (a, b = 0):
    #TODO
```

8. Ouvrir un fichier :

fichier = open("to/path/file", "r") (r pour read, w pour write, rw pour read and write)

Autre manière :
fichier.readline

9. Une autre manière d'utiliser les for (matrice):
[[o for _ in range(10)] for _ in range(10)]

10. Ajouter un conteur à un itérable : Pour cela on utilise le mot clef enumerate
'''
l = ["eat","sleep","repeat"] 
  
for el in enumerate(l): 
    print el

for count,el in enumerate(l, 100): 
    print count,el 
 '''

 11. Convertir des données en chaines de caractères:
 On utilise pour cela le mot clef "str()"

 12. Les puissances en python :
     On utilise les ** : ex 2 ** 3 = 8
