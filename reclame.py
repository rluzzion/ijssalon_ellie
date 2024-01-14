from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs - prijs * korting} euro."
    return tekst

def inkomsten_totaal(inkomsten):
    return sum(inkomsten)

def inkomsten_totaal(inkomsten,btw): #ik heb voor de volledigheid vraag 7 apart uitgevoerd
    tekst = f"Het totaal van alle inkomsten van deze week is {sum(inkomsten)} euro, waarover {sum(inkomsten) * btw} euro btw betaald dient te worden."
    return tekst

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    return sum(mijn_lijst) / len(mijn_lijst) # gedeeld door 7 kan in dit voorbeeld ook, maar als de list korter of langer wordt, klopt het gemiddelde niet meer

def gemiddelde(mijn_lijst): #ik heb voor de volledigheid vraag 10 apart uitgevoerd
    tekst = f"De gemiddelde inkomsten deze week zijn {sum(mijn_lijst) / len(mijn_lijst)} euro"
    return tekst

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer