class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        
        if isinstance(numerator, str):
            try:
                tempValues = numerator.split("/", 1)
                self.numerator = int(tempValues[0])
                self.denominator = int(tempValues[1])
            except ValueError:
                self.fraction_string = '0'
                return
                
        elif isinstance(numerator, float) or isinstance(denominator, float):
            self.fraction_string = '0'
            return

        elif isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator

        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
            
        if self.denominator == 0:
            raise ZeroDivisionError("ZeroDivisionError: Cannot divide by zero.")
        
        elif self.numerator == 0:
            self.fraction_string = '0'
            return

        else:
            self.divisor = self.gcd(self.numerator, self.denominator)
            self.fraction_string = str(int(self.numerator/self.divisor)) + '/' + str(int(self.denominator/self.divisor))
       
        pass
    @staticmethod
    def gcd(a, b):

        #The Euclidean Algorithm is used to compute for the GCD.        
        
        a = abs(a)
        b = abs(b)
        
        if b == 0 or a == 0:
            return 0
        
        while b != 0:
            a = b
            b = a % b
        return a

    def get_numerator(self):    
        
        return self.numerator
        pass

    def get_denominator(self):
       
        return self.denominator
        pass

    def get_fraction(self):
        
        return self.fraction_string
        pass



