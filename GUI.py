from tkinter import *
from Model import Model
from Model import Feld

class GUI(object):
    '''
    Wird benutzt um das 4 Gewinnt Spiel zu steuern. 
    '''
    def __init__(self,dictionary):
        '''
        Erstellt ein GUI Objekt.
        '''
        self.dictMethoden = dictionary

        # Farben
        self.bgSpielfeld = "blue"
        self.bgLabels = "#0096FF"
        self.bgButton = "white"
        self.fgButton = "black"
        self.Aktuellefarbe = "reset"
        self.spielzuege = 0
        self.fertig = False
        self.einmal = True
        
        self.fenster = Tk()
        self.fenster.title("4Gewinnt")
        self.fenster.geometry("720x1000")
        self.fenster.resizable(False, False)
        
        # Bilder
        self.defaultImg = "buttonGrey.png"
        self.defaultImage = PhotoImage(file=self.defaultImg)

        self.buttonRedImg = "buttonRed.png"
        self.buttonRedImage = PhotoImage(file=self.buttonRedImg)

        self.buttonYellowImg = "buttonYellow.png"
        self.buttonYellowImage = PhotoImage(file=self.buttonYellowImg)
        
        self.bilderListe = [self.buttonYellowImage,self.buttonRedImage,self.defaultImage]
        
        # Überschrift

        self.labelÜberschrift = Label(master=self.fenster, bg=self.bgLabels, fg="black", text="4 Gewinnt", font=("Arial", 44, "bold"))
        self.labelÜberschrift.place(x=10, y=10, width=700, height=80)

        self.frameSpielfeld = Frame(master=self.fenster, bg=self.bgSpielfeld)
        self.frameSpielfeld.place(x=10, y=190, width=700, height=600)

        # Spielfeld erstellen
        xWert = 0
        yWert = 0
        self.listeFelder = []

        felderListe = []
        for zaehler in range(42):
            string = "feld" + str(zaehler)
            felderListe.append(string)
        for feld in felderListe:
            feld = Label(master=self.frameSpielfeld, fg="black",
                         image=self.defaultImage, text=str(feld), bg=self.bgSpielfeld)
            self.listeFelder.append(feld)
            feld.place(x=xWert, y=yWert, height=100, width=100)
            xWert += 100
            if xWert == 700:
                xWert = 0
                yWert += 100

        # Buttons
        self.frameButtons = Frame(master=self.fenster, bg=self.bgLabels)
        self.frameButtons.place(x=10,y=100,height=80,width=700)

        self.button1 = Button(master=self.frameButtons, text="▼", font=("Arial", 20, "bold"),bg=self.bgButton, fg=self.fgButton, command=lambda: self.dictMethoden["ButtonTop"](
            0, self.listeFelder, self.labelÜberschrift, self.bilderListe,self.framePlayers))
        self.button1.place(x=20, y=10, height=60, width=60)
        self.button2 = Button(master=self.frameButtons, text="▼", font=("Arial", 20, "bold"), bg=self.bgButton, fg=self.fgButton, command=lambda: self.dictMethoden["ButtonTop"](
            1, self.listeFelder, self.labelÜberschrift, self.bilderListe, self.framePlayers))
        self.button2.place(x=120, y=10, height=60, width=60)
        self.button3 = Button(master=self.frameButtons, text="▼", font=("Arial", 20, "bold"), bg=self.bgButton, fg=self.fgButton, command=lambda: self.dictMethoden["ButtonTop"](
            2, self.listeFelder, self.labelÜberschrift, self.bilderListe, self.framePlayers))
        self.button3.place(x=220, y=10, height=60, width=60) 
        self.button4 = Button(master=self.frameButtons, text="▼", font=("Arial", 20, "bold"), bg=self.bgButton, fg=self.fgButton, command=lambda: self.dictMethoden["ButtonTop"](
            3, self.listeFelder, self.labelÜberschrift, self.bilderListe, self.framePlayers))
        self.button4.place(x=320, y=10, height=60, width=60)
        self.button5 = Button(master=self.frameButtons, text="▼", font=("Arial", 20, "bold"), bg=self.bgButton, fg=self.fgButton, command=lambda: self.dictMethoden["ButtonTop"](
            4, self.listeFelder, self.labelÜberschrift, self.bilderListe, self.framePlayers))
        self.button5.place(x=420, y=10, height=60, width=60)
        self.button6 = Button(master=self.frameButtons, text="▼", font=("Arial", 20, "bold"), bg=self.bgButton, fg=self.fgButton, command=lambda: self.dictMethoden["ButtonTop"](
            5, self.listeFelder, self.labelÜberschrift, self.bilderListe, self.framePlayers))
        self.button6.place(x=520, y=10, height=60, width=60)
        self.button7 = Button(master=self.frameButtons, text="▼", font=("Arial", 20, "bold"), bg=self.bgButton, fg=self.fgButton, command=lambda: self.dictMethoden["ButtonTop"](
            6, self.listeFelder, self.labelÜberschrift, self.bilderListe, self.framePlayers))
        self.button7.place(x=620, y=10, height=60, width=60)

        # Spielerauswahl
        self.framePlayers = Frame(master=self.fenster, bg=self.bgLabels)
        self.framePlayers.place(x=10,y=800,width=700,height=80)
        self.buttonStart = Button(master=self.framePlayers, bg=self.bgButton,
                                  text="(Re-)start", fg="black", command=lambda: self.dictMethoden["StartReset"](self.listeFelder,self.labelÜberschrift,self.bgLabels,self.framePlayers,self.bilderListe), font=("Arial", 16, "bold"))
        self.buttonStart.place(x=300, y=10, width=100, height=60)

        # Credits
        self.frameCredits = Frame(master=self.fenster, bg=self.bgLabels)
        self.frameCredits.place(x=10, y=890, width=700, height=100)
        self.labelCredits = Label(master=self.frameCredits,text="Informatikprojekt April 2022 \n Danke an alle Tester")
        self.labelCredits.place(x=10,y=10,width = 680,height = 80)
        
        self.fenster.mainloop()
