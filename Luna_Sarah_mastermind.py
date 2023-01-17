import random as r
#!!!!!!!!!!!!!!!!!!!!!!!!   important   !!!!!!!!!!!!!!!!!!!!!!!
#j'ai demandé au prof pour les couleur et il veut qu'on utiliseau minimum de lettre

#Couleurs :
#1 = "vert", 2 = "bleu", 3 = "mauve", 4 = "rouge", 5 = "orange", 6 = "jaune", 
#7= "rose", 8 = "truquoise", 9 = "blanc", 10 = "noir", 11 = "gris", 12 = "maron"

class Tableau_jeux:
    def __init__(self) -> None:
        self.classement : list[int]= []
        self.lecture_classement()
        self.COULEURS = ["vert", "bleu", "mauve", "rouge", "orange", "jaune", 
                        "rose", "truquoise", "blanc", "noir", "gris", "maron"]


    def lecture_classement(self):
        with open('score.txt', "r", encoding="UTF-8") as f:
            donnees = f.readlines()        
            for ligne in donnees:
                ligne = int(ligne.strip())
                self.classement.append(ligne)
            

class Affichage(Tableau_jeux):
    def __init__(self) -> None:
        super().__init__()


class Règle(Tableau_jeux):
    def __init__(self, nb_colones, nb_couleur) -> None:
        super().__init__()
        self.nb_colones = nb_colones
        self.nb_couleur = nb_couleur
        self.choix_couleur = []
        self.couleur_utilisateur = []
        self.points = ''


    def choisir_couleur(self):
        temp = []
        for nombre in range(self.nb_couleur):
            temp.append(nombre)
        r.shuffle(temp)
        for nombre in temp:
            self.choix_couleur.append(Couleur((self.COULEURS[nombre])))
    

    def devine_couleur(self):
        #demande à l'utilisateur les couleur qu'il veut essayer
        #le met dans self.couleur utilisateur avec un append 
        pass


    def compare(self):
        #comparer self.couleur_utilisateur : list[object] et self.choix_couleur(object) : list[object]
        #enumerate une liste
        #1. si même couleur et même place if 
        #2. si la place est mauvaise en regardant la couleur
        #print nb bon et nb mauvaise place
        #return True si c'est réussi et False si c'est mauvais
        pass


    def pointage(self, nb_ligne):
        # return True si c'est un nouveau meillleur score
        pass


    def jouer(self):
        self.choisir_couleur()
        fini = False
        compteur = 0
        réussit = False
        while fini == False:
            self.devine_couleur()
            réussit = self.compare()
            pass
            if compteur == 9:
                fini = True
            compteur += 1
        if réussit == False:
            print("Vous n'avex pas réussit. Meilleur chance la prochaine fois.")
        elif réussit == True:
            meilleur = self.pointage(compteur)
            print(f"Bravo!!! Vous avez gagné!!")
            if meilleur == True:
                print(f"C'est un nouveau record!!")
            print(f"vous avez eu {self.points} points.")


class Couleur:
    def __init__(self, couleur) -> None:
        self.couleur : str = couleur

    def __str__(self) -> str:
        return print(f'{self.couleur}')





if __name__ == "__main__":
