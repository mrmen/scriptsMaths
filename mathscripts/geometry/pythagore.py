__author__ = 'mrmen'

import random

from TemplateExercice import *

class Pythagore(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = 10
        self.max = 100
        self.value_added = [0, 1]
        self.alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        self.generate()

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                value = self.generate_exercise_raw()
                name = self.create_name()
                rect = random.randint(0, 2)
                rectangle = random.randint(0, 1)
                tempenonce.append(self.create_enonce(name, value, rect, rectangle))
                tempsolution.append(self.create_solution(name, value, rect, rectangle))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)

    def create_name(self):
        alphabet = list(self.alphabet)
        name = []
        for _ in range(3):
            index = random.randint(0, len(alphabet) - 1)
            name.append(alphabet.pop(index))
        return name

    def create_enonce(self, name, value, rect, rectangle):
        name_temp = list(name)
        string_output = ""
        string_output += "Soit un triangle $%s%s%s$ rectangle en $%s$ tel que :" % (name[0], name[1], name[2], name[rect])
        main_sommet = name_temp.pop(rect)
        hyp = name_temp[0] + name_temp[1]
        c1 = main_sommet + name_temp.pop()
        c2 = main_sommet + name_temp.pop()
        # if 1 hyp unknown
        if rectangle:
            string_output += "\\[%s = %s~cm\ et\ %s = %scm\\]" % (c1, value[0], c2, value[1])
            string_output += "Quelle est la longueur de $%s$ ?" % hyp
        # if 0 hyp known
        else:
            string_output += "\\[%s = %s~cm\ et\ %s = %scm\\]" % (hyp, value[2], c2, value[1])
            string_output += "Quelle est la longueur de $%s$ ?" % c1
        return string_output


    def create_solution(self, name, value, rect, rectangle):
        name_temp = list(name)
        string_output = ""
        main_sommet = name_temp.pop(rect)
        hyp = name_temp[0] + name_temp[1]
        # noinspection PyUnusedLocal
        c1 = main_sommet + name_temp.pop()
        c2 = main_sommet + name_temp.pop()
        # if 1 hyp unknown
        if rectangle:
            string_output += "$%s = %s$ cm" % (hyp, value[2])
        # if 0 hyp known
        else:
            string_output += "$%s = %s$ cm" % (c2, value[0])
        return string_output

    def generate_exercise_raw(self):
        u, v = 0.0, 0.0
        while (u==0.0) or (v==0.0) or (u==v):
            u = random.randint(1, 10) / 2.0
            v = random.randint(1, 10) / 2.0
            v, u = min(u, v), max(u, v)
        return [u ** 2 - v ** 2, 2 * u * v, u ** 2 + v ** 2]


if __name__ == "__main__":
    app = Pythagore()
    app.display()
