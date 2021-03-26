```py
def func(x):
"""
Basic Function. Defines 'x' as a variable and returns parabola, that is x^2-5x+6
"""
    return (x**2 - 5*x + 6) 
    
def derivative(x):
    return (func(x+1e-7)-func(x))/(1e-7)
    
print(derivative(5))
end
```
