Feuille de triche Python - Vincent Agullo
=========================
Dernière mise à jour: 07/04/2020


# Table of Contents
1. [Types primitifs et opérateurs](1_Types_primitifs_et_opérateurs.md)

# A ne pas oublier
The second paragraph text
1. Definir une fonction 
```
  def maFonction():
     # CODE
```
2. On lance le programme depuis le terminal avec `python3 Exercice1.py`

3. Les commentaires suivent un #

4. Les commentaires sur plusieurs lignes : on utilise les '''

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

```
fichier = open("to/path/file", "r") (r pour read, w pour write, rw pour read and write)
```
Autre manière :
fichier.readline

9. Une autre manière d'utiliser les for (matrice):
```
[[o for _ in range(10)] for _ in range(10)]
```

10. Ajouter un conteur à un itérable : Pour cela on utilise le mot clef enumerate
```
l = ["eat","sleep","repeat"] 
  
for el in enumerate(l): 
    print el

for count,el in enumerate(l, 100): 
    print count,el 
```

 11. Convertir des données en chaines de caractères:
 On utilise pour cela le mot clef "str()"

 12. Les puissances en python :
     On utilise les ** : ex 2 ** 3 = 8
 
 13. Les dictionnaires :
```
dict = {}

# Pour verifier si un élément est dans un dictionnaire 

if not value in dict :
   #TODO
```
14. Itérer sur deux listes en parallèle : 
```
for f, b in zip(foo, bar):
    print(f, b)
```
Le zip s'arrête lorsque le plus petit des foo ou bar s'arrête.
Zip retourne un itérateur de tuples

15. Taille d'une chaine de caractère :
```
len("MyWord")
```
16. Valeur absolue :
```
abs(1 - 2) # = 1
```
17. Récupérer tout les caractères d'une chaine de caractère sauf la première.
```
string = "String"
print(string[1:]) # print "tring"
```

18. Lire un fichier sans les caractères de fin de ligne :
```
f = open("file", 'r')
x = f.read().splitlines()
f.close()
```

19. Creer un fichier si il existe pas :
```
open('file.txt', 'w+')
```

20. Pour sauvegarder et charger un dictionnaire dans un fichier :

On utilise pour cela la librairie pickle.
```
with open('file.txt', 'wb') as f:
     pickle.dump(dict, f, pickle.HIGHEST_PROTOCOL)

with open('file.txt', 'rb') as f:
     dict = pickle.load(f)
```
