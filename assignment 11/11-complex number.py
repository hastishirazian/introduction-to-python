class Complex :
    def __init__ (self , r , im) :
        self.real = r
        self.img = im

    def show (self) :
        print (self.real, "+" , self.img ,"i")


    def sum (self , other) :
        result_r = self.real + other.real
        result_img = self.img + other.img
        result = Complex (result_r , result_img)
        return result
    
    def sub (self , other) :
        result_r = self.real - other.real
        result_img = self.img - other.img
        result = Complex (result_r , result_img)
        return result
    
    def mul (self , other) :
        result_r = self.real * other.real - self.img * other.img
        result_img = self.img * other.real + self.real * other.img
        result = Complex (result_r , result_img)
        return result
#--------------------------------------------------------------------------------------------
a = 2
b = 3
comp_1 = Complex (a,b)
comp_1 .show ()

c = 5
d = 4
comp_2 = Complex (c,d)
comp_2 .show ()

print("The sum of two mixed numbers:")
comp_3 = comp_1.sum(comp_2)
comp_3.show()

print("Subtraction of two mixed numbers:")
comp_4 = comp_1.sub(comp_2)
comp_4.show()

print("Multiply two mixed numbers:")
comp_5 = comp_1.mul(comp_2)
comp_5.show()