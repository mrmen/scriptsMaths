__author__ = 'mrmen'


class TemplateExercice:
    def __init__(self):
        """create all needed parts"""
        self.listeEnonce = []
        self.listeSolution = []
        self.nbExercice = 5
        self.nbQuestion = 10
        self.COLONNE=1
        self.package = ["amsmath", "amssymb", "inputenc", "fontenc", "geometry", "xlop", "multicol", "babel", "qrcode"]

    @staticmethod
    def format_exercice(exercice, exercise_type):
        """print an exercise with its question"""
        print("\\begin{" + exercise_type + "}\\ ")
        print("")
        print("\\begin{enumerate}")
        for question in exercice:
            print("\\item " + question)
        print("\\end{enumerate}")
        print("\\end{" + exercise_type + "}")

    def print_enonce(self):
        """print enonce according to listeEnonce"""
        for exercice in self.listeEnonce:
            self.format_exercice(exercice, "exercice")

    def print_solution(self):
        """print solution according to listeSolution"""
        for solution in self.listeSolution:
            self.format_exercice(solution, "solution")

    def print_preamble(self):
        """print preamble according to self.package"""
        print("\\documentclass[12pt,french]{article}")
        for package in self.package:
            line = "\\usepackage"
            if package == "geometry":
                line += "[margin=2cm]"
            elif package == "inputenc":
                line += "[utf8]"
            elif package == "fontenc":
                line += "[T1]"
            line += "{" + package + "}"
            print(line)
        print("\\newtheorem{exercice}{Exercice}")
        print("\\newtheorem{solution}{Solution de l'exercice }")
        print("\\begin{document}")

    @staticmethod
    def print_postamble():
        """print postamble ie only end document"""
        print("\\end{document}")

    def display(self):
        """display the whole exercise according to previous functions"""
        self.print_preamble()
        if self.COLONNE!=0:
            print("\\begin{multicols}{2}")
        # TODO
        self.print_enonce()
        if self.COLONNE!=0:
            print("\\end{multicols}")
        # TODO fix this part
        print("\\newpage")
        print("\\begin{multicols}{2}")
        # TODO
        self.print_solution()
        print("\\end{multicols}")
        self.print_postamble()
