from random import randint, seed

class Model(object):
    '''
    Führt Befehle aus die durch Knopfdrück in der GUI ausgelöst werden.
    '''
    def __init__(self):
        seed()
        '''
        Erstellt ein Model-Objekt mit allen benötigten Attributen. 
        '''
        self.felderListe = []
        self.aktuellerSpieler = None
        self.fertig = False
        self.einmal = True
        self.Aktuellefarbe = "reset"
        self.spielzuege = 0
        
        # Felder Objekte erstellen
        for counter in range(42):
            feld = Feld()
            self.felderListe.append(feld)
        counter = 0
        for yWert in range(6):
            for xWert in range(7):
                self.felderListe[counter].setY(yWert)
                self.felderListe[counter].setX(xWert)
                counter += 1
                
    def getDictMethoden(self):
        '''
        Methode um der GUI über den Controller Zugriff auf die self.buttonTop und self.startResetButton Methoden zu geben.
        Verknüpft GUI und Model
        Parameter: keine
        Rückgabewert: Dictionary mit Methoden
        '''
        self.dictMethoden = {
                             "ButtonTop": self.buttonTop,
                             "StartReset":self.startResetButton
                             }
        return self.dictMethoden

    def autoSwitch(self,pFramePlayers):
        '''
        Methode zuständig fürs wechseln der Spieler.
        Methode läuft nur ab wenn das Spiel noch nicht beendet ist und schon ein Knopf gedrückt wurde bzw. das erste Mal gedrückt wird.
        Sie bestimmt welcher Spieler an der Reihe ist und ändert dementsprechend die aktuelle Farbe und den Hintergrund des angegebenen GUI-Elements ab.
        Parameter: 
        - pFramePlayer (tkinter frame): ist das Element der GUI bei dem später die Farbe an den aktuellen Spieler angepasst werden soll
        Rückgabewert: keiner
        '''
        if self.fertig == False:
            if self.einmal == True:
                if self.spielzuege % 2 == 0 or self.spielzuege == 0:
                    self.aktuellerSpieler = "Spieler1"
                    self.Aktuellefarbe = "gelb"
                    pFramePlayers.config(bg="yellow")
                    print("Spieler1 GELB ist dran")
                else:
                    self.aktuellerSpieler = "Spieler2"
                    self.Aktuellefarbe = "rot"
                    pFramePlayers.config(bg="red")
                    print("Spieler2 ROT ist dran")
                self.einmal = False
        else:
            ("Spiel Vorbei!")


    def buttonTop(self, num, pFelderLabelListe, pÜberschriftLabel, pBilderListe, pFramePlayers):
        '''
        Ermittelt durch self.rutschen wo das Feld in der angeklickten Spalte plaziert werden kann. Ändert die Farbe an dieser Stelle. 
        Checkt danach ob der Spieler gewonnen hat. Danach wird der Spieler gewechselt.
        Parameter: 
        - num (int): x-Koordinate der Knöpfe die diese Methode von der GUI aus auslösen können.
        - pFelderLabelListe (list): Liste der Tkinter-Labels die in der GUI das Spielfeld bilden
        - pÜberschriftLabel (tkinter label): Label mit der Überschrift in der GUI
        - pBilderListe (list): Liste mit den Bilder um die Labels im GUI-Spielfeld zu füllen
        - pFramePlayers (tkinter frame): ist das Element der GUI bei dem später die Farbe an den aktuellen Spieler angepasst werden soll
        Rückgabewert: keiner
        '''
        if self.einmal == False:
            feldNummer = self.rutschen(num) 
            if feldNummer == "voll":
                print("ACHTUNG! Alle Felder sind belegt bitte auf den Restart Knopf drücken!")
            elif feldNummer == "gehtnicht":
                print("Geht nicht! Suche einen anderen Punkt für deine Platzierung")
            else:
                self.farbeAendern(pFelderLabelListe[feldNummer], self.Aktuellefarbe, pBilderListe)
                self.einmal = True
                erfolg = self.checkFeld()
                if erfolg:
                    print("Spieler: ",self.aktuellerSpieler,"gewinnt!!")
                    self.fertig = True
                    self.gewinn(pÜberschriftLabel)
                self.spielzuege += 1
                self.autoSwitch(pFramePlayers)
                
    def rutschen(self,num):
        '''
        Checkt ob nicht schon das ganze Feld voll ist. Checkt ob das Feld überhaupt frei ist und wieviel es in der gewählten Spalte nach unten rutschen kann.
        Parameter: 
        - num (int): x-Koordinate der Knöpfe die diese Methode von der GUI aus auslösen können.
        Rückgabewert (int oder str): Stelle also INT in der Liste mit den Felder wo das Feld hingerutscht ist. Wenn ein plazieren nicht möglich ist wird ein STR mit "gehtnicht" zurückgegeben
        '''
        übrig = 0
        # prüfen ob überhaupt noch Platz ist:
        for feld in self.felderListe:
            if feld.nichtBesetzt() == "Leer":
                übrig += 1
        if übrig == 0:
            return "voll"
        # "runterrutschen"
        if self.felderListe[num].nichtBesetzt() == "Leer":
            while True:
                if not num >= 35:
                    if self.felderListe[num+7].nichtBesetzt() == "Leer":
                        num += 7 
                    else: 
                        break
                else:
                    break
            self.felderListe[num].setSpieler(self.aktuellerSpieler)
            return num
        else:
            return "gehtnicht"

    def checkFeld(self):
        '''
        Sucht im Spielfeld nach 4er Reihen für den aktuellen Spieler. Bei Erfolg wird True, bei Nichterfolg False zurückgegeben.
        Parameter: keine
        Rückgabewert: BOOL
        '''
        for feld in self.felderListe:
            erfolg = 0
            if feld.nichtBesetzt() == self.aktuellerSpieler:
                NummerListe = self.felderListe.index(feld)      
                         
                # Horizontal
                for x in range(7-feld.x):
                    if feld.getX() < 4:
                        if self.felderListe[NummerListe+x].nichtBesetzt() == self.aktuellerSpieler:
                            erfolg += 1 
                            # hier gleich 4 weil x bei 0 startet und dann nochmal das ursprungfeld prüft!!
                            if erfolg == 4:
                                print("Horizontal", NummerListe)
                                return True
                        else:
                            break
                    else:
                        break
                erfolg = 0
                
                # Vertikal
                for x in range(6-feld.y):
                    if self.felderListe[NummerListe+7*x].nichtBesetzt() == self.aktuellerSpieler:
                        erfolg += 1
                        if erfolg == 4:
                            print("Vertikal", NummerListe)
                            return True
                    else:
                        break
                erfolg = 0
                
                # Schräg nach Rechts
                if feld.getY() < 3 and feld.getX() < 4:
                    for x in range(6-feld.y):
                        if self.felderListe[NummerListe+8*x].nichtBesetzt() == self.aktuellerSpieler:
                            erfolg += 1
                            if erfolg == 4:
                                print("Schräg R", NummerListe)
                                return True
                        else:
                            break
                erfolg = 0
                
                # Schräg nach Links
                if feld.getY() < 3 and feld.getX() > 2:
                    for x in range(6-feld.y):
                        if self.felderListe[NummerListe+6*x].nichtBesetzt() == self.aktuellerSpieler:
                            erfolg += 1
                            if erfolg == 4:
                                print("Schräg L", NummerListe)
                                return True
                        else:
                            break
                erfolg = 0
        return False
    
    def startResetButton(self, pFelderLabelListe, pÜberschriftLabel, pResetBG, pFramePlayers, pBilderListe):
        '''
        Setzt das Spiel so zurück das eine weitere Runde gespielt werden kann.
        Parameter: 
        - pFelderLabelListe (list): Liste der Tkinter-Labels die in der GUI das Spielfeld bilden
        - pÜberschriftLabel (tkinter label): Label mit der Überschrift in der GUI
        - pResetBG (str): Original Farbe des Überschriften Labels der GUI
        - pFramePlayers (tkinter frame): ist das Element der GUI bei dem später die Farbe an den aktuellen Spieler angepasst werden soll
        - pBilderListe (list): Liste mit den Bilder um die Labels im GUI-Spielfeld zu füllen
        Rückgabewert: keiner
        '''
        # Reset Objekte
        for feld in self.felderListe:
            feld.setSpieler("Leer")
        # Reset Labels
        for feld in pFelderLabelListe:
            self.farbeAendern(feld, "reset", pBilderListe)
        self.fertig = False
        self.einmal = True
        self.spielzuege = randint(0, 1)
        pÜberschriftLabel.config(text="4 Gewinnt", bg=pResetBG)
        self.autoSwitch(pFramePlayers)
        
    def gewinn(self, pÜberschriftLabel):
        '''
        Wird ausgeführt wenn ein Spieler 4 in einer Reihe hat. Ändert Farbe und Text der Überschrift in der GUI.
        Parameter:
        - pÜberschriftLabel (tkinter label): Label mit der Überschrift in der GUI
        Rückgabewert: keiner
        '''
        if self.Aktuellefarbe == "rot":
            gewinnerFarbe = "red"
            changeSpieler = "Spieler2 (Rot)"
        elif self.Aktuellefarbe == "gelb":
            gewinnerFarbe = "yellow"
            changeSpieler = "Spieler1 (Gelb)"
        else:
            gewinnerFarbe = "grey"
            changeSpieler = "Niemand"
        text = changeSpieler + " gewinnt!"
        pÜberschriftLabel.config(bg=gewinnerFarbe, text=text)
                
    def farbeAendern(self, pFeld, pFarbe, pBilderListe):
        '''
        Ändert das Bild in einem Label im GUI-Spielfeld.
        Parameter:
        - pFeld (tkinter label): Feld im GUI-Spiefeld bei dem das Bild bzw die Farbe geändert werden soll
        - pFarbe (str): farbe die das Feld annehmen soll
        - pBilderListe (list): Liste mit den Bilder um die Labels im GUI-Spielfeld zu füllen
        Rückgabewert: keiner
        '''
        if pFarbe == "rot":
            farbeNeu = pBilderListe[1]
        if pFarbe == "gelb":
            farbeNeu = pBilderListe[0]
        if pFarbe == "reset":
            farbeNeu = pBilderListe[2]
        pFeld.config(image=farbeNeu)
        
