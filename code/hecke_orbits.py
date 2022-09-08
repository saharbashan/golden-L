from sage.misc.cachefunc import cached_function
from sage.all import Integer,cos,pi,AA,NumberField,MatrixSpace,VectorSpace,animate,sxrange,matrix,RDF, floor,point2d,identity_matrix
# License
# Copyright

r"""
Diagonals in the "double-(2g+1)-gon staircase"

EXAMPLES::

    sage: load('hecke-orbits.sage')
    sage: basic_diagonals(1)
    [(1, 0), (1, 1)]
    sage: basic_diagonals(2)
    [(1, 0), (a, 1), (a, a)]
    sage: basic_diagonals(3)
    [(1, 0), (a, 1), (a^2 - 1, a), (a^2 - 1, a^2 - 1)]
    sage: basic_diagonals(4)
    [(1, 0), (a, 1), (a^2 - 1, a), (a + 1, a^2 - 1), (a + 1, a + 1)]
    sage: basic_diagonals(5)
    [(1, 0),
     (a, 1),
     (a^2 - 1, a),
     (a^3 - 2*a, a^2 - 1),
     (a^4 - 3*a^2 + 1, a^3 - 2*a),
     (a^4 - 3*a^2 + 1, a^4 - 3*a^2 + 1)]
    sage: basic_diagonals(6)
    [(1, 0),
     (a, 1),
     (a^2 - 1, a),
     (a^3 - 2*a, a^2 - 1),
     (a^4 - 3*a^2 + 1, a^3 - 2*a),
     (a^5 - 4*a^3 + 3*a, a^4 - 3*a^2 + 1),
     (a^5 - 4*a^3 + 3*a, a^5 - 4*a^3 + 3*a)]
    sage: basic_diagonals(7)
    [(1, 0),
     (a, 1),
     (a^2 - 1, a),
     (a^3 - 2*a, a^2 - 1),
     (-a^3 + a^2 + 4*a, a^3 - 2*a),
     (a^3 - 2*a + 1, -a^3 + a^2 + 4*a),
     (a^2 + a - 1, a^3 - 2*a + 1),
     (a^2 + a - 1, a^2 + a - 1)]
    sage: basic_diagonals(8)
    [(1, 0),
     (a, 1),
     (a^2 - 1, a),
     (a^3 - 2*a, a^2 - 1),
     (a^4 - 3*a^2 + 1, a^3 - 2*a),
     (a^5 - 4*a^3 + 3*a, a^4 - 3*a^2 + 1),
     (a^6 - 5*a^4 + 6*a^2 - 1, a^5 - 4*a^3 + 3*a),
     (a^7 - 6*a^5 + 10*a^3 - 4*a, a^6 - 5*a^4 + 6*a^2 - 1),
     (a^7 - 6*a^5 + 10*a^3 - 4*a, a^7 - 6*a^5 + 10*a^3 - 4*a)]
    sage: basic_diagonals(9)
    [(1, 0),
     (a, 1),
     (a^2 - 1, a),
     (a^3 - 2*a, a^2 - 1),
     (a^4 - 3*a^2 + 1, a^3 - 2*a),
     (a^5 - 4*a^3 + 3*a, a^4 - 3*a^2 + 1),
     (a^6 - 5*a^4 + 6*a^2 - 1, a^5 - 4*a^3 + 3*a),
     (a^7 - 6*a^5 + 10*a^3 - 4*a, a^6 - 5*a^4 + 6*a^2 - 1),
     (a^8 - 7*a^6 + 15*a^4 - 10*a^2 + 1, a^7 - 6*a^5 + 10*a^3 - 4*a),
     (a^8 - 7*a^6 + 15*a^4 - 10*a^2 + 1, a^8 - 7*a^6 + 15*a^4 - 10*a^2 + 1)]
    sage: basic_diagonals(10)
    [(1, 0),
     (a, 1),
     (a^2 - 1, a),
     (a^3 - 2*a, a^2 - 1),
     (a^4 - 3*a^2 + 1, a^3 - 2*a),
     (a^5 - 4*a^3 + 3*a, a^4 - 3*a^2 + 1),
     (-a^5 + a^4 + 6*a^3 - 2*a^2 - 8*a - 2, a^5 - 4*a^3 + 3*a),
     (a^5 - 4*a^3 + 3*a + 1, -a^5 + a^4 + 6*a^3 - 2*a^2 - 8*a - 2),
     (a^4 - 3*a^2 + a + 1, a^5 - 4*a^3 + 3*a + 1),
     (a^3 + a^2 - 2*a - 1, a^4 - 3*a^2 + a + 1),
     (a^3 + a^2 - 2*a - 1, a^3 + a^2 - 2*a - 1)]
    sage: basic_diagonals(11)
    [(1, 0),
     (a, 1),
     (a^2 - 1, a),
     (a^3 - 2*a, a^2 - 1),
     (a^4 - 3*a^2 + 1, a^3 - 2*a),
     (a^5 - 4*a^3 + 3*a, a^4 - 3*a^2 + 1),
     (a^6 - 5*a^4 + 6*a^2 - 1, a^5 - 4*a^3 + 3*a),
     (a^7 - 6*a^5 + 10*a^3 - 4*a, a^6 - 5*a^4 + 6*a^2 - 1),
     (a^8 - 7*a^6 + 15*a^4 - 10*a^2 + 1, a^7 - 6*a^5 + 10*a^3 - 4*a),
     (a^9 - 8*a^7 + 21*a^5 - 20*a^3 + 5*a, a^8 - 7*a^6 + 15*a^4 - 10*a^2 + 1),
     (a^10 - 9*a^8 + 28*a^6 - 35*a^4 + 15*a^2 - 1, a^9 - 8*a^7 + 21*a^5 - 20*a^3 + 5*a),
     (a^10 - 9*a^8 + 28*a^6 - 35*a^4 + 15*a^2 - 1, a^10 - 9*a^8 + 28*a^6 - 35*a^4 + 15*a^2 - 1)]

    sage: load('hecke-orbits.sage')
    sage: d = long_diagonals(2, 9, 9)
    sage: pic = nf_point2d(d) + line2d(((5,0),(5,5),(0,5)))
    sage: ppic = pic + sum(line2d(((0,0),p)) for p in d)
    sage: ppic.show(aspect_ratio=1,figsize=(20,20))

    sage: load('hecke-orbits.sage')
    sage: xmax, ymax = 100, 100
    sage: xmax, ymax = 500, 500
    sage: d = long_diagonals(2, xmax, ymax, clip=True)
    sage: pic = nf_point2d(d) + line2d(((xmax, 0),(xmax, ymax), (0, ymax)))
    sage: pic.show(aspect_ratio=1,figsize=(20, 20))
    sage: nf_point2d(d).show(aspect_ratio=1, axes=False, figsize=(100,100))

    sage: load('hecke-orbits.sage')
    sage: xmax, ymax = 100, 100
    sage: xmax, ymax = 500, 500
    sage: d2 = long_diagonals(2, xmax, ymax, clip=True)
    sage: nf_point2d(d2).show(aspect_ratio=1, axes=False, figsize=(xmax/20, ymax/20))
    sage: d3 = long_diagonals(3, xmax, ymax, clip=True)
    sage: nf_point2d(d3).show(aspect_ratio=1, axes=False, figsize=(xmax/20, ymax/20))
    sage: d4 = long_diagonals(4, xmax, ymax, clip=True)
    sage: nf_point2d(d4).show(aspect_ratio=1, axes=False, figsize=(xmax/20, ymax/20))
    sage: d5 = long_diagonals(5, xmax, ymax, clip=True)
    sage: nf_point2d(d5).show(aspect_ratio=1, axes=False, figsize=(xmax/20, ymax/20))
    sage: d6 = long_diagonals(6, xmax, ymax, clip=True)
    sage: nf_point2d(d6).show(aspect_ratio=1, axes=False, figsize=(xmax/20, ymax/20))

    sage: load('hecke-orbits.sage')
    sage: gmin, gmax = 2, 8
    sage: xymax = 250
    sage: verbose = True
    sage: for g in sxrange(gmin, gmax+1):
    ....:     if verbose:
    ....:         print('g = {}'.format(g))
    ....:     p = nf_point2d(long_diagonals(g, xymax, xymax),
    ....:         aspect_ratio=1, figsize=(10, 10))
    ....:     p.save('long_diagonals_g_{}_xy_{}.svg'.format(g, xymax))
    ....:     p.save('long_diagonals_g_{}_xy_{}.png'.format(g, xymax))

    sage: d = long_diagonals(g=1, xmax=250, ymax=250)
    sage: dd = [vector(ZZ, v) for v in d if not (ZZ(v[0]) % 2) or not (ZZ(v[1]) % 2)]
    sage: p = nf_point2d(dd, aspect_ratio=1, figsize=(10, 10))
    sage: p.save('long_diagonals_g_{}_xy_{}.png'.format('oo', 250))
    sage: p.save('long_diagonals_g_{}_xy_{}.svg'.format('oo', 250))

.. NOTES:

    - The time-consuming steps are (1) plotting, (2) enumerating;
      not much point in speeding up the preliminary steps;
      and not clear whether this would speed them up:

          def xxx(g, n=None, a=None, K=None, V=None):
              if n is None or a is None or K is None or V is None:
                   g, n, a, K, V = structure(g)

.. TODO:

    - Read Koseleff-Rouillier-Tran,
      "On the Sign of a Trigonometric Expression"

    - Animate the staircase surfaces Stairs(g) as g grows

          sage: gmax = 12
          sage: gmax = 40
          sage: animate(Stairs(g).show(
                    aspect_ratio=1, axes=False) for g in range(3, gmax+1))

    - Animate "long diagonals of Stairs(g)" as g grows

          sage: gmax = 12
          sage: gmax = 40
          sage: animate(long_diagonals(g, 200, 200).show(
                    aspect_ratio=1, figsize=(10, 10))
                    for g in range(3, gmax+1))



          sage: longdiags = []
          sage: gmax = 27
          sage: xmax = 100
          sage: for g in sxrange(3, gmax+1):
          ....:     longdiags.append(nf_point2d(long_diagonals(g, xmax, xmax),
          ....:             aspect_ratio=1, figsize=(10, 10)))
          ....:
          sage: animate(longdiags)

    - Animate "all diagonals of Stairs(g)" as g grows

          sage: gmax = 12
          sage: gmax = 40
          sage: longdiags = []
          sage: for g in sxrange(3, gmax+1):
          ....:     print(g, end=' ')
          ....:     longdiags.append(nf_point2d(long_diagonals(g, 30, 30),
          ....:                      aspect_ratio=1, figsize=(10, 10))
          sage: animate(longdiags
                    aspect_ratio=1, figsize=(10, 10))
                    for g in range(3,gmax+1)))

    - line2d of long diagonals

          sage: line2d(long_diagonals(3, 10, 10)).show(
                    aspect_ratio=1, axes=False, figsize=(10, 10))

Finding holes.

    sage: def boxes(d, box_size=1, return_box=False):
    ....:     b = box_size
    ....:     from collections import defaultdict
    ....:     box = defaultdict(list)
    ....:     xmax = ymax = 2^4
    ....:     for x, y in d:
    ....:         box[(b*floor(x/b), b*floor(y/b))].append((x,y))
    ....:     return box
    sage: xmax = ymax = 2^10
    sage: d2 = long_diagonals(2, xmax, ymax, clip=True)
    sage: len(d2)
    572605
    sage: B = boxes(d2, box_size=4, return_box=True)
    ....: G = Graphics()
    ....: for b, l in box.iteritems():
    ....:     G += text('{0:02d}'.format(len(l)), b)
    sage: G.show(aspect_ratio=1, aspect_ratio=1, figsize=64)
"""
from collections import defaultdict
from itertools import chain
from datetime import datetime

