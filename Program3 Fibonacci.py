
from functools import reduce

# Number of elements in the Fibonacci series
n = 50

# Generate Fibonacci series
fibonacci_series = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 2), [0, 1])

result = fibonacci_series(n)

print(result)