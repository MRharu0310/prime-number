print (2 ,end=" ")

sosuunokouho = 3
yakusuunokazu = 0
yakusuunokouho = 1
kokomademotomeru = 100000

while sosuunokouho <= kokomademotomeru:
    
    while yakusuunokazu < 2 :
       
        if sosuunokouho % yakusuunokouho ==0:
            yakusuunokazu = yakusuunokazu + 1
            
        yakusuunokouho = yakusuunokouho + 2
     
    if sosuunokouho == yakusuunokouho - 2:
        print (sosuunokouho , end=" ")  
   
    yakusuunokouho = 1
    yakusuunokazu = 0
    sosuunokouho = sosuunokouho + 2              