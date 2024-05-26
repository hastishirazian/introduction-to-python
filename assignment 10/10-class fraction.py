class fraction:

    #properties
    def __init__(self,n,d):
        self.numerator = n   #soorat
        self.Denominator = d #makhraj


    #methods
    def sum(self):
        ...

    def mul(self , fraction1 , fraction2):
        result1 = fraction1.numerator*fraction2.numerator
        result2 = fraction1.Denominator*fraction2.Denominator
        x = fraction(result1,result2)
        return x

    def sub(self):
        ...

    def Div(self):
        ...
    
    def fraction_to_number(self):
        ...

    def show(self):
        print(self.numerator , "/" , self.Denominator)

a= fraction(6,8)
a.show()

b= fraction(7,1)
b.show()

z= a.mul(a,b)
z.show()