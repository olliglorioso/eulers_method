# Euler's method

## Features

- Approximate the solution function of a differential equation numerically with Euler's method.
- Give the equation in the following form y'=f(x, y) as a parameter to EulersMethod-class, as well as the initial values x0 and y0.
- EulersMethod.execute(x_stop=5, step_size=0.1, iterations=1000) approximates the solution in the vicinity of x=5, with steps of size 0.1 and max number iterations of 1000.
- PyPi-link: https://pypi.org/project/eulers-method/0.0.2/

## Quick start

```bash
pip install eulers-method==0.0.2
```

```python
from eulers_method import EulersMethod
equation = "y'=2/5*x*y"
euler = EulersMethod.EulersMethod(equation = equation, x0 = 1, y0 = 3)
res = euler.execute(x_stop=5, step_size = 0.1, iterations = 1000)
```
