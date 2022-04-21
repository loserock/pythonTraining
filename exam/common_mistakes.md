
A leggyakoribb hibák
====================

 - `str` használata `list` helyett, `.append()` helyett `+= " " + data` hozzáfűzéssel, majd a végén `.split()`-tel lista lesz belőle
 - `set.add` helyett `list` feltöltése, majd a végén konvertálás `set`-re (egyedi elemek számának meghatározásához)
 - fájl folyamatos újra beolvasása minden feladathoz
 - `class` mindig újra példányosítása minden method híváshoz
 - érdemes kerülni az olyan változóneveket, amik a nyelvben definiált szavak (pl. modul vagy függvény név), például: `open`, `max`, `min`, `list`, `dict`, `id`...
 - file stream használata lista helyett, képes rá a nyelv, de néha máshogy fog viselkedni, például egymásba ágyazott ciklusnál tolni fogja a beolvasott sort előre és nem lehet szimultán olvasni kétszer ugyanazt a filestream-et (új `open`-nel lehetne, de nem hatékony és nem is ajánlott)
 - copy-paste kódrészre, függvény `def` helyett
 - `class`-on belül már ki van számolva az eredemény, de nincs eltárolva membernek, hanem újra kiszámoltatja
 - file stream objektumra létezik `.readlines()` metódus, ami egy `list`-ben visszaadja az összes sort elemenként, de jó comprehension-nel is, csak a readlines tömörebb
 - `.split(' ')` helyett általában jobb a `.split()` simán, bár most jó erdményt adott az előbbi is
 - elegánsabb `+=`-t használni `a = a +` helyett
 - ha ciklussal max `float` vagy `int` számot kell keresni, és az lehet negatív is, akkor nem jó a default szűrő értéket 0-ról indítani (de nem vontam le érte, és most kijött a jó megoldás így is, mázli)
 - ha számot (`float`, `int`) szövegből olvasunk be, át kell konvertálni az `str`-t, különben a max/min keresés (vagy a relációk) nem számként fognak rajtuk működni!
 - for használata következetesen `xrange(len())` stílusban indexeléssel, sima for vagy for + enumerate helyett (van, amikor ez tényleg a legjobb megoldás)
 