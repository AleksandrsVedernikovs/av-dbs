class Car(object):
 
    def __init__(self):
        self.__make = ''
        self.__model = ''
        self.__year = ''
        self.__engine_size = ''
        self.__reg = ''    
        self.__type = ''
        
    def setup(self, make, model, year, engine_size, reg, type):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__engine_size = engine_size
        self.__reg = reg
        self.__type = type
        if self.__type == 'petrol':
            Dealership.petrol_cars_avail.append((self.__make, self.__model, self.__year, self.__engine_size, self.__reg))
        if self.__type == 'diesel':
            Dealership.diesel_cars_avail.append((self.__make, self.__model, self.__year, self.__engine_size, self.__reg))
        if self.__type == 'hybrid':
            Dealership.hybrid_cars_avail.append((self.__make, self.__model, self.__year, self.__engine_size, self.__reg))
        if self.__type == 'electric':
            Dealership.electric_cars_avail.append((self.__make, self.__model, self.__year, self.__engine_size, self.__reg))
            
    def getmake(self):
        return self.__make
        
    def getmodel(self):
        return self.__model
        
    def getyear(self):
        return self.__year
    
    def getengine_size(self):
        return self.__engine_size
        
    def getreg(self):
        return self.__reg





class Dealership(object):

    
    petrol_cars_avail = []
    diesel_cars_avail = []
    hybrid_cars_avail = []
    electric_cars_avail = []
        
    petrol_cars_rented = []
    diesel_cars_rented = []
    hybrid_cars_rented = []
    electric_cars_rented = []
        
    def menu(self):
        #print what options you have
        print "###################################################################"
        print "#                  Welcome to car_rental.py                       #"
        print "#                  Your options are:                              #"
        print "#                        >>><<<                                   #"
        print "#                  1) Rent                                        #"
        print "#                  2) Return                                      #"
        print "#                  3) Quit App                                    #"                                 
        print "###################################################################"
        print 'There are %s petrol , %s diesel, %s hybrid and %s electric cars available for you.' % (len(Dealership().petrol_cars_avail), len(Dealership().diesel_cars_avail), len(Dealership().hybrid_cars_avail), len(Dealership().electric_cars_avail))
        while True:
            choice = raw_input('Select option> ')
            if int(choice) == 1 or int(choice) == 2:
                choice = int(choice)
                break
            elif int(choice) == 3:
                print 'Thank you'
                exit()
            else: 
                print 'Invalid selection. Try again'
                continue
        if choice == 1: 
            print '************ Rent|Choose type: ***********'
            print '#               1. Petrol                #'
            print '#               2. Diesel                #'
            print '#               3. Hybrid                #'
            print '#               4. Electric              #'
            print '#               5. Back to menu          #'
            print '******************************************'
            self.rental_process()
        if choice == 2:
            print '*********** Return|Choose type: **********'
            print '#               1. Petrol                #'
            print '#               2. Diesel                #'
            print '#               3. Hybrid                #'
            print '#               4. Electric              #'
            print '#               5. Back to menu          #'
            print '******************************************'
            self.return_process()
    
    def rental_process(self):
        answer = raw_input('Select type> ') 
        if answer == '1':
            print '\n>>>>>>  Petrol cars available:  <<<<<<<<<<'
            for car in self.petrol_cars_avail:
                car_details = []
                for attr in car:
                    car_details.append(attr)
                print (self.petrol_cars_avail.index(car)+1), (" ".join([str(elem) for elem in car_details]))
            car_choice = raw_input('Select car> ')
            car_choice = int(car_choice)
            self.petrol_cars_rented.append(self.petrol_cars_avail.pop(car_choice - 1))
            renting.menu()
                
        if answer == '2':
            print '\n>>>>>>>>  Diesel cars available:  <<<<<<<<<<'
            for car in self.diesel_cars_avail:
                car_details = []
                for attr in car:
                    car_details.append(attr)
                print (self.diesel_cars_avail.index(car)+1), (" ".join([str(elem) for elem in car_details]))
            car_choice = raw_input('Select car> ')
            car_choice = int(car_choice)
            self.diesel_cars_rented.append(self.diesel_cars_avail.pop(car_choice - 1))
            renting.menu()
            
        if answer == '3':
            print '\n>>>>>>>>    Hybrid cars available:  <<<<<<<<<<'
            for car in self.hybrid_cars_avail:
                car_details = []
                for attr in car:
                    car_details.append(attr)
                print (self.hybrid_cars_avail.index(car)+1), (" ".join([str(elem) for elem in car_details]))
            car_choice = raw_input('Select car> ')
            car_choice = int(car_choice)
            self.hybrid_cars_rented.append(self.hybrid_cars_avail.pop(car_choice - 1))
            renting.menu()
            
        if answer == '4':
            print '\n>>>>>>>>    Electric cars available:  <<<<<<<<<<'
            for car in self.electric_cars_avail:
                car_details = []
                for attr in car:
                    car_details.append(attr)
                print (self.electric_cars_avail.index(car)+1), (" ".join([str(elem) for elem in car_details]))
            car_choice = raw_input('Select car> ')
            car_choice = int(car_choice)
            self.electric_cars_rented.append(self.electric_cars_avail.pop(car_choice - 1))
            renting.menu()
                
        if answer == '5':
            renting.menu()            
            
    def return_process(self):
        answer = raw_input('Select type> ') 
        if answer == '1':
            print '\n>>>>>>>>    Petrol cars rented:  <<<<<<<<<<'
            for car in self.petrol_cars_rented:
                car_details = []
                for attr in car:
                    car_details.append(attr)
                print (self.petrol_cars_rented.index(car)+1), (" ".join([str(elem) for elem in car_details]))
            car_choice = raw_input('Select car> ')
            car_choice = int(car_choice)
            self.petrol_cars_avail.append(self.petrol_cars_rented.pop(car_choice - 1))
            renting.menu()
                
        if answer == '2':
            print '\n>>>>>>>>    Diesel cars rented:  <<<<<<<<<<'
            for car in self.diesel_cars_rented:
                car_details = []
                for attr in car:
                    car_details.append(attr)
                print (self.diesel_cars_rented.index(car)+1), (" ".join([str(elem) for elem in car_details]))
            car_choice = raw_input('Select car> ')
            car_choice = int(car_choice)
            self.diesel_cars_avail.append(self.diesel_cars_rented.pop(car_choice - 1))
            renting.menu()
                
        if answer == '3':
            print '\n>>>>>>>>    Hybrid cars rented:  <<<<<<<<<<'
            for car in self.hybrid_cars_rented:
                car_details = []
                for attr in car:
                    car_details.append(attr)
                print (self.hybrid_cars_rented.index(car)+1), (" ".join([str(elem) for elem in car_details]))
            car_choice = raw_input('Select car> ')
            car_choice = int(car_choice)
            self.hybrid_cars_avail.append(self.hybrid_cars_rented.pop(car_choice - 1))
            renting.menu()
                
        if answer == '4':
            print '\n>>>>>>>>    Electric cars rented:  <<<<<<<<<<'
            for car in self.electric_cars_avail:
                car_details = []
                for attr in car:
                    car_details.append(attr)
                print (self.electric_cars_avail.index(car)+1), (" ".join([str(elem) for elem in car_details]))
            car_choice = raw_input('Select car> ')
            car_choice = int(car_choice)
            self.electric_cars_rented.append(self.electric_cars_avail.pop(car_choice - 1))
            menu()
                
        if answer == '5':
            renting.menu()
            
def openf():
    fname = open('cars.txt', 'r')
    car_list = fname.readlines()

    for line in car_list:
        line = line.replace(',',' ')
        line = line.strip().split()
        car = Car()
        car.setup(*line)
         
openf()        
renting = Dealership()
renting.menu()





