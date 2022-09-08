# -*- coding: utf-8

# License
# Copyright

r"""
Empty spaces in Hecke5 orbit of (1, 0)

"""
import os

load('hecke-orbits.sage')

def empty_boxes(d):
    """
    Find the $(a, b)$ such that $[a, a+1) \times [b, b+1)$ is empty.
    
    More precisely, return a list of pairs (a, b)
    where a, b are integers, and 0 <= a <= M, 0 <= b <= N
    ...

    Note: we rely on the fact that there are no empty columns.
    In fact there is one, for x = 0, and it is left out here.

    INPUT:
    
    - ``d`` -- a dictionary as returned by the function
      ``long_diagonals_under_diagonal`` in ``hecke-orbits.sage``
    
    EXAMPLES::

    """
    empty = dict()
    kx = defaultdict(list)
    for x in d.keys():
        kx[x.floor()].append(x)
    xmax = max(kx)
    for k in range(xmax + 1):
        if k in kx:
            ck = set(y.floor() for x in kx[k] for y in d[x])
            empty[k] = [l for l in range(k) if l not in ck]
        else:
            empty[k] = list(range(k))
    return empty

def square(p, k, *kw, **opt):
    x, y = p
    return polygon([(x, y), (x+k, y), (x+k, y+k), (x, y+k)], *kw, **opt)

def empty_next_level(e):
    r"""
    Return the next level of empty boxes.
    
    EXAMPLE::
    
        sage: xmax = 2^10
        sage: d = low_diagonals(g=2, xmax=xmax)
        sage: emp = empty_boxes(d)
        sage: empty = {1: emp}
        sage: for k in range(2, 10):
        ....:     if k not in empty:
        ....:         empty[k] = empty_next_level(empty[k-1])
        sage: for k in empty:
        ....:     print(k, sum(len(empty[k][x]) for x in empty[k]))
        1 298317
        2 48578
        3 2230
        4 29
        5 0
        6 0
        7 0
        8 0
        9 0
    """
    return dict((x, [y for y in e[x] if x + 1 in e and y + 1 in e[x]
                     and y in e[x + 1] and y + 1 in e[x + 1]])
                for x in e)
