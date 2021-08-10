"""
References:
    https://projecteuler.net/problem=16
"""
from project_euler.root.perfect_digital_invariant import happy_function

if __name__ == "__main__":
    print(happy_function(2 ** 1_000))
