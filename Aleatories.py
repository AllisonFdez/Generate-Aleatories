
import random
import numpy as np
import matplotlib.pyplot as plt

def generateAleatories(cant):
    numbers = [random.randint(0,100) for _ in range(cant)]
    
    filename = 'Aleatories.json'
    with open(filename, 'w') as file:
        file.write('{}'.format(numbers))
    print(str(cant)+' Random numbers over the range 0-100 saved in '+filename)

    xAxis = list(range(0,101))
    duplicates = []
    
    for x in xAxis:
        duplicates.append(numbers.count(x))
    
    values = np.arange(len(xAxis))
    plt.bar(values, duplicates); 
    plt.title("Cant. of Duplicates"); plt.xlabel("Number"); plt.ylabel("Count")
    plt.show()

generateAleatories(1000)
