__author__ = 'mrmen'

from TemplateExercice import *
import random


class SimplificationRelatifs(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = -4
        self.max = 4
        self.operateurs=["+","-","*"]
        self.generate()

    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        iteration = 0
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            iteration += 2
            for question in range(self.nbQuestion):
            		listeValeursOperateurs = []
            		for _ in range(iteration):
            			element = 0
            			while (element==0):
	            			element = random.randint(self.min, self.max)
	            		if element<0:
	            			element = "("+ str(element)+")"
	            		else:
	            			element = str(element)
            			listeValeursOperateurs.append(element)
            			listeValeursOperateurs.append(random.choice(self.operateurs))
            		listeValeursOperateurs = listeValeursOperateurs[:-1]
            		tempenonce.append(self.format_enonce(listeValeursOperateurs))
            		tempsolution.append(self.format_solution(listeValeursOperateurs))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


    def format_enonce(self, liste):
        string = " ".join(liste)
        string = string.replace("*","\\times")
        return "$"+string+"$"
            
    def format_solution(self, liste):
        raw = " ".join(liste)
        string = raw.replace("*","\\times") + " = "
        calc = eval(raw)
        return "$"+string+str(calc)+"$"




if __name__ == "__main__":
    app = SimplificationRelatifs()
    app.display()
