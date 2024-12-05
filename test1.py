#Készítsen Python kódot, ami bekér egy egész hőmérséklet értéket és kiírja, hogy az adott értéken milyen halmazállapotű a víz!

#
homersekletC = 0
def homerseklet():
    
    if homersekletC <= 0:
        return ("Szilárd halmazállapot.") #igaz ág
    elif homersekletC < 100:
        return ("Folyékony halmazállapot.") #hamis ág
    else: 
        return ("Légnemű halmazállapot.")  #hamis ág


homersekletC = int(input("Kérek egy hőmérséklet értéket: "))
print(homerseklet())


