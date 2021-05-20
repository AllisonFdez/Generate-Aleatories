
import random
import numpy as np
import matplotlib.pyplot as plt

def generarAleatorios(cant):
    numeros = [random.randint(0,100) for _ in range(cant)]
    
    archivo = 'Aleatories.json'
    with open(archivo, 'w') as file:
        file.write('{}'.format(numeros))
    print(str(cant)+' Números aleatorios entre 0-100 guardados en '+archivo)

    xAxis = list(range(0,101))
    cantidad = []
    cantidadDict = {i:numeros.count(i) for i in xAxis}
    
    for x in xAxis:
        cantidad.append(numeros.count(x))
    
    values = np.arange(len(xAxis))
    plt.bar(values, cantidad); 
    plt.title("Cant. of Duplicates"); plt.xlabel("Number"); plt.ylabel("Count")
    plt.show()

generarAleatorios(1000)
