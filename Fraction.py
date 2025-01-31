class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        # TODO
        # Initialize denominator and numerator values```
        # can divide a string with rational numbers into two from '/'
        # `
        if isinstance(numerator, str):
            tempValues = numerator.text.split('/')
            self.numerator = int(tempValues[0])
            self.denominator = int(tempValues[1])

        elif isinstance(numerator, float) or isinstance(denominator, float):
            raise ValueError("ValueError: numbers cannot be float values")

        elif isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator

        try: 
            fraction = numerator/denominator
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        
        pass

    def gcd(a, b):
        #TODO
        #''
        # '

        pass

    def get_numerator(self):
        #TODO
        return numerator
        pass

    def get_denominator(self):
        #TODO
        return denominator
        pass

    def get_fraction(self):
        #TODO
        return fraction
        pass