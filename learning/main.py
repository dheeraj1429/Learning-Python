import pandas as pd
import numpy as np
import timeit
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

# ----------------------------------------------------------------

# df = pd.DataFrame({"cname": ["ram", "ram", "ram", "joe", "joe", "Kar"],
#                    "iname": ["soap", "soap", "soap", "slat", "salt", "soap"],
#                    "rate": [100, 200, 100, 80, 45, 40]
#                    })

# print(df)
# print(df.pivot_table(index='cname', columns='iname', values='rate', aggfunc='mean'))
# print(df.pivot_table(index='cname', columns='iname', values='rate', aggfunc='mean').fillna(0))

# df = pd.read_csv('./SampleCSVFile_556kb.csv', usecols=['country', 'total_litres_of_pure_alcohol'], index_col='country')
# new_df = df.squeeze('columns')
# print(df.sum(numeric_only=True))
# print(df.sum() / df.count())
# print(df.mean())
# print(df.median())
# print(df.quantile(q=.5))
# print(df.quantile(.5))
# print(df.quantile(0.75) - df.quantile(0.25))
# print(new_df)
# print(new_df.max())
# print(new_df[new_df == new_df.max()].index[0])
# print(new_df.idxmax())
# print(new_df.idxmin())
# print(new_df.value_counts()) # get the values count.
# print(new_df[new_df.idxmax()])

# sorting.
# print(df.dropna(inplace=False))
# print(df.sort_values(by='total_litres_of_pure_alcohol', ascending=True))
# print(df.sort_values(by='total_litres_of_pure_alcohol', ascending=False))
# print(df.dropna(inplace=False).sort_values(by='total_litres_of_pure_alcohol', ascending=False))
# print(df.dropna(inplace=False).sort_values(by='total_litres_of_pure_alcohol', ascending=True))
# print(df.sort_values(by='total_litres_of_pure_alcohol', ascending=False, na_position='first'))
# print(df.sort_values(by='total_litres_of_pure_alcohol', ascending=False, na_position='last'))
# print(df.sort_values(by='total_litres_of_pure_alcohol', ascending=False, na_position='last', inplace=True))
# print(df)

# print(new_df.min())
# print(new_df.max())
# print(df.sort_values(by='total_litres_of_pure_alcohol', ascending=True)[:10])
# print(new_df.sort_values(ascending=True, na_position='last')[:10])
# print(df.sort_values(by='total_litres_of_pure_alcohol', ascending=True).nsmallest(columns='total_litres_of_pure_alcohol', n=20))
# print(df.sort_values(by='total_litres_of_pure_alcohol', ascending=True).nsmallest(columns='total_litres_of_pure_alcohol', n=10))
# print(df.sort_values(by='total_litres_of_pure_alcohol', ascending=True).nsmallest(columns='total_litres_of_pure_alcohol', n=29))
# print(df.nsmallest(columns='total_litres_of_pure_alcohol', n=29))

# sort by index
# print(new_df.head(10))
# print(new_df.sort_index())
# print(df.sort_index(ascending=True))
# print(df.sort_index(ascending=False))
# print(df.index.isnull().sum())

# x = new_df[new_df < 50]
# print(x.sort_values()[:20])
# y = x.nsmallest(n=20)
# print(y.mean())
# print(y.median())
# print(y.std())
# print(y.describe())

# print(df.fillna(10))
# print(df * 2)

# x = pd.Series({"am": 2, "Am": 2})
# new_df.sort_index(inplace=True)
# x + new_df
# print(new_df + x)
# print(new_df + x)
# print(new_df.add(x, fill_value=0))
# print(new_df.divide(x, fill_value=1))
# print(new_df.multiply(x, fill_value=1))
# print(new_df.std())
# print(((new_df.subtract(new_df.mean())**2).sum() / new_df.count() - 1)**(1/2))

# print('total', new_df.size)
# print('nut null', new_df.notnull().sum())
# print(new_df.isnull().sum())
# print(new_df.count() + new_df.isnull().sum())

# print(df.std()) # 3.454136
# print(((new_df.subtract(new_df.mean())**2).sum() / (new_df.count() - 1))**(1/2))
# print(new_df.sum())
# print(new_df.cumsum())
# print(new_df)
# print(pd.Series([1, 2, 3]).cumsum())
# print(new_df.cumsum(skipna=False))
# print(new_df.cumsum(skipna=True))

# data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
# df = pd.DataFrame(data)
# print(df)
# print(df.prod())
# print(10 * 13 * 9)
# print(df.prod(axis='index'))
# print(new_df.prod())
# print(new_df.cumprod())

