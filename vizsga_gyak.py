
from asyncio import DatagramProtocol
from curses import napms

def time_change(perc):
    
    nap = perc // (24 * 60)
    perc %=  24 * 60
    ora = perc // 60
    perc %= 60

    return "Sorozatnézéssel %02d napot %02d órát és %02d percet töltött" % (nap,ora,perc)
    #print(f"Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.")


print("1. feladat")
with open("lista-1.txt","r") as f:
    
    percek = 0
    szamlalo = 1
    szamlalo_2 = 1
    total = 0
    megnezet = 0
    darab = 0
    for line in f:
        
        sor = line.strip("\n")
        if sor[0] in {"2"}:
            if sor[1] in {"0"}: 
                darab += 1
        else:
            pass

    
    
        sor2 = line.strip("\n")

        if sor2 in {"0"}: 
            total += 1
            
        elif sor2 in {"1"}: 
            total += 1
            megnezet += 1
            
        else:
            pass


        sor3 = line.strip("\n")
        
        if szamlalo == 4:
            check = sor3
            szamlalo = 0

            
        else:
            szamlalo += 1

        if sor3 in {"1"}:   
            percek = percek + int(check)


        sor4 = line.strip("\n")
        
        if szamlalo_2 == 6:
            szam = int(sor4.strip("."))
            szamlalo_2 = 0
        else:
            szamlalo_2 += 1


            

    print("2. feladat")
    print(f"A listában {darab} db vetítési dátummal rendelkező epizód van.")
    
    print("3. feladat")
    
    ossz = float(megnezet / total * 100)                

    vegre = format(ossz,".2f")+ "%"
    print(f"A listában lévő epizódok {vegre}-át látta. ")

    print("4. feladat")
    
    print(time_change(percek))