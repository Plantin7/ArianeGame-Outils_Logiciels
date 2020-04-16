6 - Modules
===========

# Importer des modules

On peut importer des modules en python

```
import math
print(math.sqrt(16))  # => 4.0
```
# Importer des fonctions spécifiques d'un module
On peut importer des fonctions spécifiques d'un module

```
from math import ceil, floor
print(ceil(3.7))  # => 4.0
print(floor(3.7))   # => 3.0
```
# Raccourcir un nom de module
On peut raccourcir un nom de module
```
import math as m
math.sqrt(16) == m.sqrt(16)   # => True
```
# Ecrire vos propres modules
```
Les modules Python sont juste des fichiers Python.
Vous pouvez écrire les vôtres et les importer. Le nom du module est le nom du fichier.
```
