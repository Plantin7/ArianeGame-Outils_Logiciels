Feuille de triche Python - Vincent Agullo
=========================
Dernière mise à jour: 07/04/2020

Ces feuilles de triches ont pour but d'aborder les notions essentielles de python  
Il n'est pas impossible qu'il y est des erreurs. Si vous avez le moindre doute je vous invite à regarder sur internet et à me retourner les erreurs pour que je puisse les corriger  
Je vous souhaite une bonne lecture.

# Table of Contents
1. [Types primitifs et opérateurs](1_Types_primitifs_et_opérateurs.md)
2. [Variables et Collections](2_Variables_et_Collections.md)
2. [Structures de contrôle et Itérables](3_Structures_de_contrôle_et_Itérables.md)

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
6. En python on peut retourner un couple de valeur dans une fonction.

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

14. Itérer sur deux listes en parallèle : 
```
for f, b in zip(foo, bar):
    print(f, b)
```
Le zip s'arrête lorsque le plus petit des foo ou bar s'arrête.
Zip retourne un itérateur de tuples

16. Valeur absolue :
```
abs(1 - 2) # = 1
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
