#Bibliotecas 

from cgitb import text
import RPi.GPIO as GPIO                 #En VSC aparecen errores pero al ejecutarlo en Raspberry no ocurren
from mfrc522 import SimpleMFRC522

#iniciar sensor
reader = SimpleMFRC522()

#ciclo de control para detectar errores try:
try:
    Nombre = input('Nombre del usuario: ')
    Edad = input('Edad del usuario: ')
    Celular = input('Numero de celular del usuario: ')
    Fecha_Naciemiento = input('Fecha de nacimiento del usuario: ')
    Nivel_acceso = input('Nivel de acceso del usuario: ')
    text = (Nombre + ',' + str(Edad) +','+ str(Celular) +','+ str(Fecha_Naciemiento) +','+ str(Nivel_acceso))
    print("Acerca la etiqueta RF o tarjeta RF al sensor RF")    #Mensaje al usaurio, instruccion de acercar el tag
    reader.write(text)  #función reader lee y escribe en el tag, en este caso solo escribe
    print("Ya se escribio el texto en etiqueta RF o Tarjeta RF")    #mensaje al usuario de finalizado de proceso de escritura

finally:    #En caso de terminar realiza lo siguiente
    GPIO.cleanup()  #Limpia los puertos GPIO