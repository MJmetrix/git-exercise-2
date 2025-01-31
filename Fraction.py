class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        
        if isinstance(numerator, str):
            try:
                tempValues = numerator.text.split('/')
                self.numerator = int(tempValues[0])
                self.denominator = int(tempValues[1])
            except ValueError
                print("ValueError: Values cannot be strings")

        elif isinstance(numerator, float) or isinstance(denominator, float):
            raise ValueError("ValueError: numbers cannot be float values")

        elif isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator

        try: 
            fraction = numerator/denominator
        except ZeroDivisionError:
            print("ZeroDivisionError: Cannot divide by zero.")
        
        pass

    def gcd(a, b):
        #TODO
        #''
        # '

        pass

    def get_numerator(self):
      
        return numerator
        pass

    def get_denominator(self):
       
        return denominator
        pass

    def get_fraction(self):
       
        return fraction
        pass