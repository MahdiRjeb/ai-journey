# Résumé Python : List, Tuple, Set et Dictionary

Voici une fiche de révision structurée avec la définition, les fonctions principales, les exemples et les utilisations réelles de chaque structure de données.

## 1. Liste — `list`

Définition : une collection ordonnée et modifiable qui accepte les doublons.

Syntaxe

Modifiable

Python

Run

```
fruits = ["apple", "banana", "apple"]
```

Les éléments ont un index : 0, 1, 2...

### Fonctions principales

| Fonction       | Rôle                              | Exemple                     |
| -------------- | --------------------------------- | --------------------------- |
| `append(x)`    | Ajouter à la fin                  | `fruits.append("orange")`   |
| `insert(i, x)` | Ajouter à un index                | `fruits.insert(1, "mango")` |
| `remove(x)`    | Supprimer une valeur              | `fruits.remove("banana")`   |
| `pop(i)`       | Supprimer et retourner un élément | `fruits.pop(0)`             |
| `clear()`      | Vider la liste                    | `fruits.clear()`            |
| `index(x)`     | Trouver l'index                   | `fruits.index("apple")`     |
| `count(x)`     | Compter les occurrences           | `fruits.count("apple")`     |
| `sort()`       | Trier la liste                    | `fruits.sort()`             |
| `reverse()`    | Inverser l'ordre                  | `fruits.reverse()`          |
| `len(L)`       | Nombre d'éléments                 | `len(fruits)`               |

Autres opérations utiles :

Python

Run

```
fruits[0]             # Accéder au premier élément
fruits[1] = "pear"    # Modifier un élément
"apple" in fruits     # Vérifier l'existence
```

Où utiliser une liste ?

* Liste de produits dans une boutique en ligne.

* Notes des étudiants.

* Historique de messages.

* Tâches à effectuer.

* Résultats d'une API.

## 2. Tuple — `tuple`

Définition : une collection ordonnée et immuable. Après sa création, on ne peut pas modifier, ajouter ou supprimer directement ses éléments.

Syntaxe

Immuable

Python

Run

```
user = ("Sara", 20, "Tunis")
```

Les éléments ont aussi des index, à partir de 0.

### Fonctions et opérations principales

| Fonction   | Rôle                                 | Exemple                  |
| ---------- | ------------------------------------ | ------------------------ |
| `count(x)` | Compter les occurrences              | `user.count(20)`         |
| `index(x)` | Trouver l'index                      | `user.index(20)`         |
| `len(T)`   | Nombre d'éléments                    | `len(user)`              |
| `in`       | Vérifier l'existence                 | `"Sara" in user`         |
| Indexation | Lire un élément                      | `user[0]`                |
| Déballage  | Affecter les valeurs à des variables | `name, age, city = user` |

Exemple :

Python

Run

```
user = ("Sara", 20, "Tunis")

print(user[0])  # Sara
print(user[1])  # 20

# user[1] = 21  # Erreur : tuple immuable
```

Un tuple à un seul élément doit contenir une virgule :

Python

Run

```
x = ("Tunis",)  # Tuple
```

Où utiliser un tuple ?

* Coordonnées : `(latitude, longitude)`.

* Adresse IP et port : `("192.168.1.10", 443)`.

* Certaines lignes retournées par une base de données.

* Retourner plusieurs valeurs depuis une fonction.

* Paires clé-valeur obtenues avec `dictionary.items()`.

Important : si l'âge d'un utilisateur change dans une base de données, tu peux récupérer un nouveau tuple contenant le nouvel âge. L'ancien tuple, lui, ne change pas.

## 3. Ensemble — `set`

Définition : une collection modifiable de valeurs uniques. Les doublons sont automatiquement éliminés et les éléments ne sont pas accessibles par index.

Syntaxe

Python

Run

```
fruits = {"apple", "banana", "apple"}
print(fruits)  # {'apple', 'banana'}
```

Pour créer un ensemble vide, utilise `set()`, et non `{}`.

### Fonctions principales

| Fonction / opération | Rôle                            | Exemple                  |
| -------------------- | ------------------------------- | ------------------------ |
| `add(x)`             | Ajouter un élément              | `fruits.add("mango")`    |
| `remove(x)`          | Supprimer, erreur si absent     | `fruits.remove("apple")` |
| `discard(x)`         | Supprimer sans erreur si absent | `fruits.discard("kiwi")` |
| `pop()`              | Retirer un élément arbitraire   | `fruits.pop()`           |
| `clear()`            | Vider l'ensemble                | `fruits.clear()`         |
| `len(S)`             | Nombre d'éléments               | `len(fruits)`            |
| `in`                 | Vérifier l'existence            | `"apple" in fruits`      |

