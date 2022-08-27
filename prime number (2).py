sisuu = 10000000000000000
niwokakemakuttakazu = 2
kaisuu = 1
merusennnusosuunokouho = 0
yakusuunokazu = 0
yakusuunokouho = 1
print(1,'No')

while kaisuu <= sisuu:

    niwokakemakuttakazu = niwokakemakuttakazu * 2
    merusennnusosuunokouho = niwokakemakuttakazu - 1
    print (merusennnusosuunokouho)
   
    while yakusuunokazu < 2 :
       
        if merusennnusosuunokouho % yakusuunokouho == 0:
            yakusuunokazu = yakusuunokazu + 1
            
        yakusuunokouho = yakusuunokouho + 2
     
    if merusennnusosuunokouho == yakusuunokouho - 2:
        print ('Yes')  
    else: 
        print ('No')   

    yakusuunokouho = 1
    yakusuunokazu = 0   

    
    

