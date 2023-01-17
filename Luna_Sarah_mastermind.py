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
        self.choisir_couleur()


    def choisir_couleur(self):
        temp = []
        for nombre in range(self.nb_couleur):
            temp.append(nombre)
        r.shuffle(temp)
        for nombre in temp:
            self.choix_couleur.append(Couleur((self.COULEURS[nombre])))
    

    def jouer(self):
        fini = False
        compteur = 0
        réussit = False
        while fini == False:
            
            
            if compteur == 9:
                fini = True

        pass


    def pointage(self):
        pass


class Couleur:
    def __init__(self, couleur) -> None:
        self.couleur = couleur


    def __str__(self) -> str:
        return print(f'{self.couleur}')


if __name__ == "__main__":
    essai = Règle(6, 6)