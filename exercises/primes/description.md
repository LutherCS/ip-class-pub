# Basic JavaScript

## Overview

Implement the following functionality.

1. Read parameters `name` and `number` from the URL query string
2. Generate a page based on the provided values:
   1. Display an individualized greeting
   2. Display whether the number is prime
   3. Display a table of the first `number` primes
3. If any value is not provided in the URL, use the following defaults: *student* for `name` and *330* for `number`

## HTML

In order to pass the provided tests your elements must have the following attributes:

1. Greeting: level 1 header with the id `greeting`.
2. Number information: paragraph with the id `numberInfo`.
3. Table of *prime* numbers: table with the id `nPrimes`

Classes of these elements are left at your discretion and depend on the chosen CSS framework (see below).

## CSS

Use *Bootstrap* or other framework to style the greeting, the information about the number, and the table of primes.

## JavaScript

Break the implementation into the following functions. See the *primes.js* for implementation details and *test_primes.py* for expected result.

1. `greet(name, selector)`: Greets user by name.
2. `isPrime(number)`: Checks if a number is prime.
   1. Example: `isPrime(2)` returns `true`
   2. Example: `isPrime(4)` returns `false`
3. `printNumberInfo(number, selector)`: Prints whether a number is prime.
4. `getNPrimes(number)`: Generates an array of prime numbers.
   1. Example: `getNPrimes(2)` returns `[2, 3]`
   2. Example: `getNPrimes(4)` returns `[2, 3, 5, 7]`
5. `printNPrimes(number, selector)`: Prints a table of prime numbers.

## Running

Use Python built-in HTTP server to run your application. Your program must properly handle all cases as values may or may not be provided in the URL query string.

Case 1: both values provided

```text
http://localhost:8000/primes.html?name=Roman&number=4
```

Case 2: only name is provided

```text
http://localhost:8000/primes.html?name=Roman
```

Case 3: only number is provided

```text
http://localhost:8000/primes.html?n=4
```

Case 4: no values are provided

```text
http://localhost:8000/primes.html
```

## Testing

Requires `pytest` and `playwright`.

Run the following:

```bash
python -m pytest -v tests/primes
```

## Demonstration

![Demo](primes.apng)
