#!/usr/bin/env python3
""" 2. Poisson CDF """


class Poisson():
    """represents a poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """class constructor"""

        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) <= 1:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data)) / len(data)

    def pmf(self, k):
        """calculates the value of the PMF for a given number of “successes”"""

        e = 2.7182818285
        if k < 0:
            return 0

        if type(k) is not int:
            k = int(k)

        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)

        return ((self.lambtha ** k) * (1 / (e ** self.lambtha))) / factorial(k)

    def cdf(self, k):
        """Calculates the value of the CDF for a given number of “successes”"""

        if type(k) is not int:
            k = int(k)

        if k < 0:
            return 0
        else:
            res = 0
            for i in range(k + 1):
                res += self.pmf(i)
            return res
