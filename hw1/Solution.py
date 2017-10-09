from Marriage import Marriage
import itertools

class Solution:

    def __init__(self, number, women, men):
        """
        The constructor exists only to initialize variables. You do not need to change it.
        :param number: The number of members
        :param men: The preference list of men, as a dictionary.
        :param women: The preference list of the women, as a dictionary.
        """
        self.num = number
        self.men = men
        self.women = women
        self.count = 0
        self.stable_matchings = []

    def output_stable_matchings(self):
        """
        This method both computes and returns the stable matchings
        :return: the list of stable matchings
        """

        for perm in itertools.permutations(self.men, self.num):
            marriages = [None] * self.num
            for i in range(0, self.num):
                marriages[i] = Marriage(perm[i], i+1)

            if self.is_stable(marriages):
                self.count = self.count + 1
                self.stable_matchings.append(marriages)

        return self.stable_matchings
    
    def is_stable(self, marriages):
        for i in range(len(marriages)):
            man1 = marriages[i].man()
            woman1 = marriages[i].woman()

            for j in range(1, len(marriages)):
                man2 = marriages[j].man()
                woman2 = marriages[j].woman()
                
                if (self.men[man1].index(woman2) <  self.men[man1].index(woman1)) and (self.women[woman2].index(man1) < self.women[woman2].index(man2)):
                    return False
                elif (self.women[woman1].index(man2) < self.women[woman1].index(man1)) and (self.men[man2].index(woman1) < self.men[man2].index(woman2)):
                    return False
        return True