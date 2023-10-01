import math
import random
from collections import defaultdict
from itertools import product
import numpy as np
from matplotlib import pyplot

# Número de celdas.
nxC, nyC = 31, 31
# Radio circunferencia
radio = 15
#Concentración de medicamento 
Local_concentration = 10
#Centro circunferencia.
h = math.floor(0.5*nxC); k = math.floor(0.5*nyC)
# Listas auxiliares.
Grafica = []; sites = []
#Constantes del modelo 
D = 3.16
Cs = 12.78
T=300.15
Kb=1.380649*10**-23
pasos = 200
t=np.arange(0.01,9,10/pasos)
confianza = 0.80



# Diccionario de posiciones.
for x,y in product(range(0, nxC),range(0,nyC)): sites.append((x,y))

# Contenido de cada punto.
Contenido = dict() # Diccionario de contenido.
sites_esfera = []

# Creamos matriz medicamento - agua.
for position in sites:
    x,y = position
    if (x-h)**2+(y-k)**2<= radio**2:
        Contenido[position] = ['D', Local_concentration]
        sites_esfera.append(position) 
    else :Contenido[position] = ['W', 0]

# Medicamento inicial:
contadorDin = list(np.array(list((Contenido.values())))[:,0]).count('D')
# print("Contenido inicial: " ,contadorDin)

# Definimos la funcion energia_S
def Energia_S():
    entalpia = 55
    entropia = 0.25
    contadorD = list(np.array(list((Contenido.values())))[:,0]).count("D")
    contadord = list(np.array(list((Contenido.values())))[:,0]).count("d")
    
    Qf = contadorD+contadord
    return (entalpia+entropia)*Qf

#Definimos la función montecarlo de la siguiente manera
def montecarlo():
    for x,y in Vecinos.items():
        if len(y) == 4: # Cuando no estamos en la frontera.
            for i in y:
                
                # Celdas D:
                if Contenido[x][0]=='D' and (Contenido[i][0] == 'W' or Contenido[i][0] == 'd'):
                    Contenido[x][0] = 'd'
                    Contenido[x][1] = 10 #Contenido[x][1]-1
                
                # Celdas d:  Movimiento de las celdas d.
                elif Contenido[x][0] == 'd' and Contenido[i][0] == 'W': 
                    if random.random()< 0.3 and Contenido[x][1]>.5:
                        Contenido[i][0] = 'd' 
                        Contenido[i][1]=Contenido[x][1]-0.1
                        Contenido[x][0] = 'W' #; Contenido[x][1]=0
                    elif random.random()< 0.3 and Contenido[i][1]<=.5:
                        Contenido[x][0] = 'W' ; Contenido[x][1]=0
                    # A cada movimiento de una celda d, le corresponde a un estado general
                    # de concentración en terminos del modelo de Higuchi.
                              
        else: # Cuando estamos en la frontera.
            if Contenido[x][0] == 'd': Contenido[x][0] = 'W'

# Función Alejandria, que ajusta los cambios según el modelo de Higuchi estadisticamente
def Alejandria(t,Contenido):
    matriz_i = Contenido.copy()
    montecarlo()  # hacemos un cambio al sistema
    # Contamos el número de celdas D y d por iteración.
    contadorD = list(np.array(list((Contenido.values())))[:,0]).count("D")
    contadord = list(np.array(list((Contenido.values())))[:,0]).count("d")
    
    Qf = contadorD+contadord # Concentración por cada paso for.

    # Aplicamos un intervalo de confianza 
    if (D*t*(2*contadorDin-Cs)*Cs)**0.5 - 1.96*(4*pasos/t)**0.5/(nxC*nyC) <= Qf <= (D*t*(2*contadorDin-Cs)*Cs)**0.5 + 1.96*(4*pasos/t)**0.5/(nxC*nyC): 
        return 1-Qf/contadorDin
    else: 
        if random.random() <= np.exp(-Energia_S()/(Kb*T)): # calcularle la energia al sistema
            Contenido = matriz_i # volver al estado inicial
        else: return 1-Qf/contadorDin




    
# Creación diccionario de vecinos.
Vecinos = defaultdict(list) 

for site in Contenido:
    x,y = site
    if y-1 >= 0:
        Vecinos[site].append(((x) , (y-1) % nyC))
    if x-1 >= 0:
        Vecinos[site].append(((x-1) % nxC, (y)))
    if x+1 < nxC:
        Vecinos[site].append((x+1 % nxC, y ))
    if y+1 < nyC:
        Vecinos[site].append(((x) , (y+1) % nyC))


print("----------------------------------------------------------------------------------------------------------")

#print('Estos son los vecinos: ',Vecinos)

# Interacción:
for j in t:
    
    Fdr = Alejandria(j,Contenido)
    Grafica.append(Fdr) # Guardamos el dato para graficar.
    print(Fdr) # Para observar el comportamiento.
    
    

#print('Contenido después:', Contenido)
ti = np.arange(0,len(Grafica))

# Cálculo error cuadrático medio

y_true = Grafica
y_pred =np.sqrt(t*D*(2*contadorDin-Cs)*Cs)/(contadorDin)
mse = (np.square(y_true - y_pred)).mean()
print("mse: ", mse*100)



# Graficamos.
#pyplot.figure()
#pyplot.plot(t, Grafica, color= "blue")
#pyplot.plot(t,np.sqrt(t*D*(2*contadorDin-Cs)*Cs)/(contadorDin), color= "orange")
#pyplot.title("Concentración Vs Tiempo")
#pyplot.xlim(0, 10)
#pyplot.ylim(0, 1.1)
#pyplot.xlabel("Tiempo")
#pyplot.ylabel("Concentración")
#pyplot.grid()
#pyplot.show()

fig , ax = pyplot.subplots(layout="constrained")
ax.plot(t, Grafica, label='c')
ax.plot(t, np.sqrt(t*D*(2*contadorDin-Cs)*Cs)/(contadorDin), label='x')
ax.set_xlabel("Tiempo")
ax.set_ylabel("Concentración")
ax.set_title("Concentración Acetaminofen Vs Tiempo")
ax.grid()
pyplot.show()