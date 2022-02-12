# Amicable Adder

Amicable Adder, is a python function which performs the sum of all amicable numbers less than a maximum given as a parameter

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

## Installation

No installation requiered. Copy the amicable_adder.py in your project folder.

## Usage

```python
from amicable_adder import sum_amicables

# returns the sum of all amicable adders less than 10.000
sum_amicables(10000)
```

## Contributing
N/A


## License
N/A
