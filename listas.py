l = [1,2,3,4,5]

#Printeo total
print(l)

#Recorrido printeando
for x in l:
    print (x)

#Slices
#Del segundo en adelante
print("Del segundo en adelante: ", l[1:])

#Hasta el segundo
print("Hasta el segundo: ", l[:2])

#Ultimo elemento
print("Ultimo elemento: ", l[-1])

#"Compresion" de listas
print(list((x if x%2 == 0 else "impar") for x in l),"\n\n")

#Averiguar los X primeros primos
def primos(x):
    def esPrimo(x):
        if x == 1:
            return False
        else:
            if x == 2:
                return True
            else:
                for y in range(2, x, 1):
                    if x % y == 0:
                        return False
        return True

    toret = []
    aux = 1
    while len(toret) < x:
        if esPrimo(aux):
            toret.append(aux)
        #Uncomentar para ñopes
        #else:
            #print(aux, "ño")
        aux += 1

    print("\nlos ", x, " primeros primos son: ", toret)

primos(7)

print("\n\n\n\n\n\n\n\n\n\n")

def evaluar_expresion_alpha():

    def operar(op,v1,v2):
        return {
            '+': int(v1) + int(v2),
            '-': int(v2) - int(v1),
        }[op]

    cad = input("Expresion a evaluar> ")
    splitted = cad.split()
    valor1 = splitted[-1]
    valor2 = splitted[-2]
    valor1 = operar(splitted[-3], valor1, valor2)
    print(valor1)

#evaluar_expresion_alpha()

def evaluar_expresion():

    def operar(op,v1,v2):
        return {
            '+': int(v1) + int(v2),
            '-': int(v2) - int(v1),
        }[op]

    cad = input("Expresion a evaluar> ")
    splitted = cad.split()
    valueList = []
    for _ in range(1, len(splitted) + 1, 1):
        aux = splitted.pop()
        if aux.isdigit():
            valueList.append(aux)
        else:
            valueList.append(operar(aux,valueList[-1],valueList[-2]))

    print(valueList[-1])
evaluar_expresion()








