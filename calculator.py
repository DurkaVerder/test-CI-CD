class Calculator:
    def add(self, first: int | float, second: int | float) -> int | float:
        return first + second

    def divide(self, dividend: int | float, divisor: int | float) -> float:
        if divisor == 0:
            raise ZeroDivisionError("division by zero")
        return dividend / divisor

    def is_prime_number(self, number: int) -> bool:
        if number < 2:
            return False

        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                return False
            divisor += 1
        return True
