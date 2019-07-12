# String Concatenation and Formatting
Using of looping + operator is not that efficient.
The better way to concatenate strings is to use .join().

Join is the invert operation of split  
`"string split example".split()`  
produce `["string", "split", "example"]`

So to join you need  
`" ".join("string", "split", "example")`

As Placeholders `{}` are to use, as example  
`"Time is {}:{}".format(12,30)`