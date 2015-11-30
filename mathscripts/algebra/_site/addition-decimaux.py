__author__ = 'mrmen'

from TemplateExercice import *
import random


class AdditionDecimaux(TemplateExercice):
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
                exp1 = random.randint(-3,-1)
                second = random.randint(self.min, self.max)
                exp2 = random.randint(-2,-1)

                tempenonce.append("%s + %s " % (first*10**exp1, second*10**exp2))
                tempsolution.append("\\opadd{%s}{%s}" % (first*10**exp1, second*10**exp2))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


if __name__ == "__main__":
    app = AdditionDecimaux()
    app.display()