def mean(xx):
    return sum(xx) / len(xx)

def datestamp():
    r"""
    Return the current UTC date-and-time-stamp.
    """
    d = datetime.utcnow()
    return d, d.isoformat().split('.')[0].replace('T', ' ') + ' Z'

@cached_function
def structure(g):
    r"""
    Return g, n, a, K, V.

    OUTPUT:

    - ``g`` -- the genus
    - ``n`` (= 2 * g + 1) -- so that double-n-gon is related
    - ``a`` -- 2 * cos(pi/n), as a number field element
    - ``K`` -- the number field QQ(a)
    - ``V`` -- the vector field K^2

    .. TODO:

        - speed things up using Koseleff-Rouillier-Tran's paper
          "On the Sign of a Trigonometric Expression"
    """
    g = Integer(g)
    n = 2 * g + 1
    aa = AA(2*cos(pi/n))
    K= NumberField(aa.minpoly(), embedding=RDF(aa),names='a')
    V = VectorSpace(K, 2)
    return((g, n, K.gen(), K, V))

@cached_function
def number_sequence(g):
    r"""
    Return number sequence giving coordinates of basic diagonals.

    EXAMPLE::

        sage: number_sequence(2)
        (0, 1, a)
    """
    g, n, a, K, V = structure(g)
    s = [K.zero(), K.one()]
    while len(s) <= g:
        s.append(a*s[-1] - s[-2])
    return(tuple(s))

