__author__ = 'mrmen'

from TemplateExercice import *
import random


class Mult10(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = 1
        self.max = 10000
        self.generate()

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                first = random.randint(self.min, self.max)
                second = float(random.randint(self.min, self.max))/10**first
                third = random.randint(1,4)
                tempenonce.append("%s \\times %s" % (second, 10**third))
                tempsolution.append("%s \\times %s = %s" % (second, 10**third, second, 10**third))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


if __name__ == "__main__":
    app = Addition()
    app.display()
