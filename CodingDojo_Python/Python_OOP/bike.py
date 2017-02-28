class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print 'Price:', self.price
        print 'Max speed:', self.max_speed
        print 'Total miles:', self.miles
    def ride(self):
        print 'Riding'
        self.miles += 10
    def reverse(self):
        print 'Reversing'
        if self.miles - 5 < 0:
            self.miles = 0
        else:
            self.miles -= 5
bike1 = Bike(500, '35mph')
bike2 = Bike(400, '50mph')
bike3 = Bike(10000, '700mph')
#Time to ride!
    #bike1
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
    #bike2
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
    #bike3
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
