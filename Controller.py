from GUI import GUI
from Model import Model

class Controller(object):
    '''
    Wird benutzt um das 4 Gewinnt Spiel zu starten. Übergibt Methoden vom Model an die GUI. Verbindung der 2 Haelften.
    '''
    def __init__(self):
        '''
        Erstellt ein GUI und ein Model Objekt.
        '''
        self.model = Model()
        self.gui = GUI(self.model.getDictMethoden())

c = Controller()





