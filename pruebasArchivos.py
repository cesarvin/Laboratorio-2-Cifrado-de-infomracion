##Grupo #1 Lab2 Block Ciphers.
# Jorge Azmitia
# Cristina Bautista
# Sebastian Maldonado
# Abril Palencia
# Cesar Rodas

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import os
import os.path


ans=True
while ans:
    # Se declara el salt previamente generado de forma aleatoria
        # El salt es un conjunto de data que se utiliza como un input adificonal a una funcion
        # unidireccional que hashea data
    salt = b'\xfd\xb0>]T^\xa6e[\xad\x8e;\x04\x0b\x1doJ\x12^\x0e\x98x|`\xa8\\\xd7\xae\x83\xc1\x16\xf8'
    
    print ("""
        1.Enctiptar Archivo
        2.Desenctiptar Archivo
        4.Exit/Quit
        """)
    ans=input("Seleccione una opcion: ")
    
    if ans=="1":
     
        # se solicita el password para cifrar el archivo
        password = input("Ingrese el password: ")
        
        # Se genera una llave en base al password previamente definido, al salt generado
        # Esta llave se utilizara para la encripcion.
        key = PBKDF2(password,salt,dkLen=32)

        # se solicita el nombre del archivo que debe estar en la misma carpeta del script
        file_name = input("Ingrese el nombre del archivo para encriptar: ")
        
        #se lee el archivo txt que se desea encriptar
        with open(file_name, 'rb') as fo:
            file_plaintext = fo.read()
           
        # mensaje a encriptar 
        file_to_crypt = file_plaintext + b"\0" * (AES.block_size - len(file_plaintext) % AES.block_size)

        # vector de inicialización para el cifrado
        iv = Random.new().read(AES.block_size)

        # seleccionar el metodo de cifrado, utilizamos CBC
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # archivo encriptado
        file_encrypt = iv + cipher.encrypt(file_to_crypt)
        
        # se escribe el nuevo archivo encriptado 
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(file_encrypt)
        
        # se elimina el archivo no encriptado
        os.remove(file_name)
        
        print("\n -----Archivo encriptado correctamente-----") 
       
    elif ans=="2":
        # se solicita el password usado para cifrar el archivo
        password = input("Ingrese el password que utilizo para encriptar el archivo: ")
        
        # se solicita el nombre del archivo encriptado que debe estar en la misma carpeta del script 
        file_name = input("Ingrese el nombre del archivo encriptado: ")

        # Se genera una llave en base al password previamente definido, al salt generado
        # Esta llave se utilizara para la encripcion.
        key = PBKDF2(password,salt,dkLen=32)

        # se lee el texto cifrado del archivo
        with open(file_name, 'rb') as fo:
            cipher_file = fo.read()
        
        # vector de inicialización para el cifrado
        iv = cipher_file[:AES.block_size]
        
        # seleccionar el metodo de cifrado, utilizamos CBC
        cipher_cbc = AES.new(key, AES.MODE_CBC, iv)

        # archivo desencriptado
        file_plaintext = cipher_cbc.decrypt(cipher_file[AES.block_size:])
        file_decrypt = file_plaintext.rstrip(b"\0")
        
        # se escribe el archivo desencriptado
        with open(file_name[:-4], 'wb') as fo:
            fo.write(file_decrypt)
        
        # se elimina el archivo encriptado
        os.remove(file_name)
        
        print("\n -----Archivo desencriptado correctamente-----") 

    elif ans=="4":
        print("\n Gracias por utilizar el programa")
        exit()
    elif ans !="":
        print("\n Opion invalida, favor intente de nuevo")


#   RESPUESTAS

#   i. ¿Qué modo de AES usó? ¿Por qué?
#   Se utilizó el modo cbc, porque es de los modos de encriptación más recientes de AES, en el que se utiliza un vector 
#   de inicializació que generalmente es un random para generar los mensajes, es el modo mas utilizado de AES
#
#   ii. ¿Qué parámetros tuvo que hacer llegar desde su función de Encrypt a la Decrypt? ¿Por qué?
#   para usar el modo CBC se crea un AES con la llave, el modo y el vector de inizialización
#   se creó el parámetro key con la llave, la cuál es importante ya que sin esta no se puede implementar el modo y será utilzada para encriptar dentro de las operaciones del cypher
#   también el parametro iv que se generó a travez del tamaño del bloque para encriptar 
#
#   iii. ¿Qué variables considera las más importantes dentro de su implementación? ¿Por qué?
#   consideramos que las mas importantes son key y iv ya que depende de estas variables para saber que tan seguro es el cipher
#