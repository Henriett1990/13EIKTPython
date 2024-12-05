#Készítsen Python kódot, ami bekér egy egész hőmérséklet értéket és kiírja, hogy az adott értéken milyen halmazállapotű a víz!

def homerseklet():
    homersekletC = int(input("Kérek egy hőmérséklet értéket: "))

    if homersekletC <= 0:
        print("Szilárd halmazállapot.") #igaz ág
    elif homersekletC < 100:
        print("Folyékony halmazállapot.") #hamis ág
    else: 
        print("Légnemű halmazállapot.")  #hamis ág

homerseklet()


