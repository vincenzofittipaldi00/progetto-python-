mesi =["gen" "feb" "mar" "apr" "mag"  "giu" "lug" "ago" "set" "ott" "nov" "dic"]
spese = [820, 760 ,  910 , 700, 680 , 1250 , 890 , 1420 ,730 , 770 , 800, 1100]
budget= 900

#stampare i mesi sopra il budget

print("mesi sopra il budget")

for i in range (len(mesi)):
    
    if spese [i] > budget:
        print(mesi[i])
        
        #calcolare il totale delle spese
        
        totale = sum(spese)
        
        print(" totale dell anno:" ,totale )
        
        #calcolare la media mensile
        
        media = totale / len(spese)
        
        print("media mensile:" , format(media, "2f"))
    


       