### Opérations entre ensembles

Python

Run

```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

| Opération             | Signification                       | Résultat             |
| --------------------- | ----------------------------------- | -------------------- |
| <code>A \\\| B</code> | Union : tous les éléments           | `{1, 2, 3, 4, 5, 6}` |
| `A & B`               | Intersection : éléments communs     | `{3, 4}`             |
| `A - B`               | Différence : dans A, pas dans B     | `{1, 2}`             |
| `A ^ B`               | Différence symétrique : non communs | `{1, 2, 5, 6}`       |

Où utiliser un ensemble ?

* Éliminer les doublons d'une collection.

* Garder des identifiants uniques.

* Trouver les étudiants présents dans deux groupes.

* Comparer les permissions ou les rôles.

* Vérifier rapidement si une valeur existe.

Exemple pour supprimer les doublons :

Python

Run

```
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)

print(unique_numbers)  # {1, 2, 3, 4}
```

## 4. Dictionnaire — `dict`

Définition : une collection modifiable de paires clé → valeur. Chaque clé est unique et sert à retrouver sa valeur.

Syntaxe

Python

Run

```
student = {
    "name": "Sara",
    "age": 20
}
```

Ici, `"name"` et `"age"` sont les clés.

### Fonctions et opérations principales

| Fonction / opération | Rôle                                 | Exemple                       |
| -------------------- | ------------------------------------ | ----------------------------- |
| `d[key]`             | Lire une valeur                      | `student["name"]`             |
| `get(key)`           | Lire sans erreur si la clé manque    | `student.get("phone")`        |
| `get(key, default)`  | Définir une valeur par défaut        | `student.get("phone", 0)`     |
| `d[key] = value`     | Ajouter ou modifier                  | `student["age"] = 21`         |
| `pop(key)`           | Supprimer et retourner une valeur    | `student.pop("age")`          |
| `keys()`             | Obtenir les clés                     | `student.keys()`              |
| `values()`           | Obtenir les valeurs                  | `student.values()`            |
| `items()`            | Obtenir les paires                   | `student.items()`             |
| `update(d)`          | Ajouter ou modifier plusieurs paires | `student.update({"age": 22})` |
| `clear()`            | Vider le dictionnaire                | `student.clear()`             |
| `len(d)`             | Nombre de paires                     | `len(student)`                |

### Exemple important : compter des mots

Python

Run

```
text = "a b a c a b"
counts = {}

for word in text.split():
    counts[word] = counts.get(word, 0) + 1

print(counts)
# {'a': 3, 'b': 2, 'c': 1}
```

Explication :

1. `text.split()` sépare le texte en mots.

2. `counts.get(word, 0)` récupère le compteur, ou `0` si le mot est absent.

3. `+ 1` augmente le compteur.

4. `counts[word] = ...` crée la clé ou met à jour sa valeur.

Où utiliser un dictionnaire ?

* Informations d'un utilisateur.

* Données JSON reçues d'une API.

* Configuration d'un programme.

* Association d'un identifiant à un utilisateur.

* Comptage de fréquences.

## 5. Comparaison finale

| Caractéristique    | `list`                | `tuple`       | `set`           | `dict`                 |
| ------------------ | --------------------- | ------------- | --------------- | ---------------------- |
| Ordre conservé     | Oui                   | Oui           | Non garanti     | Oui, ordre d'insertion |
| Doublons           | Oui                   | Oui           | Non             | Clés uniques           |
| Modifiable         | Oui                   | Non           | Oui             | Oui                    |
| Accès par index    | Oui                   | Oui           | Non             | Non, accès par clé     |
| Syntaxe            | `[]`                  | `()`          | `{}` ou `set()` | `{clé: valeur}`        |
| Utilité principale | Collection modifiable | Valeurs fixes | Valeurs uniques | Clé → valeur           |

## 6. Comment choisir dans un projet réel ?

Liste — `list`

Je veux stocker plusieurs éléments, garder leur ordre et les modifier.

Exemple : panier de produits.

Tuple — `tuple`

Je veux regrouper quelques valeurs qui ne doivent pas changer.

Exemple : coordonnées GPS.

Ensemble — `set`

Je veux des valeurs uniques et comparer des groupes.

Exemple : identifiants uniques.

Dictionnaire — `dict`

Je veux retrouver une information grâce à une clé.

Exemple : ID d'un utilisateur → ses informations.

Le plus important à retenir :

* `list` = ordre et modification.

* `tuple` = ordre et immutabilité.

* `set` = unicité.

* `dict` = association clé-valeur.
