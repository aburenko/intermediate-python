# List Comprehension and Generators
**List Comprehension** - fast, but memory expansive  (e.g. `[i for i in range(n)]`) 
> creates all elements of an array and save them
 
**Generator** - slower, but not using that much memory (e.g. `range(n) or (i for i in range(n))`)
> instead of creating all that element makes an iterator 

