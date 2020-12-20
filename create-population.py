'''
Here we can create the class City and the class Fitness
Then we are going to create the initial population
'''

# City class to create and deal with cities
    class City:
    # Initially only has x and y coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # With the Pythagorean theorem, we calculate the distance
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance

    # Clean mode to show the cities output as coordinates
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def lista(self):
        coord = []
        coord = [self.x, self.y]
        return coord

# Fitness Class, in this case we will treat fitness as the inverse of the route distance
class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def routeDistance(self):
        if self.distance == 0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i]
                toCity = None
                if i + 1 < len(self.route):  # I calculate to start and end in the same place
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0]
                pathDistance += fromCity.distance(toCity)
            self.distance = pathDistance
        return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness

## CREATING THE POPULATION: createRoute (individual), initialPopulation (population)
def createRoute(cityList):
    # route = random.sample(cityList, len(cityList))
    teste_rota = random.sample(cityList[1:], len(cityList[1:]))  # Randomize the cities that are not the deposit
    teste_rota.insert(0, cityList[0])  # inserts the deposit at the beginning of the rotation
    teste_rota.insert(len(teste_rota), cityList[0])  # inserts the deposit at the end of the route
    return teste_rota
    # return route
def initialPopulation(popSize, cityList):
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population
