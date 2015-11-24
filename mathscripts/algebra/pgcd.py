__author__ = 'mrmen'

from TemplateExercice import *
import random


class Addition(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.nbExercice=1
        self.nbQuestion=1
        self.min = 50
        self.max = 9999
        self.generate()
        
    def printGcd(self, first, second):
    	string=""
    	a,b = first, second
    	r=1
    	while (r!=0):
    		string="\\[\\opidiv{%s}{%s}\\]\n"%(a,b)
    		r=a%b
    		q=(a-r)/b
    		string+="\\[%s = %s\\times %s +%s\\]\n"%(a,b,q,r)
    		string+="\\[PGCD(%s,%s) = PGCD(%s,%s)\\]\n"%(a,b,b,r)
                a,b = b,r
    	return string

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                first = random.randint(self.min, self.max)
                second = random.randint(self.min, self.max)
                third = random.randint(self.min, self.max)
                tempenonce.append("Calculer le PGCD de %s  et %s" % (first, second))
                tempsolution.append(self.printGcd(first, second))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


if __name__ == "__main__":
    app = Addition()
    app.display()
