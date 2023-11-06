import pandas as pd
import numpy as np
# from string import ascii_lowercase
# import math
# import sympy
# from sympy import symbols, diff, integrate, limit, factor, expand, oo, Eq, solve, dsolve, simplify

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

# x = symbols('x')
# y = symbols('y')

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

# ----------------------------------------------------------------

# Find the derivative of the function f(x) = cos(2x) + 3sin(3x).
# Solve the equation tan(x) = sin(x) for x.
# Calculate the integral of the function g(x) = 2cos(x) - 4sin(2x).
# Find the limit of the expression (1 - cos(x))/x as x approaches 0.
# Determine the values of x for which the equation sin(2x) = 0 is satisfied.

# x = symbols('x')
# y = symbols('y')

# fn = sympy.sin(2*x) + 3*sympy.cos(3*x)
# print(fn)
# answer = diff(fn)
# print(answer)

# equation = Eq(sympy.tan(x), sympy.sin(x))
# print(solve(equation))

# expression1 = sympy.cos(x)
# fn = (1 - expression1) / x
# # print(fn)
# # print(limit(fn, x, 0))
# lm1 = limit(expression1, x, 0)
# fnNew = 1 - limit(expression1, x, 0) / 0
# diff1 = diff(1 - expression1, x)
# diff2 = diff(x)
# fnNew = diff1 / diff2
# lm2 = limit(fnNew, x, 0)
# ----------------------------------------------------------------

# students = ['Andrew', 'John', 'Mark']
# age = [20, 10, 20, 30,]
# mixed = [True, 'John', {"name": "Mark", "age": 20}]
# some_dict = {0: "students", 1: "students", 2: "students"}
# a_dict = pd.Series(some_dict)
# b_dict = pd.Series(some_dict)

# x = pd.Series({f"data_{item}": item for item in range(10)})
# x = pd.Series(data=list(range(10)), index=map(lambda item: 'data_' + str(item), range(10)))
# x = a_dict.add_prefix('data_')
# print(x['data_0':'data_1'])
# print(x['data_0'])
# print(x.data_1)
# print(a_dict[[True, False, True]])
# print(a_dict.loc[[True if i % 2 == 0 else False for i in range(3)]])


# loc => location => indexing by labels, Labels based data selecting method
# iloc => integer loc => indexing by positions, if we are using iloc the last index value is not observer.
# last index value.

# print(a_dict.iloc[0])
# print(a_dict.iloc[0:3])

# print(a_dict.iloc[[0, 1, 2]])
# print(x)
# print('----')
# print(x.loc[lambda item: ['data_2', 'data_3']])
# print(x.loc[lambda item: [True for i in range(x.size)]])

# Indexing with callables -> A callable is just an object which is accepts some arguments and
# possibly returns something. Classes in python technically callables, but possibly the simplest
# example and the best example is function.

# print(x.loc[lambda item: ['data_0', 'data_1', 'data_2']])
# print(x.loc[lambda item: [True for i in range(x.size)]])
# print(x.loc[lambda item: [True if item % 5 == 0 else False for item in range(x.size)]])
# print(x[lambda item: [True if item % 5 == 0 else False for item in range(x.size)]])

# def everyFifthItem(x):
#     return [True if item % 5 == 0 else False for item in range(x.size)]

# print(x.loc[everyFifthItem])

# print(x.get('data_1'))
# print(x.get('data_2'))
# print(x.get('data_4'))
# print(x.get('data_10', default=None))

# a = [item**2 for item in range(100)]
# b = pd.Series(a)
# c = b.tail(3)
# d = b.iloc[-3:]
# print(pd.Series.equals(d, c))

