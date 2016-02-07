__author__ = 'mrmen'

from TemplateExercice import *
import random


class SimplificationFraction(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = 1
        self.max = 100
        self.generate()

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                num = random.randint(self.min, self.max)
                denom = random.randint(self.min, self.max)
                mult = random.randint(self.min, 25)
                style=random.randint(0,1)
                tempenonce.append(self.format_enonce(num, denom, mult, style))
                tempsolution.append(self.format_solution(num, denom, mult, style))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


    def format_enonce(self, num, denom, mult, style):
        if style:
            string = "\\dfrac{%s}{%s} = \\dfrac{%s}{\\dots}"%(num, denom, num*denom)
        else:
            string = "\\dfrac{%s}{%s} = \\dfrac{\\dots}{%s}"%(num, denom, denom*mult)
        return "$"+string+"$"
            
    def format_solution(self, num, denom, mult, style):
        string = "\\dfrac{%s}{%s} = \\dfrac{%s\\times %s}{%s\\times %s} = \\dfrac{%s}{%s}"%(num, denom, num,mult, denom,mult, num*mult, denom*mult)
        return "$"+string+"$"




if __name__ == "__main__":
    app = SimplificationFraction()
    app.display()
