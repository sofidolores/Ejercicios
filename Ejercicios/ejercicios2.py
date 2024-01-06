Variable1 = float (input ("valor de variable 1:"))
Variable2 = float (input ("valor de variable2:"))
Variable3 = float (input ("valor de variable3:"))
Variable4 = float (input ("valor de variable4:"))
VariableJ = 0

if Variable1 > 100:
    VariableJ += 1

if Variable2 > 100:
    VariableJ += 1

if Variable3 > 100:
    VariableJ += 1

if Variable4 > 100:   
    VariableJ += 1
print ("cantidad de variables mayores a 100:", VariableJ)