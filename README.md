# Euler's method

## Features

- Approximate the solution function of a differential equation numerically with Euler's method.
- Give the equation in the following form y'=f(x, y) as a parameter to EulersMethod-class, as well as the initial values x0 and y0.
- EulersMethod.execute(x_stop=5, step_size=0.1, iterations=1000) approximates the solution in the vicinity of x=5, with steps of size 0.1 and max number iterations of 1000.

## Quick start

```bash
pip install eulers_method
```

```python
from eulers_method import EulersMethod.EulersMethod
equation = "y'=2/5*x*y"
euler = EulersMethod(equation=equation, x0=1, y0=3)
res = euler.execute(x_stop=5, step_size = 0.1, iterations = 1000)
```
