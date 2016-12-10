__author__ = 'mrmen'

from TemplateExercice import *
import random


class Addition(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = 10
        self.max = 500
        self.generate()

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                first = random.randint(self.min, self.max)
                second = random.randint(self.min, self.max)
                tempenonce.append("%s + %s " % (first, second))
                tempsolution.append("\opadd{%s}{%s}"%(first,second))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


if __name__ == "__main__":
    app = Addition()
    app.display()