class Feld(object):
    '''
    Jedes Feld-Objekt stellt ein Feld auf dem 4 gewinnt Spielfeld da. 
    '''
    def __init__(self):
        '''
        Erstellt ein Feld-Objekt mit leeren Koordinatenangaben und Spielerangaben.
        '''
        self.x = None
        self.y = None
        self.spieler = False
        
    def getX(self):
        '''
        Rückgabewert: int: gibt x-Koordinate des Feldes zurück
        '''
        return self.x
    
    def getY(self):
        '''
        Rückgabewert: int: gibt y-Koordinate des Feldes zurück
        '''
        return self.y
        
    def setX(self,pX):
        '''
        Parameter: pX (int): ordnet dem Feld eine x-Koordinate zu
        '''
        self.x = pX
    
    def setY(self,pY):
        '''
        Parameter: pY (int): ordnet dem Feld eine y-Koordinate zu
        '''
        self.y = pY

    def setSpieler(self,pSpieler):
        '''
        Parameter: pSpieler (str): ordnet dem Feld einen Spieler zu
        '''
        self.spieler = pSpieler

    def nichtBesetzt(self):
        '''
        Gibt entweder "leer" zurück wenn das Feld keinem Spieler gehört oder falls es einem gehört seinen Namen als string
        Parameter: keine
        Rückgabewert: str
        '''
        if self.spieler == False:
            return "Leer"
        else:
            return self.spieler