# data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
# df = pd.DataFrame(data)
# print(df)
# print(df.prod(axis='columns'))
# print(df.cumprod(axis="columns"))

# print(new_df.diff(periods=1))
# print(new_df.diff(periods=-1))
# print('v1', 0.7 - 4.9, 'v2', 12.4 - 0.7, 'v3', 5.9 - 12.4) # periods = 1
# print('v1', 4.9 - 0.7, 'v2', 0.7 - 12.4, 'v3', 12.4 - 5.9)  # periods = -1
# for item in new_df.items():
#     print(item)
# print(new_df.filter(regex='^V'))
# print(new_df.filter(like='stan'))
# print(new_df.filter(like='Af'))
# print(new_df[lambda item: item > 10])
# print(df.where(lambda x: x > 10, other='value are two small'))
# print(df.where(lambda x: x > 10).dropna())

# print(df.mask(lambda x: x > 10).dropna())  # opposite of df.where()
# df.loc['Afghanistan'] = 20
# print(df)

# update series
# new_df.update(pd.Series(data=[200, 100], index=["Afghanistan", 'Bangladesh']))
# print(new_df.head(30))

# apply
# print(new_df)
# print(new_df.apply(lambda x: x + 2))
# print(new_df + 2)
# print(new_df.apply(np.square))

# passing the args


# def multiply_by_value(item, value):
#     if item > value:
#         return item ** 2
#     return item


# we can't use the map function with this approach. instead we can use the the apply function with callable
# one way to pass the parameters
# print(new_df.apply(multiply_by_value, value=10))
# another way to pass the parameters
# print(new_df.apply(multiply_by_value, args=(10,)))

# print(new_df.map(lambda x: x**2))
# print(new_df.apply(lambda x: x**2))


# ----------------------------------------------------------------
# df = pd.read_csv('./SampleCSVFile_556kb.csv', usecols=['wine_servings', 'country'], index_col='country')
# series_data = df.squeeze('columns')
# print(series_data)
# print(series_data.mean())
# print(series_data.median())
# print(series_data.std())
# print(series_data[:10])
# print(df.mean())
# print(df.median())
# print(df.quantile(0.5))
# print(df.std())
# print(df.var()**(1/2))
# print(np.sqrt(df.var()))
# print(df.describe())
# print(df.head(10).diff())
# print(df[:10] - df.mean())
# print((series_data[:10] - series_data.mean()).apply(lambda x: 'high' if x > 0 else 'low').value_counts())

# z scores
# print(((series_data - series_data.mean()) / series_data.std()).head(10))
# print(((series_data - series_data.mean()) / series_data.std()).max())
# print(((series_data - series_data.mean()) / series_data.std()).min())

# print(series_data[series_data.idxmax()])
# print((series_data[series_data.idxmax()] - series_data.mean()) / series_data.std())

# ----------------------------------------------------------------
# names = ["John", "Amo", "Nen", "Hasa"]
# ages = [20, 30, 21, 40]
# married = [False, False, True, False]

# ser = pd.Series(names)  # pd.Series always used one dimensional
# print(ser)
# print(ser[0])
# print(ser[ser == 'John'])
# print(ser.iloc[1])
# print(ser.ndim)
# print(ser.shape)
# print(ser.dtype)

# df = pd.DataFrame({"names": names, "ages": ages, "married": married})  # pd.Series used two dimensional
# print(df)
# print(df['names'][1])
# print(df.iloc[2, 0])
# print(df.iloc[0])
# print(df.ndim)
# print(df.shape)
# print(df.dtypes)

# more ways to create pandas data frames.
# tuple_name = tuple(names)
# tuple_ages = tuple(ages)
# tuple_married = tuple(married)
# print(tuple_name, tuple_ages, tuple_married)
# print(pd.DataFrame({"names": tuple_name, "ages": tuple_ages, "married": tuple_married}))
# print(pd.DataFrame({"names": pd.Series(tuple_name), "ages": pd.Series(tuple_ages), "married": pd.Series(tuple_married)}))

# dict_names = {key: value for key, value in enumerate(tuple_name)}
# dict_ages = {key: value for key, value in enumerate(tuple_ages)}
# dict_married = {key: value for key, value in enumerate(tuple_married)}
# print(pd.DataFrame({"names": dict_names, "ages": dict_ages, "married": dict_married}))

# print(pd.DataFrame([{"names": name, 'ages': age, "married": married} for name, age, married in zip(tuple_name, tuple_name, tuple_married)]))
# print(df.info(verbose=False))
# print(df.info(verbose=True))
# print(df.info(max_cols=10))
# print(df.info(memory_usage=True))
# print(df.info(memory_usage=False))
# print(df.info(memory_usage='deep'))
# ----------------------------------------------------------------

