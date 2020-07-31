##Grupo #1 Lab2 Block Ciphers.
# Jorge Azmitia
# Cristina Bautista
# Sebastian Maldonado
# Abril Palencia
# Cesar Rodas

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

ans=True
while ans:
 print ("""
    1.Enctiptar
    2.Desenctiptar
    4.Exit/Quit
    """)
 ans=input("Seleccione una opcion: ")
 if ans=="1":
     
     ##Se declara un archivo en el cual se sacara el resultado encriptado
     output_file = 'encrypted.bin' #Output file
     #Se solicita el texto a encriptar
     texto = input("Ingrese un texto: ")
     #Se colicita una clave a encriptar
     password = input("Ingrese un password: ")
     #Se declara el salt previamente generado de forma aleatoria
     #El salt es un conjunto de data que se utiliza como un input adificonal a una funcion
     #unidireccional que hashea data
     salt = b'\xfd\xb0>]T^\xa6e[\xad\x8e;\x04\x0b\x1doJ\x12^\x0e\x98x|`\xa8\\\xd7\xae\x83\xc1\x16\xf8'
     #--------------------------------
     #Pregunta b.i Si, se necesita hacer encode. Sobre la data a encriptar. Esto para pasarla al formato necesario para la encripcion
     #--------------------------------
     data = texto.encode('utf-8')
     #Se genera una llave en base al password previamente definido, al salt generado
     #Esta llave se utilizara para la encripcion.
     key = PBKDF2(password,salt,dkLen=32)

     #Utilizaremos un cifrado CBC "code block chaining" este es un modo de operacion de un block cipher
     #Este se hace en base a la llave anteriormente generada. 

     #--------------------------------
     #Pregunta b.ii Se utilizo el modo CBC. Esto debido a que nos parecio interesante utilizar una forma mas avanzada de code block cipher
     #Esto es ya que a cada bloque de texto le aplica un XOR con el bloque previo de cifrado. Esto hace que cada uno de los bloques dependa del anterior hasta el punto actual
     #Aparte, utiliza un vector de inicializacion para el primer bloque, por lo cual se necesita el mismo asi como cada uno de los bloques
     #--------------------------------

     cipher = AES.new(key, AES.MODE_CBC)
     #Para cifrar la data se procede a hacer un pad al input y luego se encripta el resultado
     ciphered_data = cipher.encrypt(pad(data,AES.block_size))

     #Se procede a guardar el texto cifrado en un archivo para guardarlo.
     file_out = open (output_file,"wb")
     #Guardamos el vector de inicializacion (Este se requiere para la desencripcion)      
     file_out.write(cipher.iv)
     file_out.write(ciphered_data)
     #Se muestra el texto cifrado
     print("Texto encriptado: ",ciphered_data)
     file_out.close()
     
     print("\n -----Texto Encriptado correctamente-----") 

 elif ans=="2":
     othrpassword = input("Ingrese el password que utilizo para encriptar los datos: ")
     if(othrpassword!=password):
         print("Password incorrecto")
     else:
         
         #Se declara el archivo base para la desencripcion. 
         input_file= 'encrypted.bin'
         file_in = open (output_file,"rb")
         #Se obtiene el vector de inicializacion
         iv= file_in.read(16)
         #Se obtiene la data cifrada
         ciphered_data = file_in.read()
         file_in.close()
         #Se declara el cifrado en modo CBC con el vector de inicializacion. 
         cipher = AES.new (key,AES.MODE_CBC, iv=iv)
         #Se obtiene el texto original luego de descifrar lo que se tenia en el archivo y luego quitar el pad que se le añadio en el paso anterior
         #--------------------------------
         #Pregunta b.iii Fue necesario hacer llegar lo siguiente:
         #La llave de encripcion en base al password para descifrar el texto
         #Indicar el modo de encripcion para seguir el parametro especifico
         #El vector de inicializacion para tener la base de la encripcion y hacerla al contrario
         #El texto cifrado para poder descifrarlo
         #El tamaño de bloque
         #--------------------------------
         original_data=unpad(cipher.decrypt(ciphered_data), AES.block_size)
         print(original_data.decode('utf-8'))

     print("\n -----Texto Desencriptado correctamente-----") 
 elif ans=="4":
     print("\n Gracias por utilizar el programa")
     exit()
 elif ans !="":
     print("\n Opion invalida, favor intente de nuevoi")





