import csv
from fileinput import filename
from pickle import TRUE
import random

with open('numero_aleatorio.csv', mode = 'w') as csv_file:
    fieldname = ['Numero_Aleatorio']
    writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    writer.writeheader()
    
    while TRUE:
        x = random.random()
        
        writer.writerow({'Numero_Aleatorio': x})  
    
    writer.close()