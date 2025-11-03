# -*- coding: utf-8 -*-
"""

Auto und 2 Ziegen
mit festgelegter Reaktion von Bill
Created on Thu Aug 28 11:57:14 2025


@author: gerkae
"""
import numpy as np
import math as m
import random

random.seed()

# Das Experiment wird X mal durchgeführt
X = 1
s_erfolg = 0
s_bleiben = 0
swe = 0
swm = 0
sbe = 0
sbm = 0
bill2 = 0
bleiben = 1

for x in range (1, X+1):


    
    tore = [0 , 0, 0]

    
    auto = random.randint(0,2)
    tore[auto] = 1                       # hinter dieser Tür ist das Auto
#    print(tore)
    
    bill = random.randint(0,2)          # Bill wählt eine Tür
#    print("Bills erste Wahl = ", bill) 
    
    # Moderator weiss,in welchen Türen Ziegen sind und macht eine solche auf
    ziegen = [0,0]
    if (tore[0] == 1 ):                    # Wenn das Auto in der 1. Tür ist
        ziegen[0] = 1                    # dann sind Ziegen in der 2. Tür
        ziegen[1] = 2                    # und in der 3. Tür
        auto = 0                  
                                         
        
    if (tore[1] == 1 ):                    # Wenn das Auto in der 2. Tür ist
        ziegen[0] = 0                    # dann sind Ziegen in der 1. Tür
        ziegen[1] = 2                    # und in der 3. Tür
        auto = 1                   
        
    if (tore[2] == 1 ):                    # Wenn das Auto in der 3. Tür ist
        ziegen[0] = 0                    # dann sind Ziegen in der 1. Tür
        ziegen[1] = 1                    # und in der 2. Tür
        auto = 2                   
        
    
#    print("Ziegen = ", ziegen)
#    print("Auto = ", auto)
    #  im Array ziegen sind jetzt die Indices der Ziegen-Türen (minus 1)
    
    op = random.randint(0,1)         # Welche Tür soll der Moderator nicht öffnen?
    
#    print("Nicht öffnen = ", op)     # op bezieht sich auf die Indices des Array ziegen
    
    # Es sind jetzt noch die Türen Nr. bill und Nr. ziegen[op] geschlossen
    # Diese zwei Indices kommen in die neue Auswahl final = [bill-1, ziegen[op] ]
    
    final = [bill, ziegen[op] ]
#    print("Final = ",final)         # Das sind Indices für das Array tore
    
    # Aus diesem Sampel kann Bill jetzt noch mal auswählen
    # Wir legen seine Entscheidung aber selber fest
    # abwechselnd wechseln oder bleiben
    
    if (bill2 == 0):
        bill2 = 1
    else:
        bill2 = 0
    
    
#    bill2 = random.randint(0,1)
#    final[bill2] = bill
#    print("Endwahl = ",bill2)
#    if ()
    # Aus diesem Auswahlfeld final konnte Bill jetzt noch mal eine Tür auswählen
    
    # Ist er bei seiner ersten Wahl geblieben?  if (final[bill2] == bill) 
    if (final[bill2] == bill):
        bleiben = 1
    else:
        bleiben = 0
    
#    print("Bleiben = ", bleiben)
    
    # Und hat er das Auto ?
    # Ist final[bill2] == auto 
    if (final[bill2] == auto):
        erfolg = 1
        if (bleiben == 1):
            sbe = sbe + 1
        else:
            swe = swe + 1
    else:                               # in diesem Zweig hat Bill das Auto nicht
        erfolg = 0                      # also kein Erfolg
        if (bleiben == 1):
            sbm = sbm + 1               # ein Misserfolg mehr duech Bleiben
        else:
            swm = swm + 1               # ein Misserfolg mehr durch Wechsel
        
#    print("Erfolg = ", erfolg)    
    s_erfolg = s_erfolg + erfolg
    s_bleiben = s_bleiben + bleiben

# =============================================================================
# qb = sbe / s_erfolg
# qw = swe / s_erfolg
# qbm = sbm / (X-s_erfolg)
# qwm = swm / (X-s_erfolg)
# =============================================================================
print("Versuche = ",X)
print("Geblieben = ", s_bleiben)
print("Erfolg = ", s_erfolg) 
print("Erfolg durch Bleiben = ", sbe)   
print("Erfolg durch Wechsel = ", swe)
print("kein Erfolg bei Bleiben = ", sbm)
print("kein Erfolg bei Wechsel = ", swm)        
                   