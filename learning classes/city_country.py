class city_name():

    def __init__(self,city,country,population):
        self.country = country
        self.city = city
        self.population =  str(population)

    def combine(self):
        address = (self.city + ","+self.country +","+"population-"+self.population)
        print(address.title())

my_city = city_name("delhi","india",5000000)
my_city.combine()
