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
 - `return` opcionális
    - paraméterszáma: 0, 1, 2.. (return with tuple)
 - rugalmas bejövő paraméterek, default értékek
    - dinamikus kezelés: `*args`, `**kwargs`
 - rövid visszatérő függvény: `lambda`

---
## Függvények

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