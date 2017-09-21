<!-- $theme: gaia -->
<!-- page_number: false -->
<!-- footer: Péter Handbauer, version: 08/23 -->
<!-- $size: a1 -->

Python Training "2":
Useful parts
==============================

Tematika v1 (2017/II)
-----------------

---
<!-- footer: Python 2 tematika -->

## Story so far

 1. Ismétlések, gyorstalpaló
    - script nyelvi dolgok, típusgyengeség, alap szintaxis
    - háttér, nyelvi evolúció, interpreter
    - feljesztő eszközök, ajánlott IDE-k Pythonhoz, debugging, project Pythonban
    - hasznos `__builtin__` nyelvi eszközök (`dir()`, `help()`, `type(t)`, `any()`...) és lehetőségek (egysoros `(if else)`...)
    - adatszerkezet alapok, konverziók, tuple csomagolás és swap
 2. Adatszerkezetek
    - string, string formázás, file írás és olvasás
    - szekvenciák (`list`, `tuple`, `array`), felhasználásuk, trükkök
    - halmazok, dictionary, előnyök és hátrányok
    - iterálás collection típusokon, `iter`, `enumerate`, `zip`, keresés és feltöltés
    - típusok függvényekben, másolás vs referálás, `*args` és `**kwargs`
 3. Comprehensions
    - list comprehensions, feltételes, példák
    - kombinációs comprehension
    - szótár, halmaz
    - más lehetőségek, `itertools`
    - sebesség összehasonlítás, performancia elemző, PyPy és JIT
    - gyakorlatok
 4. Függvények mélyebben
    - függvény névterek, callstack, garbage collection
    - lambda függvények
    - generátorok, `yield`, Python 3 vonatkozások
    - generator expressions, kivétel ellenőrzés, `next`
    - dekorátorok, áttekintés
 5. Objektumok Pythonban
    - OOP áttekintés, Python `class` alapok
    - members, Python private és protected lehetőségek
    - metódus vs függvény, védett metódusok, `__init__`, `__del__`...
    - old és new-style class, származtatás Pythonban, `mro()`
    - gyakorlatok
 6. **Extra adag** Innentől lehetne durvulni! :D
    - type() három paraméterrel, type(type), "everything is object"
    - meta, operátor metódusok, static és dynamic methods, classmethod
    - easter eggs, `dis`, Python filozófia és Python Zen, jövő
    - numpy, scipy, IPython...
    - whatever...
 6. Python gyakorlatok, mindennapi library-k
    - `os`, `sys`, `subprocess`
    - opcionálisan: `pickle`, `shelve`, `time`, `threading`, `tkinter`
    - Python compile, frozen, bináris pakk
    - PEP8, autoformatter és checker
    - ...egyéb AdventOfCode és HackerRank feladatok

---

====

```python
import numpy

def fn():
	pass
>>> fn()
```

---
<!-- page_number: false -->