# ----------------------------------------------------------------
# file = pd.read_csv("./SampleCSVFile_556kb.csv",)
# file = pd.read_csv("./SampleCSVFile_556kb.csv", usecols=['country', 'total_litres_of_pure_alcohol'])
# file = pd.read_csv("./SampleCSVFile_556kb.csv", usecols=['country', 'total_litres_of_pure_alcohol'], index_col='country')
# file = pd.read_csv("./SampleCSVFile_556kb.csv", usecols=['country', 'total_litres_of_pure_alcohol'], index_col='country')
# newFile = file.squeeze('columns')  # convert dataFrame to series
# print(file.head())
# print(file.tail())
# print(type(file))
# print(file.size)
# print(file.values)
# print(file.index)
# print(file.shape)
# print(len(file))

# print(newFile.is_unique)
# print(type(newFile))
# print(newFile.head(10).is_unique)
# print(newFile.head(5).is_unique)
# print(newFile.head(5).nunique())
# print(newFile.nunique())
# print(newFile.nunique(dropna=False)) # Series.nunique(dropna=True) -> Excludes NA values by default. Don’t include NaN in the count.

# print(pd.Series([1, 2, 3]).is_monotonic_increasing)
# print(pd.Series([1, 2, 3]).is_monotonic_decreasing)
# print(pd.Series([1, 2, 3, 3, 3, 3, 3, 3, 3]).is_monotonic_increasing)
# print(pd.Series([3, 2, 1, 3, 4, 1]).is_monotonic_decreasing)

# print(pd.Series(reversed([1, 2, 3, 4, 5, 6, 7])).is_monotonic_decreasing)
# print(newFile.size) # return the size of the pandas series
# print(newFile.count()) # return the number of not null items in pandas series
# print(newFile.hasnans) # return true and false if series has nan items or null items.

# print(newFile.isnull())
# print(newFile[newFile.isnull()]) # return all the null values
# print(newFile[newFile.isnull()].values)
# print(newFile[newFile.isnull()].index)
# nan_values_list = list(newFile[newFile.isnull()].index)
# print(newFile[nan_values_list])

# print(newFile[newFile.isnull()].size)
# print(len(list(newFile[newFile.isnull()].index)))
# print(newFile.isnull().sum()) # return the sum of the all True values.

# all = newFile.size  # return the size of the series
# non_nulls = newFile.count()  # return the count of not null values
# nulls = newFile.isnull().sum()  # return the sum of all null values
# print(all == non_nulls + nulls)

# ----------------------------------------------------------------

# ser = pd.Series(data=[True, False, None, 2], dtype=float)
# print(np.isnan(ser))
# print(ser.isnull())
# print(newFile[newFile.isnull()].size)
# print(newFile[np.isnan].size)

# not null values
# print(newFile[newFile.notnull()])
# print(newFile.notnull())
# print(newFile.isnull())
# print(newFile.notnull().sum() + newFile.isnull().sum() == newFile.size)

# wine_serving = newFile[newFile.notnull()]
# print(wine_serving[wine_serving > 10])
# print(newFile.dropna())
# print(newFile.dropna(inplace=True)) # change the existing variable value.
# print(newFile)

# print(newFile.fillna(100, inplace=False))
# newFile.fillna(100, inplace=True)
# print(newFile)

# print(newFile.sum())
# print(newFile.count())
# print(newFile.sum() / newFile.count())
# print(newFile.mean())

# Descriptive analysis -> It's a branch of mathematical dealing with the collection, analysis, interpretation ane
# presentation of masses of numerical data.
# Descriptive statistics are used to describe / summarize the large data in the way that are meaningful and useful

# marks = np.random.random(50) * 100
# marks_series = pd.Series(marks)
# print(marks_series.describe())
# print(marks_series.max())
# print(marks_series.min())
# print(marks_series.count())
# print(marks_series.dtype)

# n1 = np.random.random(5) * 100
# n2 = np.random.random(5) * 100
# n3 = np.random.random(5) * 100
# n4 = np.random.random(5) * 100

# df = pd.DataFrame({'A': n1, 'B': n2, "C": n3, "D": n4})
# print(df.max())  # return the max values from every column
# print(df.max('index'))
# print(df)
# print(df.max('columns'))  # return the max values from every column

