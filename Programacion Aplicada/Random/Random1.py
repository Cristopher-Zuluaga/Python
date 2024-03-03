import csv
import random
from datetime import datetime
import matplotlib.pyplot as plt

# Generar datos y escribirlos en un archivo CSV
with open('numero_tiempo.csv', mode='w') as csv_file:
    fieldname = ['Numero_Aleatorio', 'Tiempo']
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()

    for _ in range(10):  # Genera 10 números aleatorios
        x = random.random()
        tiempo_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow({'Numero_Aleatorio': x, 'Tiempo': tiempo_actual})

# Leer datos del archivo CSV y almacenarlos en listas separadas
with open('numero_tiempo.csv', mode='r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)

    lista_numeros = []
    lista_tiempos = []
    for row in reader:
        numero = float(row[0])
        tiempo = row[1]
        lista_numeros.append(numero)
        lista_tiempos.append(tiempo)

# Crear el gráfico de dispersión
plt.scatter(lista_numeros, range(len(lista_numeros)))

# Agregar etiquetas a los ejes
plt.xlabel("Número aleatorio")
plt.ylabel("Índice")

# Mostrar el gráfico
plt.show()

# Imprimir las listas (opcional)
print("Números:", lista_numeros)
print("Tiempos:", lista_tiempos)