def basic_diagonals(g):
    r"""
    Return the basic diagonals for the (odd n) "double-n-gon staircase".

    EXAMPLES::

        sage: basic_diagonals(2)
        [(1, 0), (a, 1), (a, a)]
    """
    g, n, a, K, V = structure(g)
    v = [V((K.one(), K.zero())), V((a, K.one()))]
    while len(v) <= g:
        v.append(a*v[-1] - v[-2])
    return(v)

def xmatrix(g, format='vertical'):
    r"""
    Return the extra diagonals to add in each sector, as a matrix.
    """
    g, n, a, K, V = structure(g)
    d = basic_diagonals(g)
    if format=='vertical':
        return(matrix(K, d[1:] + [u[::-1] for u in d[-2:0:-1]]))
    elif format=='horizontal':
        return(matrix(K, d[1:] + [u[::-1] for u in d[-2:0:-1]]).transpose())
    raise ValueError("format should be 'horizontal' or 'vertical'")

def augmatrix(g):
    r"""
    Return the augmentation matrix, ie diagonals to add in each sector.

    Same as xmatrix, different implementation to compare speed.
    """
    g, n, a, K, V = structure(g)
    s = number_sequence(g)
    s.extend(s[::-1])
    return(matrix(K, (s[1:-2],s[2:-1])))

