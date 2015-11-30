# __author__ = 'mrmen'

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
        self.exType=["tartelettes salees", "tartelettes sucrees", "sachet de dragees", "petits pains", "bouquets"]
        self.tarteletteSalee = ["tranches de chorizo", "tranches de fromage de chevre", "olives", "tomates", "tranches de bacon"]
        self.pains = ["tranches de chorizo", "tranches de fromage de chevre", "olives", "tomates", "tranches de bacon"]
        self.tarteletteSucree = ["carres de chocolat", "amandes", "speculos", "fraises", "cerises", "framboises", "raisins"]
        self.dragee = ["vanille", "fraise", "chocolat", "pistache", "rose", "violette", "menthe", "banane", "citron"]
        self.fleurs = ["lilas", "coquelicots", "tournesols", "tulipes", "roses", "marguerittes", "pivoines"]
        self.ingredients = [self.tarteletteSalee, self.tarteletteSucree, self.dragee, self.pains, self.fleurs]
        self.generate()

    def pgcdInt(self, first, second):
        a,b = max(first, second),min(first, second)
        while (b!=0):
            r=a%b
            a,b = b,r
        return a

    def printGcd(self, first, second):
    	string=""
    	a,b = first, second
    	r=1
    	while (r!=0):
            string+=" %s %s\n"%(a,b)
            string+="\\[\\opidiv{%s}{%s}\\]\n"%(a,b)
            r=a%b
            q=int((a-r)/b)
            string+="\\[%s = %s\\times %s +%s\\]\n"%(a,b,q,r)
            string+="\\[PGCD(%s,%s) = PGCD(%s,%s)\\]\n"%(a,b,b,r)
            a,b = b,r
    	return string

    def createSolution(self, exType, first, second, ingredient1, ingredient2):
        string = "On cherche le maximum de %s identiques que l'on peut faire en utilisant %s %s et %s %s."%(exType, first,ingredient1, second, ingredient2)
        string += "Cela revient a rechercher le PGCD de %s et %s\n\n"%(first, second)
        string += self.printGcd(first,second)
        pgcd = self.pgcdInt(first,second)
        string += "On en deduit qu'il sera possible de faire %s %s. Chaque element sera constitue de %s %s et de %s %s."%(pgcd, exType, int(first/pgcd), ingredient1, int(second/pgcd), ingredient2)
        return string
        
    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                first = random.randint(self.min, self.max)
                second = random.randint(12, 60)*first
                index = random.randint(0,len(self.exType)-1)
                exType = self.exType[index]
                templist=list(self.ingredients)
                ingredient1 = templist[index].pop(random.randint(0,len(templist[index])-1))
                ingredient2 = templist[index].pop(random.randint(0,len(templist[index])-1))                                 
                tempenonce.append("Combien de %s identiques constitues equitablement avec %s %s et %s %s peut-on faire au maximum ?. Quelle sera leur composition ?" % (exType, first, ingredient1, second, ingredient2))
                tempsolution.append(self.createSolution(exType, first, second, ingredient1, ingredient2))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


if __name__ == "__main__":
    app = ProblemePGCD()
    app.display()
