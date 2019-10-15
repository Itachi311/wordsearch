# HTTP service that provides an endpoint for fuzzy search / autocomplete of English words.

A Django based Word Search WebApp This WebApp basically renders a search box on browser where the user can type in a word as an input to search that word in a [dataset](https://drive.google.com/file/d/1dZdWIkjP6MNWFt-Umq8BfUU4AplpmRHX/view) containing 333,333 English words and the frequency of their usage in some corpus

## Objective:

1. Python app using Django framework that exposes a single endpoint
```GET /searchResults?word=<input> ```

## Setup:

1. To start a project in Django
```django-admin start project wordsearch ```
2. To start a new app in Django
```python manage.py startapp search_word```
3. ```-- wordsearch
    |-- README.md
    |-- db.sqlite3
    |-- manage.py
    |-- search_word
    |   |-- __init__.py
    |   |-- __pycache__
    |   |   |-- __init__.cpython-36.pyc
    |   |   |-- admin.cpython-36.pyc
    |   |   |-- models.cpython-36.pyc
    |   |   |-- search.cpython-36.pyc
    |   |   `-- views.cpython-36.pyc
    |   |-- admin.py
    |   |-- apps.py
    |   |-- migrations
    |   |   |-- __init__.py
    |   |   `-- __pycache__
    |   |       `-- __init__.cpython-36.pyc
    |   |-- models.py
    |   |-- search.py
    |   |-- templates
    |   |   `-- search.html
    |   |-- tests.py
    |   `-- views.py
    |-- word_search.tsv
    `-- wordsearch
        |-- __init__.py
        |-- __pycache__
        |   |-- __init__.cpython-36.pyc
        |   |-- settings.cpython-36.pyc
        |   |-- urls.cpython-36.pyc
        |   `-- wsgi.cpython-36.pyc
        |-- settings.py
        |-- urls.py
        `-- wsgi.py
        ```

## usage:

``` python manage.py runserver```


## search.py:

	contains the searching algorithm 


## Constrains:

1. Matches can occur anywhere in the string, not just at the beginning. For example, eryx should match archaeopteryx (among others).

2. We assume that the user is typing the beginning of the word. Thus, matches at the start of a word should be ranked higher. For example, for the input 		pract, the result practical should be ranked higher than impractical.

3. Common words (those with a higher usage count) should rank higher than rare words.

4. Short words should rank higher than long words. For example, given the input environ, the result environment should rank higher than environmentalism.

5. As a corollary to the above, an exact match should always be ranked as the first result.

6. The search algorithm you develop should ideally incorporate some form of a weighted average of all qualifying parameters. The perfect weights, in production systems, are however derived through the use of ML algorithms.