def within_bounds(v, xmax, ymax):
    return(v[0] < xmax and v[1] < ymax)

def long_diagonals(g, xmax=10, ymax=10, clip=True):
    r"""
    Return the long diagonals for 0 <= x < xmax, 0 <= y < ymax.
    """
    g, n, a, K, V = structure(g)
    xmax, ymax = K(xmax), K(ymax)
    M = MatrixSpace(K, 2)
    def bounded(v):
        return(within_bounds(v, xmax, ymax))
    x = identity_matrix(K, 2).rows()
    if xmax == ymax:
        x = basic_diagonals(g)
    m = xmatrix(g)
    l = m.nrows()
    k, nc = 1, len(x)
    while k < nc:
        if bounded(x[k-1]) and bounded(x[k]):
            xx = (m * M(x[k-1:k+1])).rows()
            if any(bounded(v) for v in xx):
                x[k:k] = xx
                nc += l
            else: k += 1
        else:
            k += 1
    if clip:
        x = list(filter(bounded, x))
    if xmax == ymax:
        x.extend(v[::-1] for v in x[-2::-1])
    return x

def low_diagonals(g=2, xmax=10, clip=True, start=None):
    r"""
    Return the long diagonals for 0 <= x < xmax and 0 <= y < x

    These are returned as a dictionary d whose keys are the
    x coordinates of these diagonals, and d[x] is the sorted
    list of y coordinates such that (x, y) is such a diagonal.

    If a starting list of (unclipped) diagonals is passed in,
    it is used as a starting point and extended in place.
    """
    g, n, a, K, V = structure(g)
    xmax = K(xmax)
    M = MatrixSpace(K, 2)
    def bounded(v):
        return v[0] <= xmax
    m = xmatrix(g)
    l = m.nrows()
    if start is None:
        x = basic_diagonals(g)
    else:
        x = start
    k, nc = 1, len(x)
    while k < nc:
        if bounded(x[k-1]) and bounded(x[k]):
            xx = (m * M(x[k-1:k+1])).rows()
            if any(bounded(v) for v in xx):
                x[k:k] = xx
                nc += l
            else: k += 1
        else:
            k += 1
    if clip:
        x = list(filter(bounded, x))
    d = defaultdict(list)
    for u, v in x:
        d[u].append(v)
    return d

