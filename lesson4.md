<!-- $theme: gaia -->
<!-- page_number: false -->
<!-- footer: Péter Handbauer, version: 10/04 -->
<!-- $size: a1 -->


Python Tréning "2"
==============================

#### (Mostly) advanced

## III. Collection bejárások

---
<!-- footer: Python tréning "2", III. Collection bejárások -->

## Story so far

 - átnézés: `for` és `while` Python-ban
 - iterálás collection típusokon, `enumerate`, `zip`, `len`, `max`, `min`...
 - halmazok, dictionary, előnyök és hátrányok
 - paraméter és keyword unpack, `*args`, `**kwargs`
 - comprehensions
 - iterátorok, `iter`

---
## Ciklusok Pythonban

 - Pythonic way: **csak** `for` és `while`
 - Interpreter _lassú_ ciklusra!
    - egymázba ágyazott `for` ciklusra különösen
 - Vannak célirányos _alternatívák_ `for` helyett
    - adott feladatra általában jobbak
    - pl. `map()`, `filter()`, comprehensions...

---
## `while`

```python
while condition:
    # code block
    # run while condition is True
else:
    # else is optional!
    # after False contidion
    # don't run after break or exception!
# code block after the cycle
```

 - emlékeztető: `False` lehet `0`, `""`, `None` vagy `[]` is!

---
## `for`

 - igazából for_each jellegű

```python
for variable_s in collection:
    # code block
    # run with every members of collection
else:
    # also optional

```

---
## `for`

 - collection elemein halad
    - `str` karakterein halad
    - rendezetlen `set` elemein is
 - file objektum (vagy StringIO) _sorain_ halad
 - `dict` _kulcsain_ halad
 - iterátoron halad végig exception dobás nélkül
 - _nem mindig_ jó módosításra!
 - eszközök: `enumerate()`, `zip()`, itertools modul (pl. `izip()`)

---
## `dict`

 - hash tábla kulcs-érték párokkal
 - **bármilyen** típus lehet kulcs és érték is
    - _kevert_ típusok is `dict`-en belül!
 - minden kulcs egyedi, érték ismétlődés lehet

```python
d = dict( (('a', 1), ('b', 2)) )
d = {'a': 1, 'b': 2}
d['c'] = 3
d[10] = {5: 10/5, 2: 10/2, 1: 10/1}
```

---
## `set`
 - **bármilyen** típusú objektumok halmaza
    - elem nem ismétlődhet
    - módosíthatatlan változat: `frozenset`
 - halmazműveletek és gyors elem létezés vizsgálat (`in`)

```python
s = set( [2, 3, 5, 7, 11] )
s2 = {2, 4, 6, 8, 10, 11}
s.add(13)
s2.remove(11)
2 in s
s.intersection(s2)  # s & s2
s.union(s2)         # s | s2
s.difference(s2)    # s - s2
# ...
```

---

### Kérdések?

#### ...

---

# List Comprehensions

### avagy alternatív `for` ciklus

---
## Comprehensions?

 - Pythonic _felfogás_ collection kezelésre
 - alapból _list_ comprehension-re gondolunk
    - gyors egy soros utasítás `list` létrehozásra és manipulálásra
 - lehet egészen összetett: egymásba ágyazott, feltételes
    - valójában mini program (procedure)
 - **gyors** és _sokszor_ praktikus
 - _dict_ comprehension, _set_ comprehension
 - _generator_ expression (~comprehension)

---
## List Comprehension

 - not so something competly different:

`[` _expression_ `for` _tempvars_ `in` _something_ `if` _conditions_ `]`

 - példák:

```python
sq_list = [i*i for i in xrange(1000)]
# nearly equivalent, but slower alternative:
fn = lambda i: i*i
sq_list_2 = map(fn, xrange(1000))

# conditional form:
l = [i for i in xrange(1000) if i % 7 == 0 and i % 2 == 0]

```

---
## `set` és `dict` comprehensions

```python

# set comprehension
s = {i*i for i in xrange(10,101,2)}

# dict comprehension
d = {i: i*i for i in xrange(10,101,2)}

```

## Much more?
---
## Comprehension vs `map()` sebesség

```bash
$ python -mtimeit -s'xs=range(10)' 'map(hex, xs)'
1000000 loops, best of 3: 1.41 usec per loop
```
```bash
$ python -mtimeit -s'xs=range(10)' '[hex(x) for x in xs]'
1000000 loops, best of 3: 1.81 usec per loop
```
```bash
$ python -mtimeit -s'xs=range(10)' 'map(lambda x: x+2, xs)'
1000000 loops, best of 3: 1.97 usec per loop
```
```bash
$ python -mtimeit -s'xs=range(10)' '[x+2 for x in xs]'
1000000 loops, best of 3: 0.921 usec per loop
```
---

## Comprehension vs `map()` sebesség 2

 - az ördög előbújik _JIT_ esetén

```bash
pypy -mtimeit -s'xs=range(10)' 'map(lambda x: x+2, xs)'
1000000 loops, best of 3: 0.452 usec per loop

pypy -mtimeit -s'xs=range(1000)' 'map(lambda x: x+2, xs)'
10000 loops, best of 3: 33.4 usec per loop
```

```bash
pypy -mtimeit -s'xs=range(10)' '[x+2 for x in xs]'
10000000 loops, best of 3: 0.125 usec per loop

pypy -mtimeit -s'xs=range(1000)' '[x+2 for x in xs]'
100000 loops, best of 3: 3.47 usec per loop

```

---

## Comprehension vs `map()` különbségek
 - scope veszélyek:
```python
for x, y in somePoints:
    # (several lines of code here)
    squared = [x ** 2 for x in numbers]
    # Oops, x was silently overwritten!
```
 - túlterhelés:
```python
# Python 3
>>> map(str, range(10**100))
<map object at 0x2201d50>
>>> [str(n) for n in range(10**100)]
# DO NOT TRY THIS AT HOME OR YOU WILL BE SAD #
```

---

## Generator Expression

 - csak egy gyors példa

```python
# this is NOT a tuple:
g = ( i*i for i in xrange(10,21,2) )

# this is a generator:
print g.next()
for sq in g:
    print sq,
```

```bash
100
144 196 256 324 400
```

---

### Kérdések?

### Folyt. köv.
