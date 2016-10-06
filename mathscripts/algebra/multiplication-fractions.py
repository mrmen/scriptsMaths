__author__ = 'mrmen'
from TemplateExercice import *
import random
import math

class MultiplicationFraction(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.FACTEUR = [2,3,4,5,6,7,8,9,10,11,12,13]
        self.NUMERATEUR = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        self.DENOMINATEUR = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        self.generate()

    def gcd(self,a,b):
        while a%b != 0 : 
            a, b = b, a%b 
        return b        
        
    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                raw = self.generate_exercise()
                tempenonce.append(self.format_list(self.parse_exercise_raw(raw)))
                tempsolution.append(self.get_solution(raw))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)

    def generate_exercise(self):
        """Generate a list of value in order to create rationals"""
        return [[random.randint(1,15) for _ in range(2)] for _ in range(2)]
    
    def parse_exercise_raw(self, list):
        """Parse output of generate_exercise and give a LaTeX output"""
        numerateur = list[0]
        denominateur = list[1]
        #
        frac = []
        frac.append("\\dfrac{"+str(numerateur[0])+"}"+"{"+str(denominateur[0])+"}")
        frac.append("\\dfrac{"+str(numerateur[1])+"}"+"{"+str(denominateur[1])+"}")
        return frac

    def format_list(self, list):
        return "$%s \\times %s$" % (list[0], list[1])

    def get_solution(self, list):
        numerateur = list[0]

        denominateur = list[1]
        stringOutput = ""
        stringOutput = stringOutput + "\\begin{align*}"
        frac = self.parse_exercise_raw(list)

        stringOutput += frac[0] + "\\times" + frac[1]

        stringOutput += "\n& = "
        stringOutput += "\\dfrac{%s \\times %s}{%s \\times %s}"%(list[0][0], list[1][0], list[0][1], list[1][1])
        stringOutput += "\n& = "
        num,denom = list[0][0] * list[1][0], list[0][1] * list[1][1]
        commun = gcd(num, denom)
        num,denom = int(num/commun), int(denom/commun)
        stringOutput += "\\dfrac{%s \\times %s}{%s\\times %s}"%(num,commun,denom,commun)
        stringOutput += "\n& = "
        stringOutput += "\\dfrac{%s}{%s}"%(num,denom)
        stringOutput += "\\end{align*}"

        return stringOutput
if __name__ == "__main__":
    app = MultiplicationFraction()
    app.display()
