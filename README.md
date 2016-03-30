# PartizanEndnimSolver

To escape the tyranny of repetitive busywork.

## How To Use

Simply run `python3 main.py` and enter a space-separated list of stack heights for the state to be analyzed.

## Examples

Input:

`3 5 4 5 1`

Output:

`state: w = 3 5 4 5 1`

`outcome class L`

`L(w) = 0`

`R(w) = 2`

`show proof (y/n)? y`

`proof:`

`L(3 5) = 5`

`R(3 5) = 0`

`L(3 5 4) = 5 - 0 + 4 = 9`

`L(5 4) = 0`

`R(5 4) = 5`

`R(3 5 4) = 5 - 0 + 3 = 8`

`L(3 5 4 5) = 0`

`L(5 4 5) = 0`

`L(4 5) = 5`

`R(4 5) = 0`

`R(5 4 5) = 0`

`R(3 5 4 5) = 0 - 0 + 3 = 3`

`L(3 5 4 5 1) = 0`

`L(5 4 5 1) = 0 - 0 + 1 = 1`

`L(4 5 1) = 5 - 0 + 1 = 6`

`L(5 1) = 0`

`R(5 1) = 5`

`R(4 5 1) = 5 - 0 + 4 = 9`

`R(5 4 5 1) = 0`

`R(3 5 4 5 1) = 0 - 1 + 3 = 2`

-

Input:

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20`

Output:

`state: w = 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20`

`outcome class R`

`L(w) = 209`

`R(w) = 0`

`show proof (y/n)? n`
