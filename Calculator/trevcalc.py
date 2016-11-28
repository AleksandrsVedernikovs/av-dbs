class Calculator():

    # this adds two as given
    def add(self, a,b):
        return a + b
    #print add(5,15)
    #print add(-5,15)
    #print add(0,15)
    #print (20 == add(5,15))
    #print (10 == add(-5,15))
    #print (15 == add(0,15))
    
    # this subtracts 'a' - 'b'
    def sub(self, a,b):
        return a - b
    #print sub(5,3)
    #print sub(-5,3)
    #print sub(5,-3)
    #print (2 == sub(5,3))
    #print (-8 == sub(-5,3))
    #print (8 == sub(5,-3))
    
    # this multiplies 'a' by 'b'    
    def mul(self, a,b):
        return a * b
    #print mul(8,7)
    #print mul(0,7)
    #print mul(-8,7)
    #print (56 == mul(7,8))
    #print (0 == mul(0,8))
    #print (-56 == mul(-7,8))
    
    # this divides 'a' by 'b'
    def div(self, a,b):
        if b == 0:
            print ("Can't divide by Zero")
        else:
            return a / b
    #print div (256,16)
    #print div (256,-16)
    #print div (0,16)
    #print (16 == div(256,16))
    #print (-16 == div(256,-16))
    #print (0 == div(0,16))
        
    # this squares the 'a'
    def squared(self, a):
        return a ** 2
    #print squared(4)
    #print squared(0)
    #print squared(1)
    #print (16 == squared(4))
    #print (0 == squared(0))
    #print (1 == squared(1))
    
    # this extracts square root of the 'a'
    def square_root(self, a):
        if a < 0:
            print("Invalid Input :")
        else:
            return a ** 0.5
    #print square_root(25)
    #print square_root(256)
    #print square_root(1)
    #print (5 == square_root(25))
    #print (16 == square_root(256))
    #print (1 == square_root(1))
    
    # this exponentiates  'a' to the power of 'b'
    def exponentiate(self, a,b):
        return a ** b
    #print exponentiate(2,3)
    #print exponentiate(2,4)
    #print exponentiate(0,3)
    #print (8 == exponentiate(2,3))
    #print (16 == exponentiate(2,4))
    #print (0 == exponentiate(0,3))
        
    # this cubes the 'a'
    def cube(self, a):
        return a ** 3
    #print cube(5)
    #print cube(0)
    #print cube(15)
    #print (125 == cube(5))
    #print (0 == cube(0))
    #print (3375 == cube(15))
    
    # this extracts cube root of the 'a'
    def cube_root(self, a):
        if a >= 0:
            return round(a ** 0.33)
        if a < 0:
            return round(-(-a) ** 0.33)
    #print cube_root(125)
    #print cube_root(875)
    #print cube_root(0)
    #print (5 == cube_root(125))
    #print (9== cube_root(875))
    #print (0 == cube_root(125))
    
    # this calculates factorial of the 'a'
    def factorial(self, a):
        if a < 0:
            print("Invalid Input: ")
        elif a == 0:
            return 1
        else:
            return a * float(self.factorial(a-1))
            
    # this calculates Sin of the 'a'
    def sin(self, a):
        radians = a*(3.14159265358979323846/180)
        return round(((radians) - ((radians**3)/Calculator().factorial(3)) + ((radians**5)/Calculator().factorial(5))- ((radians**7)/Calculator().factorial(7))+((radians**9)/Calculator().factorial(9))), 4)
    #print sin(5)
    #print sin(0)
    #print sin(-2)
    #print (0.0872 == sin(5))
    #print (0 == sin(0))
    #print (-0.0349 == sin(-2))
    
    # this calculates Cos of the 'a'
    def cos(self, a):
        radians = a*(3.14159265358979323846/180)
        return round((1 - ((radians**2)/Calculator().factorial(2)) + ((radians**4)/Calculator().factorial(4))- ((radians**8)/Calculator().factorial(8))+((radians**10)/Calculator().factorial(10))), 4)
    #print cos(2)
    #print cos(0)
    #print cos(-1)
    #print (0.9994 == cos(2))
    #print (1 == cos(0))
    #print (0.9998 == cos(-1))

if __name__ == '__main__':

# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
    def calculation():
        if choice == 1:       
            return Calculator().add(a,b)
        elif choice == 2:
            return Calculator().sub(a,b)
        elif choice == 3:
            return Calculator().mul(a,b)
        elif choice == 4:
            return Calculator().div(a,b)
        elif choice == 5:
            return Calculator().squared(a)
        elif choice == 6:
            return Calculator().square_root(a)
        elif choice == 7:
            return Calculator().exponentiate(a,b)
        elif choice == 8:
            return Calculator().cube(a)
        elif choice == 9:
            return Calculator().cube_root(a)
        elif choice == 10:
            return Calculator().factorial(a)
        elif choice == 11:
            return Calculator().sin(a)
        elif choice == 12:
            return Calculator().cos(a)
        elif choice == 13:
            exit()

    def menu():
        #print what options you have
        print "Welcome to calculator.py"
        print "your options are:"
        print " "
        print "1) Addition"
        print "2) Subtraction"
        print "3) Multiplication"
        print "4) Division"
        print "5) Squared"
        print "6) Square_Root"
        print "7) Exponentiate"
        print "8) Cube"
        print "9) Cube_root"
        print "10) Factorial"
        print "11) Sin"
        print "12) Cos"
        print "13) Quit calculator.py"
        print " "
        return input ("Choose your option: ")
        
        
        
    choice = menu()   
    if choice == 5 or choice == 6 or choice == 8 or choice == 9 or choice == 10 or choice == 11 or choice == 12:
        a = raw_input('Enter a :')
        a = float(a)
    elif choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice ==7:
        a = raw_input('Enter first a :')
        a = float(a)
        b = raw_input('Enter second b :')
        b = float(b)
    elif choice == 13:
            exit()
    else:
        print ('Please choose from menu options: ')
            
    print calculation() 