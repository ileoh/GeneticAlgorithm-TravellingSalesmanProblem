'''

Here we can create the class City and the class Fitness
Then we are going to create the initial population
'''

# Classe City para criar e lidar com as cidades
    class City:
    # Inicialmente possui apenas as coordenadas x e y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Com o teorema Pythagorean, calculamos a distancia
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance

    # Modo limpo mostrar a saída das cidades como coordendas
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def lista(self):
        coord = []
        coord = [self.x, self.y]
        return coord

# Classe Fitness, no caso vamos tratar o fitness como o inverso da distancia da rota
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
                if i + 1 < len(self.route):  # Calculo para comer e terminar no mesmo local
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

## CRIAÇÃO DA POPULAÇÃO: createRoute(individuo), initialPopulation(populacao)
def createRoute(cityList):
    # route = random.sample(cityList, len(cityList))
    teste_rota = random.sample(cityList[1:], len(cityList[1:]))  # Aleatoriza as cidades q nao o deposito
    teste_rota.insert(0, cityList[0])  # insere o deposito no inicio da rota
    teste_rota.insert(len(teste_rota), cityList[0])  # insere o deposito no fim da rota
    return teste_rota
    # return route
def initialPopulation(popSize, cityList):
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population