def unclipped_very_low_diagonals(g=2, xmax=10, start=None, verbose=False):
    r"""
    Return the long diagonals for 0 <= x < xmax and 0 <= y < a/2 * x

    These are returned sorted by slope, unclipped (ie there are
    some with x > xmax, so that it can be used to start again.
    """
    g, n, a, K, V = structure(g)
    xmax = K(xmax)
    M = MatrixSpace(K, 2)
    def bounded(v):
        return v[0] <= xmax
    m = xmatrix(g)
    l = m.nrows()
    if start is None:
        x = basic_diagonals(g)
        k = len(x) - 1
        x[k:] = (m[:g] * M(x[k-1:k+1])).rows()
    else:
        x = start
    k, nc = 1, len(x)
    if verbose:
        indent = "| " * verbose
        old_percent = 0
        old_time, old_iso = datestamp()
        start_time, start_iso = old_time, old_iso
        print(f'[{start_iso}] {indent}   0%')
    while k < nc:
        if verbose:
            pc = (200 * x[k][1] / a / x[k][0]).floor()
            if pc > old_percent:
                percent = pc
                new_time, new_iso = datestamp()
                this_pc = str(new_time - old_time).split('.')[0]
                all_pc = str(new_time - start_time).split('.')[0]
                timing = f'this % took {this_pc}, all % so far took {all_pc}'
                print(f'[{new_iso}] {indent} {percent:3d}% {timing}')
                old_percent = percent
                old_time, old_iso = new_time, new_iso
        if bounded(x[k-1]) and bounded(x[k]):
            xx = (m * M(x[k-1:k+1])).rows()
            if any(bounded(v) for v in xx):
                x[k:k] = xx
                nc += l
            else:
                k += 1
        else:
            k += 1
    return x

def low_diags_from_unclipped_very_low(vecs, xmax, only_very_low=False):
    r"""
    Only for genus two. May need more attention for general g.
    """
    V = vecs[0].parent()
    K = V.base_ring()
    a = K.gen()
    x = list(filter(lambda x: x[0] <= xmax, vecs))
    if not only_very_low:
        k = x.index(V((a, K.one())))
        x.extend((V((x, a*x-y)) for x, y in x[-2:k-1:-1]))
        assert x[-1][0] == x[-1][1]  # consistency check
    d = defaultdict(list)
    for u, v in x:
        d[u].append(v)
    return d

def length_ratios(g):
    r"""
    Return the length ratios of the diagonals to the long diagonals.
    """
    ns = number_sequence(g)
    return [s - ns[i-1] for i, s in enumerate(ns) if i > 0]

def all_diagonals(g, xmax=10, ymax=10):
    kk = length_ratios(g)
    m = min(kk)
    d0 = long_diagonals(g, xmax=xmax/m, ymax=ymax/m, clip=True)
    d = []
    for k in kk:
        def bounded(v):
            return within_bounds(v, xmax/k, ymax/k)
        d.extend((k * v for v in filter(bounded, d0)))
    return d

def animate_long_diagonals(gmin=2, gmax=27, xymax=100, figsize=(10,10), verbose=True):
    r"""
    Return an animation of long diagonals.

    EXAMPLE::

        sage: a = animate_long_diagonals(gmin=2, gmax=100, xymax=300, figsize=(15, 15))
        sage: a
    """
    if verbose:
        import time
    diags = []
    if verbose:
        t = [time.time()]
    for g in sxrange(gmin, gmax+1):
        if verbose:
            print('[{datestamp()}] g = {}'.format(g))
        p = nf_point2d(long_diagonals(g, xymax, xymax),
            aspect_ratio=1, figsize=(10, 10))
        p.save('long_diagonals_g_{}_xy_{}.svg'.format(g,xymax))
        p.save('long_diagonals_g_{}_xy_{}.png'.format(g,xymax))
        diags.append(p)
        if verbose:
            t.append(time.time())
            print('[{datestamp()}]         took', int(t[-1] - t[-2]), 's')
    if verbose:
        print('g = {} to {} took {} s'.format(gmin, gmax, int(t[-1]-t[0])))
    a = animate(diags)
    a.save('long_diagonals_g_{}_to_{}_xy_{}.gif'.format(gmin, gmax, xymax))
    return a

