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
            for numéro, couleur in enumerate(self.COULEURS[6 : self.nb_couleur],start=6):
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
        result_choix = ""
        for i in range(0,len(self.couleur_utilisateur)):
            if self.couleur_utilisateur[i] == self.choix_couleur[i]:
                result_choix = result_choix + "\U0001F973" + " " #return True
            else:
                result_choix = result_choix + "\U0001F621" + " " #return False
        print(result_choix)
        
 
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


class Mastermind:
    def __init__(self):
        self.menu()
    
    def jeux(self):
        print("\nSois prêt.e!")
        jeux_standard = Règle(6, 6)
        jeux_standard.jouer()

    def reglement(self): 
        print("\n===================================================================================================================================")
        print("|| Le but du Mastermind est de gagner un maximum de manches. Le joueur doit trouver la combinaison secrète pour gagner une manche.||")
        print("===================================================================================================================================")
        self.menu()
        
    def difficulte(self):
        print("\nDifficulté du jeux : ")
        print("1. Facile")
        print("2. Difficile")
        print("3. Personalisé", '\n')
        choix_dif = int(input("Choisir un numèro : "))
        nb_colonnes = 6 #jeu standard
        nb_couleur = 6  #jeu standard
        if choix_dif == 1:
            nb_colonnes = 4
            nb_couleur = 6
        elif choix_dif == 2:
            nb_colonnes = 6
            nb_couleur = 7
        elif choix_dif == 3:
            nb_colonnes = int(input("Choisir le nombre de colonnes (4 à 10): "))
            while nb_colonnes < 4 or nb_colonnes > 10:
                print("le nombre de colonnes doivent être entre 4 et 10!")
                nb_colonnes = int(input("Choisir le nombre de colonnes (4 à 10): "))
            nb_couleur = int(input("Choisir le nombre de couleurs (4 à 12): "))
            while nb_couleur < 4 or nb_couleur > 12:
                print("le nombre de couleurs doivent être entre 4 et 12!")
                nb_couleur = int(input("Choisir le nombre de couleurs (4 à 12): "))
        config = Règle(nb_colonnes,nb_couleur)
        config.jouer()
              
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

Mastermind()

# if __name__ == "__main__":
#     essai = Règle(6, 6)
#     essai.jouer()