# print(df.count())
# print(df.count(axis='columns'))
# print(df.count(axis='index'))
# print(df.count(axis='columns', numeric_only=True)) # if numeric_only is true, then only float, int and bool values are returned
# print(df.count(axis='columns', numeric_only=False))

# print(df.sum())
# print(df.sum(axis='columns'))
# print(df.sum(axis='index'))
# print(df.sum(axis='columns', numeric_only=True))
# print(df.sum(axis='columns', numeric_only=False))

# mean => Average
# print(1 + 2 + 2 - 1 / 4)
# print(df.mean(axis='index'))
# print(df.mean(axis='columns'))

# median => Return the middle of the values
# print(df.median(axis='index'))
# print(df.median(axis='columns'))
# j = pd.Series([1, 2, 3, 4])
# print(j.median())

# mode => most repetitive values
# j = pd.Series([1, 2, 3, 4, 4])
# print(j.mode())
# print(df.mode(axis='index'))
# print(df.mode(axis='columns'))

# df_new = pd.DataFrame({"A": [1, 2, 2, 4], "B": [4, 4, 6, 1], "C": [1, 1, 3, 4]})
# print(df_new.mode(axis='columns'))
# print(df_new.mode(axis='index'))

# Quantiles - In terms of statistics, Median is a quantile because it splits the data into the equal proportion.
# Quantiles - In statistics and probability quantiles are cut points dividing the range of a probability distribution into
# continuous intervals with equal probabilities, or dividing the observations in a sample in the same way.
# The 2 quantiles are called the median
# The 3 quantiles are called the terciles
# The 4 quantiles are called the quartiles
# The 5 quantiles are called the quintiles
# the 10 quantiles are called the deciles
# the 100 quantiles are called the percentiles

# quantile(q=0.5, axis='index')
# q = float or array-like, default 0.5 (50%). 0 < q < 1

# print(df)
# print(df.quantile(q=0.25, axis='columns'))
# print(df)
# print(df.quantile(q=[0.25, 0.5], axis='columns'))
# print(df.quantile(axis='columns'))
# print(df.median(axis='columns'))

# l = [20, 25, 30, 50, 23, 60, 100]
# s = pd.Series(l)
# print(s.quantile(q=0.20))  # 20% students marks 24 less.


# ----------------------------------------------------------------

# Standard deviation calculate the difference between actual values and average values for given observations. The larger
# the difference is higher is the standard  deviation.

# 8, 4, 6, 10, 4, 2, 14 -> 48 / 7 => 6.85
# x - bar_x -> 8 - 6.85 -> 1.15, for all items.
# (x - bar_x)^2 => 1.15^2 -> 1.32 for all items.
# sqrt((x - bar_x)^2 / x - 1)  -> 102.84 / 6 => 4.14

# df = pd.DataFrame([8, 4, 6, 10, 4, 2, 14])
# print(df.std())
# print(df_new.std(axis='columns'))
# print(df_new['A'].std())

# print(df_new.sum(axis='columns'))
# print(df_new.count())

# ar = np.array([12, 23, 34, 33, 21, 10, 45])
# df = pd.Series(ar)
# print(df.mean())
# print(df.var())  # 159.61904761904762
# print(df.mean()) # 25.428571428571427
# y = (ar - df.mean())**2
# print(y.sum() / 6)
# print(df_new.describe())

# df = pd.DataFrame({"Mp": [40, 54, 32, 48], "Up": [58, 50, 69, 59], "Ap": [38, 34, 27, 36], "Pb": [42, 47, 55, 61], "hr": [27, 38, 20, 52]})
# print(df.sum(axis='columns'))
# print(df)
# print(df['Pb'].mean())
# print(df)
# print(df.describe())
# print(df.max(axis='columns'))
# print(df['Pb'].min())
