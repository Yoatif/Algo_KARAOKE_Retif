class Player :
    def __init__(self,pseudo,score,):
        self.pseudo = pseudo
        self.score = score
        

    def getPseudo(self):
        return self.pseudo
    
    def getScore(self):
        return self.score
    def afficheScore(self,index):
        return self.getScore[index]
    def moyScore(self):
        moyenne=0
        for index, valeur in self.getScore():
            moyenne=moyenne+valeur
        moyenne=moyenne/5
        return moyenne
    def getMeilleurScore(self):
        meilleurScore=0
        numeroChanson=0
        for index, valeur in self.getScore():
            if valeur>scoreMax:
                scoreMax=valeur
                numeroChanson=index
        print("le meilleur score est: ",meilleurScore, " sur la chanson: ", numeroChanson)
    
    def getPireScore(self):
        pireScore = 0
        numeroChanson = 0
        for index, valeur in self.getScore():
            if valeur < scoreMin:
                scoreMin = valeur
                numeroChanson = index
        print ("le pire score est", pireScore," sur la chanson n°",numeroChanson)
    
    def setScore(self,index,score):
        self.getScore()[index] = score
        print("sur la chanson",index,"le score est maintenant de :", score)

class Karaoke:
    def __init__(self,playerList,songList):
        self.playerList = playerList
        self.songList = songList
    
    def getplayers(self):
        return self.playerList
    
    def getSongs(self):
        return self.songList
    
    def getMeilleureScore(self,chanson):
        valeur=0
        plusGrandeValeur=0
        for i in range (len(self.getplayers())):
            valeur=self.getplayers()[i].afficheScore(chanson)
            if valeur>plusGrandeValeur:
                plusGrandeValeur=valeur
        print("Le meilleur score est: ",plusGrandeValeur)

    def getMeilleureScoreTotal(self):
        valeurScore=0
        plusGrandScore=0
        for i in range (len(self.getplayers())):
            valeurScore=self.getplayers()[i].getMeilleureScoreTotal()
            if valeurScore>plusGrandScore:
                plusGrandScore=valeurScore
        print("Le meilleur score général est: ",plusGrandScore)

    def getMeilleureMoy(self):
        moyennej=0
        plusGrandemoyenne=0
        for i in range (len(self.getplayers())):
            moyennej=self.getplayers()[i].getMeilleurScore()
            if moyennej>plusGrandemoyenne:
                plusGrandemoyenne=moyennej
        print("La meilleure moyenne est: ",plusGrandemoyenne)
    
    def setNewPlayer(self,player):
        self.getplayers().append(player)
        print("joueur ajouter")

    def deletePlayer(self,player):
        if (len(listJoueur >2)):
            self.getplayers().remove(player)
            print("joueur supprimer")
        else:
            print ("tu ne peux supprimer ce joueur.")
    



joueur1 = Player("Castafiore",[50,75,55,0])
joueur2 = Player("Bonne question",[80,50,50,50])
joueur3 = Player("Inconnu",[0,0,0,0])

joueur1.getPseudo
joueur1.getScore
joueur1.getMeilleurScore
joueur1.getPireScore
joueur1.afficheScore
joueur1.setScore(3,61)


listJoueur=[joueur1,joueur2]
listChanson=["nothern cross","la danse des canard","Forgiven","Trip to valhalla","La glace"]
karaokeTest= Karaoke(listJoueur,listChanson)
karaokeTest.setNewPlayer(joueur3)
print(karaokeTest.getplayers())
karaokeTest.getMeilleureScore("nothern cross")
karaokeTest.getMeilleureScoreTotal()
karaokeTest.getMeilleureMoy()
karaokeTest.deletePlayer(joueur3)
print(karaokeTest.getJoueur())




    

