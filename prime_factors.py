class PrimeFactors:

    def __init__(self, number):
        self.number = number
        self.data = []

    def get_data(self):
        number = self.number
        for i in range(2, self.number + 1):
            number = self._add_prime(i, number)
        return self.data

    def _add_prime(self, prime, number):
        while number % prime == 0:
            self.data.append(prime)
            number /= prime
        return number