# nutrition = pd.read_csv('./nutrition.csv')
# print(nutrition.info(verbose=False, memory_usage='deep'))
# print(nutrition.head())
# print(nutrition['Unnamed: 0'])

# remove columns from the data frame. return new data frame with excluded the columns
# nutrition_new_df = nutrition.drop('Unnamed: 0', axis='columns')
# print(nutrition_new_df)

# print(nutrition.set_index('Unnamed: 0'))
# print(nutrition)

nutrition = pd.read_csv('./nutrition.csv', index_col=[0])
# print(nutrition.sample())
# print(nutrition.sample(random_state=12))
# print(nutrition.sample(n=4))

# print(nutrition.sample(frac=.01))
# print(nutrition.sample(n=3, replace=True))
# print(nutrition.axes[0])
# print(nutrition.axes[1][30])
# print(nutrition.columns[30])

# print(nutrition.axes[1])
# nutrition.set_index('name', inplace=True)
# print(nutrition)
# print(nutrition.set_index('total_fat', drop=True, append=True));
# print(nutrition.set_index('total_fat', drop=True, append=True, verify_integrity=False))
# nutrition.set_index('name', drop=True, verify_integrity=True, inplace=True)
# print(nutrition.loc['Eggplant, raw'])
# print(type(nutrition.loc['Eggplant, raw']))
# print(nutrition.loc['Eggplant, raw']['alcohol'])
# print(nutrition.loc['Eggplant, raw', 'alcohol'])

#
# print(nutrition.loc["Eggplant, raw":"Sherbet, orange", "calories":"choline"])
# print(nutrition.loc[["Eggplant, raw", "Sherbet, orange"], ["calories", "choline"]])

# print(nutrition.loc[[0, 1, 2]])
# print(nutrition.iloc[[1]])

# print(nutrition.index)
# print(nutrition.columns)

range_index = pd.RangeIndex(start=0, stop=8789, step=1)
nutrition.index = range_index
# print(type(nutrition.index))
# print(nutrition.set_index('serving_size', drop=False, append=True))
# print(nutrition.set_index('serving_size', drop=True, append=False, verify_integrity=False))
nutrition.set_index('name', inplace=True)
# print(nutrition.loc['Eggplant, raw'])
# print(nutrition.loc['Eggplant, raw']['total_fat'])
# print(type(nutrition.loc['Eggplant, raw']))

# print(nutrition.loc[['Eggplant, raw', 'Teff, uncooked'], ['calories', 'choline']])
# print(type(nutrition.loc[['Eggplant, raw', 'Teff, uncooked']]))
# print(nutrition.loc[['Eggplant, raw', 'Sherbet, orange']])
# print(nutrition.loc['Eggplant, raw':'Sherbet, orange', 'calories':'choline'])

# print(nutrition.iloc[3])
# print(nutrition.iloc[3, :])
# print(nutrition.iloc[[2, 3, 4], [1, 2, 3]])
# print(type(nutrition.iloc[[2, 3, 4], 1]))
# print(type(nutrition.iloc[[2, 3, 4], [1]]))
# print(nutrition.iloc[[2, 3, 4], 1])

# print(nutrition.loc['Cornstarch', 'calories'])
# print(nutrition.iloc[0, 1])

# single value extraction
# print(nutrition.at['Cornstarch', 'calories'])  # label based extraction
# print(nutrition.iat[0, 1]) # index based extraction


# def my_function():
# print(nutrition.loc['Cornstarch', 'calories'])
# print(nutrition.at['Cornstarch', 'calories'])


# time_taken = timeit.timeit(my_function, number=1000)
# print(f"Time taken: {time_taken} seconds")

# two ways to get the single value from the data frame.
# print(nutrition.loc['Eggplant, raw', 'vitamin_k'])
# print(nutrition.at['Eggplant, raw', 'vitamin_k'])

# get the column index
# print(nutrition.columns.get_loc('vitamin_k'))

samples = nutrition.sample(n=10, axis=0)
# print(samples.shape)
# print(samples)
# print(samples.loc[:, ['total_fat', 'cholesterol']])
# b12 = samples.columns.get_loc('vitamin_b12')
# print(samples.iloc[0:10, b12])

# print(samples.fatty_acids_total_trans.sum())
# print(samples.fatty_acids_total_trans)
# print(samples.fatty_acids_total_trans.max())

# replace the values regex, and then convert the data type string to float or int,
# ndf = samples.fatty_acids_total_trans.replace(to_replace='\smg', value='', regex=True)
# ndf = ndf.astype(float)
# print(ndf.sum())
# print(ndf.max())
