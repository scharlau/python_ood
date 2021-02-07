# CS1527
# A collection of vehicle classes used to illustrate various aspects of
# OO programming in Python.
# Last edit: 9 January 2021

               
class Car:
    __doc__ = 'Car Class'
    
    """Class attribute to hold list of Cars created."""
    all_cars = []
    
    def __init__(self, ma ='', mo = '', yr = '', **kwargs):
        super().__init__(**kwargs)
        self._make = ma
        self._model = mo
        self._year = yr
        """_odometer_reading should only be 
        accessed/modified via internal methods"""
        self.__odometer_reading = 0
        Car.all_cars.append(self)
    
    @classmethod
    def print_inventory(cls):
        for item in cls.all_cars:
            print(item.get_fullname())
    
    def __str__(self):
        return "Car: " + self.get_fullname()
        
    def __len__(self):
        return self.get_car_age() 
        
    def __eq__(self, other):
        return (self._make == other._make and 
             self._model == other._model)
        
    def get_fullname(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self._year) + ', ' + self._make + \
            ' ' + self._model
        return long_name.title()

    def get_car_age(self, current_year=2017):
        """Return the age of the car in years."""
        return current_year - self._year
        
    def increment_odometer(self,miles):
        """Increment private odometer reading by a distance in miles."""
        self.__odometer_reading += miles      
    
        
class ElectricCar(Car):
    """Represent aspects specific to electric vehicles."""

    def __init__(self, **kwargs):
        """Initialize attributes of the parent class."""
        super().__init__(**kwargs)
        """Initialize attributes specific to an electric car."""
        self._max_range = 300
        self.__battery_level = 100
        
    def __str__(self):
        return "ElectricCar: " + self.get_fullname()

    def report_battery(self):
        """Report private attribute holding battery level."""
        print(self.__battery_level)

    def charge_battery(self):
        """Increase __battery_level as charging."""
        if self.__battery_level < 100:
            self.__battery_level +=1
        else:
            print('Danger - overcharging!')
            
    def get_fullname(self):
        """Return a high voltage descriptive name."""       
        long_name = '** ' + super().get_fullname() + ' **'
        return long_name.title()

# To create instances, try:
# car1 = Car(ma='Audi',mo='Q7',yr=2004)
# ecar1 = ElectricCar(ma='Tesla',mo='Model S',yr=2016)

