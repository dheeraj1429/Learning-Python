from string import ascii_lowercase
import pandas as pd
import math
import sympy
from sympy import symbols, diff, integrate, limit, factor, expand, oo, Eq, solve, dsolve, simplify

# students = ['Andrew', 'John', 'Mark']
# age = [20, 10, 20, 30,]
# mixed = [True, 'John', {"name": "Mark", "age": 20}]
# some_dict = {0: "students", 1: "students", 2: "students"}
# a_dict = pd.Series(some_dict)
# b_dict = pd.Series(some_dict)

# print(pd.Series(students))
# print(pd.Series(age))
# print(pd.Series(mixed)[2]['name'])
# print(pd.Series(data=students))
# print(pd.Series(some_dict)[0])
# print(a_dict.equals(b_dict))

# print(pd.Series(data=age, dtype='float64'))
# print(a_dict.dtype)

# heights = [167.2, "123.12", 10.2]
# print(pd.Series(heights))
# print(pd.Series(data=students, index=['demo', 'demo', 'demo']))
# print(a_dict.index)
# print(type(a_dict.index))
# data = list(pd.RangeIndex(start=0, stop=10, step=2))
# print(data)
# print(a_dict.dtype)
# print(a_dict.name == None)
# print(a_dict)
# a_dict.name = 'some de'
# print(a_dict)
# print(a_dict)
# a_dict.index.name = 'Some document'
# print(a_dict)

# ages = [21, 20, 10, 20]
# users = ['user1', 'user2', 'user3', 'user4']
# print(pd.Series(data=users, index=ages))
# print(pd.Series(list(zip(ages, users))))
# print(pd.Series({name: age for name, age in zip(users, ages)}))

# int_list = pd.Series(item for item in range(0, 10))
# print(pd.Series(item for item in range(0, 10)))
# print(int_list.size)
# print(pd.Series(range(40)).head(n=2))
# print(pd.Series(range(40)).tail(n=2))
# pd.options.display.min_rows = 10
# print(pd.Series(range(100)))
# print(ascii_lowercase)
# print(pd.Series(list(ascii_lowercase)).head(10 + 1))

# ----------------------------------------------------------------

# print(math.sqrt(16))
# print(sympy.sqrt(16))

# print(math.sqrt(15))
# print(sympy.sqrt(15))

# x = symbols('x')
# y = symbols('y')

# expression = 2 * x + y
# expression_second = 2 * (x + y)

# print(expression)
# print(expression - y)
# print(expression_second)
# print(factor(expression_second))

# expression2 = x * (x + y)
# print(expression2)
# print(expand(expression2))
# formula = x**2
# print(diff(formula))
# formula = x**2 + x**3 + 2
# print(diff(formula))
# print(diff(y * x**2 + y**2, x))
# print(diff(sympy.exp(x**2)))
# print(diff(sympy.sin(2*x)))
# print(diff(sympy.tan(x)))
# print(diff(sympy.tan(2*x)))
# print(diff(sympy.sin(x) - sympy.cos(2*x)))
# print(integrate(sympy.sin(x) - sympy.cos(2*x)))

# fn1 = sympy.sin(x)
# fn2 = sympy.cos(2*x)
# expression = fn1 - fn2
# answer = integrate(expression)
# print(answer)
# print(integrate(2**x, x))
# print(integrate(sympy.sin(x), (x, -oo, oo)))

# print(limit(x, x, 10))
# print(limit(x, x, 30))
# print(limit(x**2, x, 10))
# print(limit(50/x, x, 0))
# print(sympy.sin(oo))
# print(sympy.sin(0))
# print(limit(sympy.sin(x), x, 0))
# print(limit(sympy.sin(x)/x, x, 0))

# eq_1 = 2 + x + x + 5
# eq_2 = 3 + x**2 + 10
# answer1 = solve(eq_1)
# answer2 = solve(eq_2)
# print(answer1, answer2)
# print(solve(Eq(x**12, y*2), y))

