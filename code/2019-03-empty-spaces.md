# Empty spaces

```
Saving uvld_12
Saving ld_12 to ld_12.sobj
Saving emtpy_12.sobj
1 4797286
2 844049
3 45822
4 787
5 4
6 0
7 0
8 0
9 0
No existing file, computing empty_13
Computing ld_13
Checking if uvld_13.sobj exists
Checking if uvld_12.sobj exists
Starting from uvld_12 as found in uvld_12.sobj
Computing uvld_13
Saving uvld_13
Saving ld_13 to ld_13.sobj
Saving emtpy_13.sobj
1 19229274
2 3453330
3 196008
4 3573
5 25
6 0
7 0
8 0
9 0
No existing file, computing empty_14
Computing ld_14
Checking if uvld_14.sobj exists
Checking if uvld_13.sobj exists
Starting from uvld_13 as found in uvld_13.sobj
Computing uvld_14
```

```
lelievre@pascaline:~/r/hecke$ ls -halF *.sobj
-rw-r--r-- 1 lelievre topodyn 284K Mar 10 16:56 empty_10.sobj
-rw-r--r-- 1 lelievre topodyn 1.2M Mar 10 18:35 empty_11.sobj
-rw-r--r-- 1 lelievre topodyn 5.2M Mar 10 19:09 empty_12.sobj
-rw-r--r-- 1 lelievre topodyn  25M Mar 11 01:44 empty_13.sobj
-rw-r--r-- 1 lelievre topodyn  310 Mar 10 17:35 empty_3.sobj
-rw-r--r-- 1 lelievre topodyn  545 Mar 10 17:35 empty_4.sobj
-rw-r--r-- 1 lelievre topodyn 1.3K Mar 10 17:35 empty_5.sobj
-rw-r--r-- 1 lelievre topodyn 3.0K Mar 10 18:31 empty_6.sobj
-rw-r--r-- 1 lelievre topodyn 8.0K Mar 10 18:31 empty_7.sobj
-rw-r--r-- 1 lelievre topodyn  24K Mar 10 15:53 empty_8.sobj
-rw-r--r-- 1 lelievre topodyn  76K Mar 10 18:31 empty_9.sobj
-rw-r--r-- 1 lelievre topodyn 8.2M Mar 10 16:56 ld_10.sobj
-rw-r--r-- 1 lelievre topodyn  33M Mar 10 18:34 ld_11.sobj
-rw-r--r-- 1 lelievre topodyn 131M Mar 10 18:57 ld_12.sobj
-rw-r--r-- 1 lelievre topodyn 520M Mar 11 00:07 ld_13.sobj
-rw-r--r-- 1 lelievre topodyn 1.2K Mar 10 17:35 ld_3.sobj
-rw-r--r-- 1 lelievre topodyn 3.0K Mar 10 17:35 ld_4.sobj
-rw-r--r-- 1 lelievre topodyn 9.0K Mar 10 17:35 ld_5.sobj
-rw-r--r-- 1 lelievre topodyn  33K Mar 10 18:31 ld_6.sobj
-rw-r--r-- 1 lelievre topodyn 127K Mar 10 18:31 ld_7.sobj
-rw-r--r-- 1 lelievre topodyn 519K Mar 10 15:53 ld_8.sobj
-rw-r--r-- 1 lelievre topodyn 2.1M Mar 10 18:31 ld_9.sobj
-rw-r--r-- 1 lelievre topodyn  21M Mar 10 16:56 uvld_10.sobj
-rw-r--r-- 1 lelievre topodyn  85M Mar 10 18:34 uvld_11.sobj
-rw-r--r-- 1 lelievre topodyn 342M Mar 10 18:56 uvld_12.sobj
-rw-r--r-- 1 lelievre topodyn 1.4G Mar 10 23:59 uvld_13.sobj
-rw-r--r-- 1 lelievre topodyn 1.6K Mar 10 17:35 uvld_3.sobj
-rw-r--r-- 1 lelievre topodyn 4.8K Mar 10 17:35 uvld_4.sobj
-rw-r--r-- 1 lelievre topodyn  18K Mar 10 17:35 uvld_5.sobj
-rw-r--r-- 1 lelievre topodyn  73K Mar 10 18:30 uvld_6.sobj
-rw-r--r-- 1 lelievre topodyn 305K Mar 10 18:31 uvld_7.sobj
-rw-r--r-- 1 lelievre topodyn 1.3M Mar 10 15:53 uvld_8.sobj
-rw-r--r-- 1 lelievre topodyn 5.1M Mar 10 18:31 uvld_9.sobj
```

## A conjecture about the density of empty spaces

### Conjecture

For any $r > 0$, define

$N_{E}(r, T) = \# \{ x, y \in [0, T]^2 \cap \mathbb{N}^2 | ([x, x + r] \times [y, y + r]) \cap \Lambda = \emptyset \}$.

Then there exists $c$ (depending on $r$)
such that $N_E(r, T) \sim c \cdot T^2$.

### Evidence

See some evidence in `empty_spaces_2019-03.ipynb`.
