__author__ = 'mrmen'
from TemplateExercice import *
import random


class AdditionDecimaux(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.FACTEUR = [2,3,4,5,6,7,8,9,10,11,12,13]
        self.NUMERATEUR = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        self.DENOMINATEUR = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        self.generate()

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
        numerateur = []
        numerateur.append(self.NUMERATEUR[random.randint(0,len(self.NUMERATEUR)-1)])
        numerateur.append(self.NUMERATEUR[random.randint(0,len(self.NUMERATEUR)-1)])

        denominateur = []
        denominateur.append(self.DENOMINATEUR[random.randint(0,len(self.DENOMINATEUR)-1)])

        facteur = self.FACTEUR[random.randint(0,len(self.FACTEUR)-1)]
        denominateur.append(denominateur[0]*facteur)
        return [numerateur,denominateur]

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
        return "$%s + %s$" % (list[0], list[1])

    def get_solution(self, list):
        numerateur = list[0]

        denominateur = list[1]
        facteur = int(list[1][1] / list[1][0])
        stringOutput = ""
        stringOutput = stringOutput + "\\begin{align*}"
        frac = self.parse_exercise_raw(list)

        stringOutput += frac[0] + "+" + frac[1]

        stringOutput += "\n& = "
        fracTimes = frac[0].replace("}", "{\color{red}\\times " + str(facteur) + "}}")
        stringOutput += fracTimes + "+" + frac[1]
        stringOutput += "\\\\\n & = "

        fracTimes = "\\dfrac{" + str(numerateur[0] * facteur) + "}{{\color{red}" + str(denominateur[1]) + "}}"
        stringOutput += fracTimes + "+" + "\\dfrac{" + str(numerateur[1]) + "}" + "{\color{red}" + str(denominateur[1]) + "}"
        stringOutput += "\\\\\n & = "

        result = "\\dfrac{" + str(numerateur[0] * facteur + numerateur[1]) + "}{" + str(denominateur[1]) + "}"
        stringOutput += result + "\n"
        stringOutput += "\\end{align*}"

        return stringOutput
if __name__ == "__main__":
    app = AdditionDecimaux()
    app.display()
