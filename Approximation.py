import math
epsilon = 1e-6
def func(x):
  """
  Defines a function.
  """
    return (x**2 - 5) 
    
def derivative(x):
  """
  Calculates derivative.
  """
    return (func(x+1e-7)-func(x))/(1e-7)
    
def approximation():
  """
  Using the Newton-Raphson Method, it finds the square root of 5. 
  """
    x = int(input('initializer: '))
    while abs(x - math.sqrt(5)) > epsilon:
        x = (-func(x)/derivative(x)) + x 
        print(x)
    return x
    
print(approximation())
