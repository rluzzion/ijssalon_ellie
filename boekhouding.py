from les_tijdelijk import som

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}

totaal_inkomsten = som(inkomsten)

print(totaal_inkomsten)