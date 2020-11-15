__author__ = 'mrmen'

# pour l'ipad
import clipboard

clip = ""
clipboard.set(clip)

def mrmen_print(string):
	global clip
	print(string)
	clip = clip + "\n" + string
	clipboard.set(clip)


class TemplateExercice:
    def __init__(self):
        """create all needed parts"""
        self.listeEnonce = []
        self.listeSolution = []
        self.nbExercice = 5
        self.nbQuestion = 10
        self.COLONNE=1
        self.package = ["amsmath", "amssymb", "inputenc", "fontenc", "geometry", "xlop", "multicol", "xcolor"]

    @staticmethod
    def format_exercice(exercice, exercise_type):
        """mrmen_print an exercise with its question"""
        mrmen_print("\\begin{" + exercise_type + "}\\ ")
        mrmen_print("")
        mrmen_print("\\begin{enumerate}")
        for question in exercice:
            mrmen_print("\\item " + question)
        mrmen_print("\\end{enumerate}")
        mrmen_print("\\end{" + exercise_type + "}")

    def mrmen_print_enonce(self):
        """mrmen_print enonce according to listeEnonce"""
        for exercice in self.listeEnonce:
            self.format_exercice(exercice, "exercice")

    def mrmen_print_solution(self):
        """mrmen_print solution according to listeSolution"""
        for solution in self.listeSolution:
            self.format_exercice(solution, "solution")

    def mrmen_print_preamble(self):
        """mrmen_print preamble according to self.package"""
        mrmen_print("\\documentclass[12pt,french]{article}")
        for package in self.package:
            line = "\\usepackage"
            if package == "geometry":
                line += "[margin=2cm]"
            elif package == "inputenc":
                line += "[utf8]"
            elif package == "fontenc":
                line += "[T1]"
            line += "{" + package + "}"
            mrmen_print(line)
        mrmen_print("\\newtheorem{exercice}{Exercice}")
        mrmen_print("\\newtheorem{solution}{Solution de l'exercice }")
        mrmen_print("\\begin{document}")

    @staticmethod
    def mrmen_print_postamble():
        """mrmen_print postamble ie only end document"""
        mrmen_print("\\end{document}")

    def display(self):
        """display the whole exercise according to previous functions"""
        self.mrmen_print_preamble()
        if self.COLONNE!=0:
            mrmen_print("\\begin{multicols}{2}")
        # TODO
        self.mrmen_print_enonce()
        if self.COLONNE!=0:
            mrmen_print("\\end{multicols}")
        # TODO fix this part
        mrmen_print("\\newpage")
        mrmen_print("\\begin{multicols}{2}")
        # TODO
        self.mrmen_print_solution()
        mrmen_print("\\end{multicols}")
        self.mrmen_print_postamble()
