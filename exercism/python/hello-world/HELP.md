# Help

## Exécute les tests

Nous utilisons [pytest][pytest: Getting Started Guide] comme exécuteur de tests sur notre site.
Tu devras installer `pytest` sur ta machine de développement si tu veux exécuter les tests du parcours Python en local.
Tu devrais aussi installer les plugins `pytest` suivants :

- [pytest-cache][pytest-cache]
- [pytest-subtests][pytest-subtests]

Tu trouveras des informations plus détaillées dans notre [guide des tests Python][Python track tests page] sur le site.

### Lance les tests

Pour exécuter les tests fournis, place-toi dans le dossier où se trouve l'exercice à l'aide de `cd` dans ton terminal (remplace `<exercise-folder-location>` ci-dessous par ton chemin).
Les fichiers de test se terminent généralement par `_test.py` et correspondent aux mêmes tests que ceux qui s'exécutent sur le site lorsqu'une solution est soumise.

Linux/MacOS
```bash
$ cd <path/to/exercise-folder-location>
```

Windows
```powershell
PS C:\Users\foobar> cd <path\to\exercise-folder-location>
```

<br>

Ensuite, exécute la commande `pytest` dans ton terminal, en remplaçant `<exercise_test.py>` par le nom du fichier de test :

Linux/MacOS
```bash
$ python3 -m pytest -o markers=task <exercise_test.py>
==================== 7 passed in 0.08s ====================
```

Windows
```powershell
PS C:\Users\foobar> py -m pytest -o markers=task <exercise_test.py>
==================== 7 passed in 0.08s ====================
```

### Options courantes
- `-o` : remplacer le fichier `pytest.ini` par défaut (tu peux t'en servir pour éviter les avertissements liés aux marqueurs)
- `-v` : activer la sortie détaillée.
- `-x` : arrêter l'exécution des tests dès le premier échec.
- `--ff` : réexécuter d'abord les tests qui ont échoué lors de l'exécution précédente, avant de lancer les autres cas de test.

Pour plus d'options, utilise `python3 -m pytest -h` ou `py -m pytest -h`.

### Corrige les avertissements

Si tu n'utilises pas `pytest -o markers=task` lorsque tu lances `pytest`, tu risques de recevoir un `PytestUnknownMarkWarning` pour les tests qui utilisent notre nouvelle syntaxe :

```bash
PytestUnknownMarkWarning: Unknown pytest.mark.task - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/mark.html
```

Pour éviter de taper `pytest -o markers=task` à chaque fois que tu lances les tests, tu peux utiliser un fichier de configuration `pytest.ini`.
Nous en avons créé un que tu peux télécharger depuis le répertoire racine du parcours Python : [pytest.ini][pytest.ini].

Tu peux aussi créer ton propre fichier `pytest.ini` avec le contenu suivant :

```ini
[pytest]
markers =
    task: A concept exercise task.
```

Placer le fichier `pytest.ini` dans le répertoire _root_ ou _working_ de tes exercices du parcours Python enregistrera les marqueurs et fera disparaître les avertissements.
Tu trouveras plus d'informations sur les marqueurs pytest dans la documentation de `pytest` sur le [marquage des fonctions de test][pytest: marking test functions with attributes] et dans la documentation de `pytest` sur [l'utilisation de marqueurs personnalisés][pytest: working with custom markers].

Tu trouveras des informations sur la personnalisation des configurations pytest dans la documentation de `pytest` sur les [formats de fichier de configuration][pytest: configuration file formats].

### Étends ton IDE ou ton éditeur de code

De nombreux IDE et éditeurs de code prennent en charge nativement `pytest` et d'autres outils de qualité du code.
Tu trouveras quelques options proposées par la communauté sur notre [page des outils du parcours Python][Python track tools page].

[Pytest: Getting Started Guide]: https://docs.pytest.org/en/latest/getting-started.html
[Python track tools page]: https://exercism.org/docs/tracks/python/tools
[Python track tests page]: https://exercism.org/docs/tracks/python/tests
[pytest-cache]:http://pythonhosted.org/pytest-cache/
[pytest-subtests]:https://github.com/pytest-dev/pytest-subtests
[pytest.ini]: https://github.com/exercism/python/blob/main/pytest.ini
[pytest: configuration file formats]: https://docs.pytest.org/en/6.2.x/customize.html#configuration-file-formats
[pytest: marking test functions with attributes]: https://docs.pytest.org/en/6.2.x/mark.html#raising-errors-on-unknown-marks
[pytest: working with custom markers]: https://docs.pytest.org/en/6.2.x/example/markers.html#working-with-custom-markers

## Soumets ta solution

Tu peux soumettre ta solution avec la commande `exercism submit hello_world.py`.
Cette commande enverra ta solution sur le site d'Exercism et affichera l'URL de la page de la solution.

Il est possible de soumettre une solution incomplète, ce qui te permet de :

- Voir comment d'autres personnes ont résolu l'exercice
- Demander l'aide d'un mentor

## Besoin d'aide ?

Si tu souhaites de l'aide pour résoudre l'exercice, consulte les pages suivantes :

- La [documentation du parcours Python](https://exercism.org/docs/tracks/python)
- La [catégorie de programmation du parcours Python sur le forum](https://forum.exercism.org/c/programming/python)
- La [catégorie de programmation d'Exercism sur le forum](https://forum.exercism.org/c/programming/5)
- Les [questions fréquentes](https://exercism.org/docs/using/faqs)

Si ces ressources ne suffisent pas, tu peux soumettre ta solution (incomplète) pour demander un mentorat.

Voici quelques ressources pour obtenir de l'aide si tu rencontres des difficultés :

- [La PSF](https://www.python.org) héberge les téléchargements de Python, la documentation et les ressources de la communauté.
- [Les forums de la communauté Python](https://discuss.python.org/) : entraide, discussions sur les PEP, les développeurs principaux de Python, et bien plus encore.
- [La communauté Exercism sur Discord](https://exercism.org/r/discord)
- [Les forums de discussion de la communauté Exercism](https://forum.exercsim.org)
- [La communauté Python sur Discord](https://pythondiscord.com/) est une communauté très utile et très active.
- [/r/learnpython/](https://www.reddit.com/r/learnpython/) est un subreddit destiné aux personnes qui apprennent Python.
- [#python sur Libera.chat](https://www.python.org/community/irc/) c'est là que se retrouvent les développeurs principaux du langage pour faire avancer le travail.
- [Les forums de la communauté Free Code Camp](https://forum.freecodecamp.org/)
- [Pythontutor](http://pythontutor.com/) pour dérouler pas à pas de petits extraits de code de façon visuelle.

De plus, [StackOverflow](http://stackoverflow.com/questions/tagged/python) est un bon endroit où chercher ton problème ou ta question pour voir si quelqu'un y a déjà répondu.
 Sinon, tu peux toujours [poser ta question](https://stackoverflow.com/help/how-to-ask) ou [répondre](https://stackoverflow.com/help/how-to-answer) à celle de quelqu'un d'autre.