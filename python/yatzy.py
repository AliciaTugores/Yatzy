class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)
    
    @staticmethod
    def chance(*dice):
        total = 0
        for number in dice:
            total += number
        return total

    @staticmethod
    def yatzy(*dice):
        for number in dice:
            if dice.count(number) == 5:
                return 50
        return 0 

    @staticmethod
    def ones(*dice):
        uno = 1
        return dice.count(uno) * uno

    @staticmethod
    def twos(*dice):
        dos = 2
        return dice.count(dos) * dos
    
    @staticmethod
    def threes(*dice):
        tres = 3
        return dice.count(tres) * tres
    
    def fours(self):
        cuatro = 4
        return self.dice.count(cuatro) * cuatro
    
    def fives(self):
        cinco = 5
        return self.dice.count(cinco) * cinco

    def sixes(self):
        seis = 6
        return self.dice.count(seis) * seis
    
    @staticmethod
    def score_pair(*dice):
        for item in range(6, 0, -1): #range('número del cual empezamos', 'número al cual queremos llegar(último+1)', 'operación a realizar en i')
            if dice.count(item) >= 2:  #buscamos el item que se repita 2 o más veces y ese item lo *2
                return item * 2 
        return 0

    @staticmethod
    def two_pair(*dice):
        contador = 0
        score = 0
        dos = 2
        for item in range(6, 0, -1):
            if dice.count(item) >= dos:
                contador += 1
                score += item * dos
            if contador == dos:
                return score
        return 0

    @staticmethod
    def three_of_a_kind(*dice):
        tres = 3
        for item in range(6, 0, -1):
            if dice.count(item) >= tres:
                return item * tres
        return 0
    
    @staticmethod
    def four_of_a_kind(*dice):
        cuatro = 4
        for item in range(6, 0, -1):
            if dice.count(item) >= cuatro:
                return item * cuatro
        return 0

    @staticmethod
    def smallStraight(*dice):
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 15
        return 0  

    @staticmethod
    def largeStraight(*dice):
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 20
        return 0
    
    @staticmethod
    def only_pair(*dice):
        dos = 2
        for item in range(6, 0, -1):
            if dice.count(item) == dos:
                return item * dos
        return 0

    @staticmethod
    def fullHouse(*dice):
        if Yatzy.only_pair(*dice) and Yatzy.three_of_a_kind(*dice):
            return Yatzy.only_pair(*dice) + Yatzy.three_of_a_kind(*dice)
        else:
            return 0