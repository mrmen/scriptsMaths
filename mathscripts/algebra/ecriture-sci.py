#!/usr/bin/env python
#
#
#    Thomas "Mr Men" Etcheverria
#    <tetcheve (at) gmail .com>
#
#    Created on : 08-02-2019 12:19:48
#    Time-stamp: <08-02-2019 16:04:35>
#
#    File name : c:/Users/Administrateur/Documents/GitHub/scriptsMaths/mathscripts/algebra/ecriture-sci.py
#    Description :
#
__author__ = 'mrmen'
from TemplateExercice import *
import random


class EcritureSci(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.NOMBRE = 2
        self.generate()

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                raw = self.generate_exercise()
                tempenonce.append(self.parse_exercise_raw(raw))
                tempsolution.append(self.get_solution(raw))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)

            
    def generate_exercise(self):
        """Generate a list of value in order to create rationals"""
        def myrand():
            mini = 1
            maxi = 5
            return random.randint(mini, maxi)
        numerateurs = [myrand()*myrand() for _ in range(self.NOMBRE) ]
        denominateurs = [myrand()*myrand() for _ in range(self.NOMBRE) ]
        puissances_num = [random.randint(-5,5) for _ in range(self.NOMBRE)]
        puissances_denom = [random.randint(-5,5) for _ in range(self.NOMBRE)]
        return [[numerateurs,puissances_num], [denominateurs, puissances_denom]]
        
    def parse_exercise_raw(self, liste):
        """Parse output of generate_exercise and give a LaTeX output"""
        num = ""
        denom = ""
        for index in range(self.NOMBRE):
            num += "%s \\times 10^{%s}."%(liste[0][0][index], liste[0][1][index])
            denom += "%s \\times 10^{%s}."%(liste[1][0][index], liste[1][1][index])
        num = num[:-1]
        num = num.replace(".","\\times ")
        denom = denom[:-1]
        denom = denom.replace(".","\\times ")
        return "\\dfrac{%s}{%s}"%(num, denom)
    
    def get_solution(self, liste):
        num = ""
        denom = ""
        for index in range(self.NOMBRE):
            num += "%s * 10**{%s}."%(liste[0][0][index], liste[0][1][index])
            denom += "%s * 10**{%s}."%(liste[1][0][index], liste[1][1][index])
        num = num[:-1]
        num = num.replace(".","*").replace("{","(").replace("}",")")
        denom = denom[:-1]
        denom = denom.replace(".","*").replace("{","(").replace("}",")")
        n = eval(num+"/("+denom+")")
        print(n)
        taille = int(len(str(n).replace(".","")))
        print(taille)
        return "{:.{}e}".format(n, taille-1)


if __name__ == "__main__":
    app = EcritureSci()
    app.display()
