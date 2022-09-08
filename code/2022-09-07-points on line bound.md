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
load('hecke-orbits.sage')
```

```sage
_g = 2
_ymax = 128
_xmax = 2 * _ymax
```

```sage
# _xmax = 1500

# _ymax = 35
```

```sage
_g, _n, _a, _K, _V = structure(_g)
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
def normal_form(p,q):
    dx=p[0]-q[0]
    dy=p[1]-q[1]
    a,b=(-dy,dx)
    c=-a*p[0]-b*p[1]
    if a==0:
        c/=b
        b=1
    else: 
        c/=a
        b/=a
        a=1
    return a,b,c
    
```

```sage
normal_form((1,0),(0,0))
```

```sage
from collections import defaultdict
from itertools import combinations
count=defaultdict(lambda :0)
for p,q in combinations(orb,2):
    count[normal_form(p,q)]+=1
```

```sage
max(count.values())
```

```sage

```
