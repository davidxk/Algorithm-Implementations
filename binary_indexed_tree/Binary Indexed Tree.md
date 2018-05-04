# Binary Indexed Tree
With the number system, human can represent the number a hundred with three digits. 

```
100 = count([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
```

This reduce the space complexity of number representation to $\log(n)$

$$\log(100) = 3$$

Binary Indexed Tree takes this notion of taking $\log$, and arrives at a data structure that achieves `update()` and `getSum()` operation both at $\log(n)$ complexity. 

For $\forall n$, `getSum(n)` is decomposed as the sum of powers-of-two. 

$$\begin{align}
	13 &= 8 + 4 + 1 \\
	1101 &= 1000 + 0100 + 0001
\end{align}$$

Each corresponding sum is stored

```python
sum(array[0: 13]) = sum(array[0: 8]) + sum(array[8: 12]) + sum(array[12: 13]) 
sum([0000: 1101]) = sum([0000: 1000]) + sum([1000: 1100]) + sum([1100: 1101]) 
```
