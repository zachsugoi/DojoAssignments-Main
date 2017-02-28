class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()
    def display_all(self):
        print 'Price:', self.price, '\n', 'Speed:', self.speed, '\n', 'Fuel:',\
                self.fuel, '\n' 'Mileage:', self.mileage, '\n', 'Tax:', self.tax
#roll out the cars
car1 = Car(2000, '50mph', 'Pretty Full', '60mpg')
car2 = Car(6000, '25mph', 'Full', '120mpg')
car3 = Car(4500, '16mph', 'To the Brim', '607mpg')
car4 = Car(15000, '1mph', 'Half Full', '.5mpg')
car5 = Car(600, '750mph', 'Overflowing', 'Infinite mpg')
car6 = Car(5, '5mph', '5 Notches Left', '5mpg')
