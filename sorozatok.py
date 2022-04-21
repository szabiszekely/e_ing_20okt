
from asyncio import DatagramProtocol


print("1. feladat")
with open("lista-1.txt","r") as f:
    
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

        if sor2[0] in {"0"}: 
            total += 1
            print(sor2)
        elif sor2[0] in {"1"}: 
            total += 1
            megnezet += 1
            print(sor2)
        else:
            pass
                

    print("2. feladat")
    print(f"A listában {darab} db vetítési dátummal rendelkező epizód van.")
    
    print("3. feladat")
    
    ossz = int(megnezet) / int(total)
    print(total)
    print(megnezet)
    print(ossz)













