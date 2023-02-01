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


class Règle(Tableau_jeux):
    def __init__(self, nb_colones, nb_couleur) -> None:
        super().__init__()
        self.nb_colones = nb_colones
        self.nb_couleur = nb_couleur
        self.choix_couleur = []
        self.couleur_utilisateur = []
        self.points = 0


    def choisir_couleur(self):
        couleurs = []
        temp= []
        for couleur in self.COULEURS[0 : self.nb_couleur]:
            couleurs.append(couleur)
        if self.nb_colones <= self.nb_couleur:
            temp = r.sample(couleurs, self.nb_colones)
        elif self.nb_colones > self.nb_couleur:
            mult = [] 
            occurence = int(self.nb_colones / self.nb_couleur) 
            if self.nb_colones % self.nb_couleur > 0: # arondir vers le haut
                occurence += 1
            for i in couleurs:
                mult.append(occurence)
            temp = r.sample(couleurs, counts=mult, k=self.nb_colones)
        for couleur in temp:
            self.choix_couleur.append(Couleur(couleur))


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
        choix_utilisateur_temp = str(input(f'Choisissez vos {self.nb_colones} couleurs:'))
        while len(choix_utilisateur_temp) != self.nb_colones:
            choix_utilisateur_temp = str(input(f'Choisissez vos {self.nb_colones} couleurs!!!:'))
        for chiffre in choix_utilisateur_temp:
            choix_utilisateur.append(int(chiffre))
        self.couleur_utilisateur = self.couleur_chiffre(choix_utilisateur)


    def compare(self):
        result_choix = ""
        réponse = ''
        utilisateur = ''
        couleur_trouver = 0
        for i in range(0,len(self.couleur_utilisateur)):
            fini = False 
            utilisateur = self.couleur_utilisateur[i]
            réponse = self.choix_couleur[i]
            if réponse.couleur == utilisateur.couleur:
                result_choix = result_choix + "\U0001F973" + " " 
                couleur_trouver += 1   
                fini = True
            while fini == False:
                for couleur_réponse in self.choix_couleur:
                    if couleur_réponse.couleur == utilisateur.couleur:
                        fini = True
                if fini == True:
                    result_choix += "\U0001F642" + " "
                elif fini == False:
                    result_choix = result_choix + "\U0001F621" + " " 
                    fini = True
        print(result_choix)
        if couleur_trouver == len(self.choix_couleur):
            return True
        else:
            return False
 

    def update_score():
        pass


    def pointage(self, nb_ligne):
        if self.nb_colones >= self.nb_couleur:
            self.points = int((self.nb_colones / self.nb_couleur) * (11 - nb_ligne)) * 7
        elif self.nb_colones < self.nb_couleur:
            self.points = int((self.nb_couleur / self.nb_colones) * (11 - nb_ligne)) * 7
        
        if self.points >= self.classement[0]:
            return True
        else:
            return False
        self.update_score()


    def jouer(self):
        self.choisir_couleur()
        fin = False
        compteur = 0
        réussit = False
        while fin == False and réussit == False:
            self.devine_couleur()
            réussit = self.compare()
            
            if compteur == 9:
                fin = True
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


class Mastermind(Tableau_jeux):
    def __init__(self):
        super().__init__()
        self.menu()
    
    def jeux(self):
        print("\nSois prêt.e!")
        jeux_standard = Règle(6, 6)
        jeux_standard.jouer()

    def reglement(self): 
        print("\n=============================================================================================================================================")
        print("|| Le but du Mastermind est de gagner un maximum de manches. Le joueur doit trouver la combinaison secrète en moins de 10 essais pour gagner.||")
        print("===============================================================================================================================================")
        self.menu()
        
    def difficulte(self):
        sortie = False
        while sortie == False:
            sortie = True
            print("\nDifficulté du jeux : ")
            print("1. Facile")
            print("2. Difficile")
            print("3. Personalisé", '\n')
            choix_dif = int(input("Choisir un numèro : "))
            if choix_dif == 1:
                nb_colonnes = 4
                nb_couleur = 6
            elif choix_dif == 2:
                nb_colonnes = 6
                nb_couleur = 9
            elif choix_dif == 3:
                nb_colonnes = int(input("Choisir le nombre de colonnes (4 à 10): "))
                while nb_colonnes < 4 or nb_colonnes > 10:
                    print("le nombre de colonnes doivent être entre 4 et 10!")
                    nb_colonnes = int(input("Choisir le nombre de colonnes (4 à 10): "))
                nb_couleur = int(input("Choisir le nombre de couleurs (4 à 12): "))
                while nb_couleur < 4 or nb_couleur > 12:
                    print("le nombre de couleurs doivent être entre 4 et 12!")
                    nb_couleur = int(input("Choisir le nombre de couleurs (4 à 12): "))
            else:
                print("Choix inexistent! Essayer à nouveau!\n")
                sortie = False                    
        config = Règle(nb_colonnes,nb_couleur)
        config.jouer()
              

    def afficher_classement(self):
        pass


    def menu(self):
        sortie = False
        while sortie == False:
            print('\n//////////////////   Mastermind Jeux   //////////////////','\n')
            print("1. Jouer le jeux")
            print("2. Règlement")
            print("3. Classement")
            print("4. Sortir",'\n')
            choice = input("Choisir un numèro : ")
            if choice == '1':
                self.difficulte()
            elif choice == '2':
                self.reglement()
            elif choice == '3':
                self.afficher_classement
            elif choice == '4':
                sortie = True
                print("À bientot")
            else:
                print("Choix inexistent! Essayer à nouveau!\n")


if __name__ == "__main__":
   Mastermind()
   #essaie = Règle(12,5)
   #essaie.jouer()