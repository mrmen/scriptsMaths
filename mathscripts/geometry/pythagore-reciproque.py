__author__ = 'mrmen'

import random

from TemplateExercice import *

class Pythagore(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = 10
        self.max = 100
        self.nbQuestion=25
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
                if (len(value)==4):
                    rectangle = False
                    value.pop(3)
                else:
                    rectangle = True
                tempenonce.append(self.create_enonce(name, value))
                tempsolution.append(self.create_solution(rectangle))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)

    def create_name(self):
        alphabet = list(self.alphabet)
        name = []
        for _ in range(3):
            index = random.randint(0, len(alphabet) - 1)
            name.append(alphabet.pop(index))
        return name

    def create_enonce(self, name, value):
        name_temp = list(name)
        string_output = ""
        string_output += "Soit un triangle $%s%s%s$ tel que :\n" % (name[0], name[1], name[2])
        main_sommet = name_temp.pop(random.randint(0,2))
        hyp = name_temp[0] + name_temp[1]
        c1 = main_sommet + name_temp.pop()
        c2 = main_sommet + name_temp.pop()
        string_output += "\[%s = %s~cm,~%s = %s~cm\ et\ %s = %s~cm\\]" % (c1, value[0], hyp, value[2], c2, value[1])
        string_output += "Ce triangle est-il rectangle ?"
        return string_output


    def create_solution(self, rectangle):
        if (rectangle==False):
            return "Non"
        else:
            return "Oui"

    def generate_exercise_raw(self):
        u, v = 0.0, 0.0
        while (u==0.0) or (v==0.0) or (u==v):
            u = random.randint(1, 10) / 5.0
            v = random.randint(1, 10) / 5.0
            v, u = min(u, v), max(u, v)
        if random.randint(0,1):
            return [u ** 2 - v ** 2, 2 * u * v, u ** 2 + v ** 2]
        else:
            to_add = [0.1*random.randint(-1,1),0.1*random.randint(-1,1),0.1*random.randint(-1,1)]
            return [u ** 2 - v ** 2 + to_add[0], 2 * u * v + to_add[1], u ** 2 + v ** 2 + to_add[2],1]

if __name__ == "__main__":
    app = Pythagore()
    app.display()
