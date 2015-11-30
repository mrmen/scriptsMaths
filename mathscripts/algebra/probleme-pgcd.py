__author__ = 'mrmen'

from TemplateExercice import *
import random
import math

class ProblemePGCD(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.nbExercice=5
        self.nbQuestion=1
        self.min = 100
        self.max = 600
        self.exType=["tartelette salee", "tartelette sucree", "dragee", "pains", "bouquets"]
        self.tarteletteSalee = ["tranches de chorizo", "tranches de fromage de chevre", "olives", "tomates", "tranches de bacon"]
        self.pains = ["tranches de chorizo", "tranches de fromage de chevre", "olives", "tomates", "tranches de bacon"]
        self.tarteletteSucree = ["carres de chocolat", "amandes", "speculos", "fraises", "cerises", "framboises", "raisins"]
        self.dragee = ["vanille", "fraise", "chocolat", "pistache", "rose", "violette", "menthe", "banane", "citron"]
        self.fleurs = ["lilas", "jasmin", "coquelicot", "tournesol", "tulipes", "roses", "margueritte", "pivoine"]
        self.ingredients = [self.tarteletteSalee, self.tarteletteSucree, self.dragee, self.pains, self.fleurs]
        self.generate()
        
    def printGcd(self, first, second):
    	string=""
    	a,b = first, second
    	r=1
    	while (r!=0):
            string+=" %s %s\n"%(a,b)
            string+="\\[\\opidiv{%s}{%s}\\]\n"%(a,b)
            r=a%b
            q=(a-r)/b
            string+="\\[%s = %s\\times %s +%s\\]\n"%(a,b,q,r)
            string+="\\[PGCD(%s,%s) = PGCD(%s,%s)\\]\n"%(a,b,b,r)
            a,b = b,r
    	return string

    def createSolution(self, exType, first, second, ingredient1, ingredient2):
        string = "On cherche le maximum de %s identiques que l'on peut faire en utilisant %s %s et %s %s."%(exType, first, second, ingredient1, ingredient2)
        string += "Cela revient a rechercher le PGCD de %s et %s\n\n"%(first, second)
        string += self.printGcd(first,second)
        pgcd = math.gcd(first,second)
        string += "On en deduit qu'il sera possible de faire %s %s. Chaque element sera constitue de %s %s et de %s %s."%(pgcd, exType, int(first/pgcd), ingredient1, int(second/pgcd), ingredient2)
        return string
        
    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                first = random.randint(self.min, self.max)
                second = random.randint(self.min, self.max)
                index = random.randint(0,len(self.exType)-1)
                exType = self.exType[index]
                ingredient1 = self.ingredients[index][random.randint(0,len(self.ingredients[index])-1)]
                ingredient2 = self.ingredients[index][random.randint(0,len(self.ingredients[index])-1)]                                     
                tempenonce.append("Quel est le maximum de %s identiques constitues equitablement avec %s %s et %s %s. Quelle sera leur composition ?" % (exType, first, second, ingredient1, ingredient2))
                tempsolution.append(self.createSolution(exType, first, second, ingredient1, ingredient2))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


if __name__ == "__main__":
    app = ProblemePGCD()
    app.display()
