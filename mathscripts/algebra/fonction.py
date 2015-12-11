#__author__ = 'mrmen'

from TemplateExercice import *
import random


class Fonction(TemplateExercice):
    def __init__(self):
        TemplateExercice.__init__(self)
        self.min = -10
        self.max = 10
        self.generate()

    def create_solution(self, a,b,x, image):
        sgnb = b[0]
        absb = int(b[1])
        if (sgnb=="+"):
            opb = "-"+b[1]
        else:
            opb = "+"+b[1]
        string = ""
        string += "\\begin{align*}"
        string += "%s x %s = %s"%(a,b,image)
        string += "& \\Longleftrightarrow %s x %s %s = %s %s \\\\"%(a,b,opb,image,opb)
        string += "& \\Longleftrightarrow %s x =  %s \\\\"%(a,eval(str(image)+"+("+str(opb)+")"))
        string += "& \\Longleftrightarrow \\dfrac{%s x}{%s} =  \\dfrac{%s}{%s} \\\\"%(a,a,eval(str(image)+"+("+str(opb)+")"),a)
        string += "& \\Longleftrightarrow x =  %s"%(x)
        string += "\\end{align*}"
        string += "\\[\\mathcal{S} = \\left\\{"+str(x)+"\\right\\}\\]"
        string += "Donc %s a un antecedent par f : %s"%(image,x)
        return string
        
        
    def generate(self):
        """generate enonce and solution according to self.nbQuestion and self.nbExercice from parent class"""
        for exercice in range(self.nbExercice):
            tempenonce = []
            tempsolution = []
            for question in range(self.nbQuestion):
                a, b = 0,0
                while (a==0):
                    a = random.randint(self.min, self.max)
                while (b==0):
                    b = random.randint(self.min, self.max)
                x = random.randint(self.min, self.max)
                image = a * x + b
                if b>=0:
                    b = "+"+str(b)
                tempenonce.append("Ant\\'ec\\'edent de $%s$ par $f : x \\mapsto %s x %s$"%(image, a, b))
                tempsolution.append(self.create_solution(a,str(b),x, image))
            self.listeEnonce.append(tempenonce)
            self.listeSolution.append(tempsolution)


if __name__ == "__main__":
    app = Fonction()
    app.display()
