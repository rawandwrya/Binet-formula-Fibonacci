# Fibonacci Recurrence Relationship:
$F_{(n)} = F_{(n-1)} + F_{(n-2)}$
> where n $= 1,2,3,...$ and $F_{(1)}=F_{(2)}=1$

# Binet's Formula:
Fibonacci Terms from the Golden Ratio
$$\text{let the golden ratio} = \varphi = \frac{1+\sqrt{5}}{2}$$
$$F_{(n)}=\frac{\varphi^{n}-(-\varphi)^{-n}}{\sqrt{5}}$$

# Logic
Binet's formula allows us to calculate Fibonacci terms, but we have to round the result up at the end.

# Functionality, Argument, and Return
1. Requires a positive integer as an argument for the function
2. Returns a numpy list of Fibonacci terms up till the nth term

# Programming Concepts Used
1. Functions-Arguments-Returns
2. Input
3. Exception Handling

# Libraries Used
1. Numpy
> np.arange()  
> np.sqrt()  
> np.add()  
> np.divide()  
> np.rint()  
