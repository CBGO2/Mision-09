#   Carlos Badillo García
#   Programa que con una lista principal, regresa distintos resultados y/o listas dependiendo la funcion llamada

def extraerPares(listaPrincipal):   #Extrae los numeros pares de una lista y los agrega a otra lista
    listaNueva = []

    for x in listaPrincipal:
        if x % 2 == 0:
            listaNueva.append(x)
    return listaNueva


def extraerMayoresPrevio(listaPrincipal):   #Extrae los numero mayores que el numero anterior y los agrega a una nueva lista
    listaNueva = []
    
    if listaPrincipal == []:
        return []

    for x in range(1, len(listaPrincipal)):
        if listaPrincipal[x] > listaPrincipal[x-1]:
            listaNueva.append(listaPrincipal[x])
    return listaNueva


def intercambiarParejas(listaPrincipal):    #Cambia de lugar los numeros de par en par, si la lista es impar, el ultimo valor se deja intacto
    listaNueva = []

    for x in range(len(listaPrincipal)):
        if x % 2 == 0:
            listaNueva.append(listaPrincipal[x])
        else:
            listaNueva.insert(x-1, listaPrincipal[x])
    return listaNueva


def intercambiarMM(listaPrincipal):     #Cambia de lugar al mayor y al menor dato dentro de la lista
    if listaPrincipal == []:
        return []
    if len(listaPrincipal) == 1:
        return []
    else:
        minimo = min(listaPrincipal)
        maximo = max(listaPrincipal)
        posMin = listaPrincipal.index(minimo)
        posMax = listaPrincipal.index(maximo)
        listaPrincipal.remove(minimo)
        listaPrincipal.remove(maximo)
        listaPrincipal.insert(posMin, maximo)
        listaPrincipal.insert(posMax, minimo)
        return listaPrincipal


def promediarCentro(listaPrincipal):    #Calcula el promedio de la lista, exceptuando el maximo y el minimo

    if listaPrincipal == []:
        return 0

    if len(listaPrincipal) <= 2:
        return 0
    else:
        listaN = listaPrincipal[:]
        minimo = min(listaN)
        maximo = max(listaN)
        listaN.remove(minimo)
        listaN.remove(maximo)
        promedio = sum(listaN)//len(listaN)
        return promedio


def calcularEstadistica(listaPrincipal):    #Calcula la media y la desviacion estandar de una lista
    suma = sum(listaPrincipal)

    if listaPrincipal == []:
        return (0,0)
    if len(listaPrincipal) == 1:
        return (0,0)
    else:
        media = suma/len(listaPrincipal)
        contador = 0

        for x in listaPrincipal:
            datos = (x - media)**2
            contador = contador + datos
        desviacion = (contador/(len(listaPrincipal)-1))**(1/2)
        return media, desviacion


def main():
    listaPrincipal = [1,2,3,4]
    print(listaPrincipal)
    print(extraerPares(listaPrincipal))
    print(extraerMayoresPrevio(listaPrincipal))
    print(intercambiarParejas(listaPrincipal))
    print(intercambiarMM(listaPrincipal))
    print(promediarCentro(listaPrincipal))
    print(calcularEstadistica(listaPrincipal))

main()