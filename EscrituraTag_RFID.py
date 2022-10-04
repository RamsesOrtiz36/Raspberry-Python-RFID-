#Bibliotecas 

from cgitb import text
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#iniciar sensor
reader = SimpleMFRC522()

#ciclo de control para detectar errores try:
try:
    text = input('New data: ') #Solicitar que se va escribir en el tag y guardarlo en variable text
    print("Now place your tag to write")    #Mensaje al usaurio, instruccion de acercar el tag
    reader.write(text)  #función reader lee y escribe en el tag, en este caso solo escribe
    print("Written")    #mensaje al usuario de finalizado de proceso de escritura

finally:    #En caso de terminar realiza lo siguiente
    GPIO.cleanup()  #Limpia los puertos GPIO