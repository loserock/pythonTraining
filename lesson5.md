<!-- $theme: gaia -->
<!-- page_number: false -->
<!-- footer: Péter Handbauer, version: 10/04 -->
<!-- $size: a1 -->


Python Tréning "2"
==============================

#### (Mostly) advanced

## IV. Függvények és generátorok

---
<!-- footer: Python tréning "2", IV. Függvények -->
## Függvények

 - _bárhol_ definiálhatók és alkalmazhatók
 - saját _local_ scope változóknak (ld.: `locals()` vs `globals()`)
    - `global` kulcsszó (_nem_ ajánlott!)
 - `return` opcionális
    - paraméterszáma: 0, 1, 2.. (return with tuple)
 - rugalmas bejövő paraméterek, default értékek
    - mutable vs unmutable
    - dinamikus kezelés: `*args`, `**kwargs`
 - rövid visszatérő függvény: `lambda`

---
## Függvény

 - definiálás: `def` kulcsszó, (paraméterek), `:` és blokk
```python
def function_name( param1, param2 ):
    # do what you want
    r = param1 + param2
    # return if you want
    return r

# call a function:
a = function_name(1, 2)
b = function_name("abc", "def")
```
---
## Függvény paraméterek
 - default érték opcionálisan megadható
 - _de_ a sorrend ilyenkor számít
` def sample_function(a, b=1): `
 - nem előre fix paraméterek, mint lista: `*args`
```python
def fn(a, b, *paramlist):
    if len(paramlist) > 0:
        # ...
```
---
## Függvény paraméterek
 - dictionary a paraméter listából `**kwargs`:
```python
def fn(**paramdict):
    if paramdict.has_key("saveAs"):
        # ...
```
 - természetesen kombinálhatók:
` def fn(a, b=1, *args, **kwargs): `
 - fordítva, list és dict-ből is kitölthetők:
```python
d = {'a': 1, 'saveAs': "new_file.txt"}
l = [1, 2, "something extra param"]
fn(**d)
fn(*l)
```
---
## Függvény

 - `global` példa

```python
def function_name(param1, param2, param3 = 0):
    global global_var
    if param3:
        return param1 * param2
    return global_var * param1, global_var * param2

# execution examples:
global_var = 42
a, b = function_name(3, 4)
print function_name(2, 6, True)
print "a: {}, b: {}".format(a, b)
```
---
# Függvény in-out paraméterek

 - ha _mutable_ objektum (pl. egy list):
    - akkor módosítható a függvényből
    - de _nem_ maga az input param `=` operátorral
    - működik pl. `.append()` vagy `d[key] = `
 - értékadással _nem_ módosítható
    - cserébe a `return` visszatérhet több értékkel is:
` a, b = calc_new_values(a, b) `
---
## Lambda

 - rövid, _értékkel_ visszatérő függvény
 - inline létrehozás `lambda` kulcsszóval:
```python
def fn_normal(p1, p2):
    return p1 + p2

fn_lambda = lambda p1, p2 : p1 + p2
# fn_normal(1,2) == fn_lambda(1,2)
```
 - viszont _closure_: a lambda látja a scope-ot
 - _általánosan_ kerülendő, de sok esetben _praktikusabb_
    - pl. `map` számára inline deklarálható

---
## Generátor függvény
 - szakaszosan kiértékeltethető, általában ismétlődő kód
 - `yield` kulcsszó a `return` helyett vagy mellett
```python
def generator_function(count_until):
    # codes like in function
    for i in xrange(count_until):
        # do anything
        yield i
    # other codes, use return optionally
    return count_until
```
 - generátor hívása csak létrehoz egy generátor objektumot

---
## Generátor objektum
 - következő kiértékelés külön hívható
    - `.next()` metódus vagy
    - `next()` függvény hívása az objektumon
    - exception dobódik, ha már véget ért
 - `for` ciklus sorban kiértékeli, amíg tudja
```python
for i in generator_function(5):
    # i will be the next value
    # what the next yield "returns"
# code after generator ended
```
---
## Generátor objektum
 - véget ér `return` sorral, vagy ha _vége_
 - kívülről is zárható `.close()` hívással

```python
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
g_instance = fibon(100)
for i in g_instance:
    print i,
    if i > 100:
        g_instance.close()
# 1 1 2 3 ... 144
```
---
## Generátor objektum
 - "Csak akkor fut le tényleg, ha szükség van rá!"
 - hasonló kezelés, mint collection/iterable esetén
 - ki lehet értékeltetni az egészet is előre
    - pl.: `list()`, `tuple()`
 - Python 3-tól egyre több függvény generátor szerű
    - pl.: `range()`, `zip()`
    - `for` ciklussal kompatibilis
    - erőforrás takarékos lehet
    - vigyázni kell a kompatibilitással!
---
## Generátor kifejezés
 - az _inline_ változat
 - ld. list comprehension, de _generátort_ készít
 - _sima_ `( )` közé írt comprehension kifejezés

```python
g = ( x*x for x in xrange(10000) )

# nearly equivalent:
def make_gen():
    for x in xrange(10000):
        yield x*x
g = make_gen()
```
---
## Coroutine (érdekesség)
 - `yield` használata _fordítva_
 - táplálása: `send()` metódussal
```python
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

cr = grep("seek this")
cr.send("print nothing")
cr.send("print because of seek this")
```
---
## Kérdések?
