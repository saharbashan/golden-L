---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.0
  kernelspec:
    display_name: SageMath 9.6
    language: sage
    name: sagemath
---

```sage
from collections import defaultdict
```

```sage
from hecke_orbits import structure,long_diagonals
```

```sage
_g = 2
_xmax = 51
_ymax = 51
```

```sage
# Load long diagonals, or compute them and save them

try:
    print('Attempting to load...')
    orb = load('data/orb_{}_{}_{}.sobj'.format(_g, _xmax, _ymax))
    print('Loaded.')
except FileNotFoundError:
    print('Failed to load.\nComputing...')
    orb = long_diagonals(_g, _xmax, _ymax)
    print('Computed.\nSaving...')
    save(orb, 'data/orb_{}_{}_{}.sobj'.format(_g, _xmax, _ymax))
    print('Saved.')
```

```sage
orb
```

```sage
structure(2)
```

```sage
g, n, a, K, V = structure(2)
c0 = matrix(2, [1, a, 0, 1])
c1 = matrix(2, [a, a, 1, a])
c2 = matrix(2, [a, 1, a, a])
c3 = matrix(2, [1, 0, a, 1])
d0 = matrix(2, [1, -a, 0, 1])
d1 = matrix(2, [a, -a, -1, a])
d2 = matrix(2, [a, -1, -a, a])
d3 = matrix(2, [1, 0, -a, 1])
```

```sage
def gcd_of_vector(x,y):
    if y == 0:
        return x
    if x > a * y:
        return gcd_of_vector(x - a*y, y)
    if x > y >= x * (a - 1):
        return gcd_of_vector(a*x - a*y, -x+a * y)
    if a * x > y >= x:
        return gcd_of_vector(a*x - y, -a*x + a*y)
    if y >= a * x:
        return gcd_of_vector(x, -a*x + y)
```

```sage
gcd_of_vector(2 + a, 3 + a)
```

```sage
gcd_of_vector(3+ 4*a,4+ 5*a)
```

```sage
(2817/4558).continued_fraction()
```

```sage
(2550/4141).continued_fraction()
```

```sage
(4125/2576).continued_fraction()
```

```sage
(4558/2817).continued_fraction()
```

```sage
(4141/2550).continued_fraction()
```

```sage
(4130/2568).continued_fraction()
```

```sage
(4140/2552).continued_fraction()
```

```sage
(4145/2544).continued_fraction()
```

```sage
(4124/2578).continued_fraction()
```

```sage
(79172/48931).continued_fraction()
```

```sage
(437/270).continued_fraction()
```

```sage
00
```

```sage

```