# ----------------------------------------------------------------
# Find the derivative of the function f(x) = sin(x) + cos(x).
# Solve the equation tan(x) = 1 for x.
# Calculate the integral of the function g(x) = 2sin(x)cos(x).
# Find the limit of the expression (sin(x) - x)/(x^3) as x approaches 0.
# Determine the values of x for which the equation sin(x) = 0 is satisfied.
# Compute the derivative of the function h(x) = atan(x) + ln(x).
# Solve the equation sec^2(x) - 2 = 0 for x.
# Calculate the definite integral of the function f(x) = sin(x) from 0 to pi.

x = symbols('x')
y = symbols('y')

# expression = sympy.sin(x) + sympy.cos(x)
# print(solve(expression))
# print(diff(expression))

# expression = sympy.tan(x) + 1
# derivative = diff(expression, x)
# print(derivative)

# g = 2*sympy.sin(x)*sympy.cos(x)
# print(diff(g))
# g = sympy.sin(2*x)
# print(diff(g, x))

# f = sympy.sin(2*x)/sympy.cos(2*x)
# print(simplify(f))

# equation = sympy.sin(2*x)/sympy.cos(2*x)
# f = Eq(equation, 2)
# f = Eq(simplify(equation), 2)
# answer = solve(f)
# print(answer)

# limit_value = limit(expression, x, 0)
# print("Limit as x approaches 0:", limit_value)

# expression1 = sympy.sin(x) - x
# expression2 = x**3
# fn = expression1 / expression2
# # limit -> x -> 0
# expDiff1 = diff(expression1)
# expDiff2 = diff(expression2)
# fn = expDiff1 / expDiff2
# limit1 = limit(expDiff1, x, 0)
# limit2 = limit(expDiff2, x, 0)
# # (cos(x) - 1)/(3*x**2) -> 1 - 1 / 3 * 0 * 2 -> 0
# expDiff3 = diff(expDiff1)
# expDiff4 = diff(expDiff2)
# limit3 = limit(expDiff3, x, 0)
# limit4 = limit(expDiff4, x, 0)
# # -sin(x)/6x -> x -> 0 =  -sin(0)/ 6*0 => -sin 0 => 0 / 0
# expDiff5 = diff(expDiff3)
# expDiff6 = diff(expDiff4)
# fn = expDiff5 / expDiff6
# limit5 = limit(expDiff5, x, 0)
# limit6 = limit(expDiff6, x, 0)
# print(limit5, limit6)


# equation = sympy.sin(2*x)/sympy.cos(2*x)
# f = Eq(equation, 2)
# f = Eq(simplify(equation), 2)
# answer = solve(f)
# print(answer)

# Find the limit of the expression (sin(x) - x)/(x^3) as x approaches 0.
# expression1 = sympy.sin(x) - x
# expression2 = x**3
# fn = expression1 / expression2

# # print(limit(fn, x, 0)) -1/6
# diffEx1 = diff(expression1)
# diffEx2 = diff(expression2)
# fn = diffEx1 / diffEx2
# # limit x -> 0 = x = 0
# expression3 = limit(diffEx1, x, 0)
# expression4 = limit(diffEx2, x, 0)
# # print(expression3, expression4) 0 / 0
# # cos(x) - 1 -> limit x => 0, cos(0) -> 1 - 1 = 0
# # 3*x^2 -> limit x -> 0 => 3*0^2 => 0
# #  0 / 0

# expression5 = diff(diffEx1)
# expression6 = diff(diffEx2)
# fn = expression5 / expression6
# #  fn = -sin(x) / 6*x
# # limit x -> 0 = -sin(0) = 0, limit x -> 0, 6x => 6*0 => 0
# # print(limit(expression5, x, 0))
# # print(limit(expression6, x, 0))

# expression7 = diff(expression5)
# expression8 = diff(expression6)
# fn = expression7 / expression8
# limit x -> 0 = -cos(x) -> -cos(0) => -1
# limit x -> 0 = 6 => 6
# print(limit(fn, x, 0))

# Determine the values of x for which the equation sin(x) = 0 is satisfied.
# expression = Eq(sympy.sin(x), 0)
# print(solve(expression, x))

# Calculate the definite integral of the function f(x) = sin(x) from 0 to pi.
# eq1 = sympy.sin(x)
# expression = integrate(eq1, (x, 0, sympy.pi))
# print(expression)