def boxes(d, box_size=1):
    r"""
    Put points of the subset d of RR^2 into b by b square boxes.

    EXAMPLES::

        sage: xmax = ymax = 2^9
        sage: b = 4
        sage: d2 = long_diagonals(2, xmax, ymax, clip=True)
        sage: len(d2)
        xxx
        sage: B = boxes(d2, box_size=b, return_box=True)
        sage: G = Graphics()
        sage: for s, l in box.iteritems():
        ....:     G += text('{0:02d}'.format(len(l)), s)
        ....: G.show(aspect_ratio=1, aspect_ratio=1, figsize=32)
        Launched png viewer for Graphics object consisting of ... graphics primitives
        sage: b = 4
        sage: from collections import defaultdict
        sage: stats = defaultdict(list)
        sage: for x, y in cartesian_product([range(0, xmax, b), range(0, ymax, b)]):
        ....:     stats[len(B[(x, y)])].append((x,y))
        sage: for n, l in stats.iteritems():
        ....:     print(n, len(l))
        0 2
        1 6
        2 40
        3 176
        4 403
        5 902
        6 1616
        7 2192
        8 2575
        9 2497
        10 2107
        11 1536
        12 1076
        13 650
        14 325
        15 148
        16 63
        17 52
        18 14
        19 2
        20 2

        sage: xmax = ymax = 2^10
        sage: b = 4
        sage: d2 = long_diagonals(2, xmax, ymax, clip=True)
        sage: len(d2)
        572605
        sage: B = boxes(d2, box_size=b, return_box=True)
        sage: G = Graphics()
        sage: for s, l in box.iteritems():
        ....:     G += text('{0:02d}'.format(len(l)), s)
        ....: G.show(aspect_ratio=1, aspect_ratio=1, figsize=64)
        Launched png viewer for Graphics object consisting of 65532 graphics primitives
        sage: 2^16
        65536
        sage: b = 4
        sage: from collections import defaultdict
        sage: stats = defaultdict(list)
        sage: for x, y in product(range(0, xmax, b), range(0, ymax, b)):
        ....:     stats[len(B[(x, y)])].append((x,y))
        sage: for n, l in stats.iteritems():
        ....:     print(n, len(l))
        ....:
        0 4
        1 48
        2 206
        3 772
        4 2034
        5 3812
        6 6413
        7 8486
        8 9836
        9 9623
        10 8368
        11 6248
        12 4158
        13 2684
        14 1489
        15 714
        16 351
        17 184
        18 72
        19 20
        20 10
        21 2
        22 2
        sage: from itertools import chain
        sage: for k, l in stats.iteritems():
        ....:     m = len(l)
        ....:     G = Graphics()
        ....:     x, y = vector(ZZ, l[randint(0, m-1)])
        ....:     xx = FiniteEnumeratedSet((x-b, x, x+b))
        ....:     yy = FiniteEnumeratedSet((y-b, y, y+b))
        ....:     xy = cartesian_product((xx, yy))
        ....:     G += nf_point2d(chain(B[s] for s in xy))
        ....:     G += line2d([(x, y), (x+4, y), (x+4, y+4), (x, y+4), (x, y)])
        ....:     G.show()
    """
    b = box_size
    from collections import defaultdict
    box = defaultdict(list)
    xmax = ymax = 2^4
    for x, y in d:
        box[(b*floor(x/b), b*floor(y/b))].append((x,y))
    return box

def nf_point2d(points, bits=20, **options):
    r"""
    Plot points with coordinates in a number field.

    INPUT:

    - ``points`` -- a list or iterables of points

    - ``bits`` (default: 20): how many bits for the fractional part

    Usual options for :meth:`point2d` can be used, eg `color='green'`
    or `aspect_ratio=1`.

    Note that applying the usual point2d to points with coordinates
    in a number field can give extremely weird results, since the
    coordinates get converted to Python floats in a brutal way.
    When the coefficients for the representation of a number field
    element as a polynomial in the number field generator are huge,
    the error in converting it to a float can get way bigger than
    the actual number field element.
    """
    q = 2^bits
    qq = RDF(q)
    p = lambda x, y: (RDF((q*x).round())/qq, RDF((q*y).round())/qq)
    return point2d((p(x,y) for x, y in points), **options)
