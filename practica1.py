#Puede empezar por +2digitos 002digitos o nada(9 digitos/letras)
#Si letras, cada 3 equivalen a un numero siendo a,b,c ->1
def sustituirLetra(cad):
        return "s"

def procesarLetras(cad):
    if( cad.isdigit() ):
        return cad[0:3]+" "+cad[3:6]+" "+cad[6:9]
    else:
        for i in range(0,len(cad),1):
            #Usar una cadena complementaria aqui para cosas
            if(not cad[i].isdigit()):
                cad[i] = sustituirLetra(cad[i])

cadena = str(input("tu cadena> "))
if cadena[0] == "+":
    print cadena[:3]+" " +procesarLetras(cadena[3:])
else:
    if cadena[:2] == '00':
        print cadena[:4]+" " +procesarLetras(cadena[3:])
    else:
        print procesarLetras(cadena)
