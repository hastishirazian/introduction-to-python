class fraction:

    #properties
    def __init__(self,n,d):
        self.numerator = n   #soorat
        self.denominator = d #makhraj


    #methods
    def sum(self , fraction1):
        # behine tar---> dg fractin 1 nemifrestim be jash---> self.num or self.den
        # abjecti ke dar main farakhani mikone dar in tabe mihe self
        result1 = self.numerator * fraction1.denominator + fraction1.numerator * self.denominator
        result2 = self.denominator * fraction1.denominator
        x = fraction(result1,result2)
        return x

    def mul(self , fraction1):
        result1 = self.numerator*fraction1.numerator
        result2 = self.denominator*fraction1.denominator
        x = fraction(result1,result2)
        return x

    def sub(self , fraction1):
        result1 = self.numerator * fraction1.denominator - fraction1.numerator * self.denominator
        result2 = self.denominator*fraction1.denominator
        x = fraction(result1,result2)
        return x

    def Div(self , fraction1):
        result1 = self.numerator * fraction1.denominator
        result2 = fraction1.numerator * self.denominator
        x = fraction(result1,result2)
        return x
    
    def fraction_to_mixed_number(self):
        if self.numerator > self.denominator:
            s = self.numerator // self.denominator
            d = self.numerator % self.denominator
            x = fraction(d,self.denominator)
            return s, fraction(d, self.denominator)

        elif self.numerator > self.denominator:
            return 1

        else:
            return 0, self

    def Simplify_fraction(self):
        n = min(self.numerator, self.denominator)
        gcd = 1
        for i in range(1, n + 1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                gcd = i

        s = self.numerator // gcd
        d = self.denominator // gcd
        return fraction(s, d)

    def show(self):
        print(self.numerator , "/" , self.denominator)
######################################################################
print("Sample examples")
a= fraction(6,8)
a.show()

b= fraction(7,1)
b.show()
# ------------------------------------------
# behine tar---> q= b.sum(a)
# chon self yani khod
print("Multiply two fractions:")
z= a.mul(b)
z.show()

print("The sum of two fractions:")
q= a.sum(b)
q.show()

print("Subtraction of two fractions:")
w= a.sub(b)
w.show()

print("Multiply two fractions:")
r= a.Div(b)
r.show()

print("The result of converting a fraction into a mixed number:")
m = a.fraction_to_mixed_number()
print(m[0] , end=' ') 
m[1].show()    

n = b.fraction_to_mixed_number()
print(n[0] ,  end=' ')  
n[1].show() 

print("Deduction Simplification:")
t= a.Simplify_fraction()
t.show()