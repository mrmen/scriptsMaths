__author__ = 'mrmen'

from TemplateExercice import *
import random


class Mult01(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = 1
        self.max = 10000
        self.nbExercice = 1
        self.nbQuestion = 30
        self.generate()

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                first = random.randint(1,5)
                secondprime = random.randint(self.min, self.max)
                second = float(secondprime)/10**first
                third = random.randint(-4,-1)
                tempenonce.append("$%s \\times %s$" % (second, 10**third))
                tempsolution.append("$%s \\times %s = $\\vspace*{3cm}" % (second, 10**third))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


if __name__ == "__main__":
    app = Mult01()
    app.display()
