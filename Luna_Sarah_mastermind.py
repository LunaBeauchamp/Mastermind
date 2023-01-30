import random as r
#Ici on peut mettre des commentaires sur des choses à changer ou à améliorer
    #je mettrais ton menu dans une boucle parce que sinon on sort imédiatement après avoir jouer.
    #je mettreai difficlté dans jouer comme ça ça nous fait un sous-menu.
    #Il faut rajouter l'option classement dans le menu.
    

#Couleurs :
#1 = "vert", 2 = "bleu", 3 = "mauve", 4 = "rouge", 5 = "orange", 6 = "jaune", 
#7= "rose", 8 = "truquoise", 9 = "blanc", 10 = "noir", 11 = "gris", 12 = "maron"


class Mastermind:
    def __init__(self):
        self.menu()
    
    def jeux(self):
        print("\nSois prêt.e!")

    def reglement(self): 
        print("\nLe but du Mastermind est de gagner un maximum de manches. Le joueur doit trouver la combinaison secrète pour gagner une manche.")

    def difficulte(self):
        print("\nDifficulté du jeux : ")
        print("1. Facile")
        print("2. Difficile")
        print("3. Personalisé", '\n')
        print("Choisir un numèro : ")
        exit()
        
    def sortir(self):
        # print("\nÀ bientôt!")
        exit()
        
    def menu(self):
        print('\n//////////////////   Mastermind Jeux   //////////////////','\n')
        print("1. Jouer le jeux")
        print("2. Règlement")
        print("3. Difficulté")
        print("4. Sortir",'\n')
        choice = input("Choisir un numèro : ")
        if choice == '1':
            self.jeux()
        elif choice == '2':
            self.reglement()
        elif choice == '3':
            self.difficulte()
        elif choice == '4':
            self.sortir()
        else:
            print("Choix inexistent! Essayer à nouveau!\n")
            self.menu()

game = Mastermind()


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


    def couleur_chiffre(self, liste):
        temp = []
        for nombre in liste:
            temp.append(Couleur(self.COULEURS[nombre -1]))
        return temp
    

    def devine_couleur(self):
        temp = ''
        choix_utilisateur = []
        if self.nb_couleur <= 6:
            for numéro, couleur in enumerate(self.COULEURS[0 : self.nb_couleur]):
                temp += f'{numéro + 1} : {couleur}\t'
            print(temp)
        else:
            for numéro, couleur in enumerate(self.COULEURS[0 : 6]):
                temp += f'{numéro + 1} : {couleur}\t'
            print(temp)
            temp = ''
            for numéro, couleur in enumerate(self.COULEURS[6 : self.nb_couleur]):
                temp += f'{numéro + 1} : {couleur}\t'
            print(temp)
        choix_utilisateur_temp = str(input(f'Choisissez vos {self.nb_couleur} couleurs:'))
        for chiffre in choix_utilisateur_temp:
            choix_utilisateur.append(int(chiffre))
        self.couleur_utilisateur = self.couleur_chiffre(choix_utilisateur)


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
    essai = Règle(6, 6)
    essai.jouer()