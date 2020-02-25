import xml.etree.ElementTree as ET

## def ordenarXML(parent, attr):
   ## parent[:] = sorted(parent, key=lambda child: child.get(attr))

baraja = ET.ElementTree(file="myBaraja.xml")
root = baraja.getroot()

## ordenarXML(root, 'attack')

class Carta:
    def __init__(self, name ,attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense



def cardSelect():
    cont = 0
    value = 5
    global p1

    while True:
        if value<0:
            return
        for child in root.findall('.//deck/'):
            for cardChild in child.getchildren():
                if cont == 10:
                    return
                if cardChild.tag == "name":
                    name = cardChild.text
                if cardChild.tag == "attack":
                    attack = int(cardChild.text)
                if cardChild.tag == "defense":
                    defense = int (cardChild.text)
            if attack == value:
                p1 = Carta(name, attack, defense)
                cont = cont+1


        value = value-1


cardSelect()
print(p1.name+" "+str(p1.attack)+" "+str(p1.defense))
