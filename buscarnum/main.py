import hashlib
import re

if __name__ == "__main__":
   y = 921
   T = True
   f = open("/home/Sebastianrza/fichero1.txt", 'w')
   while T:
      inputFile = open("/home/Sebastianrza/fichero1.txt")
      readFile = inputFile.read()
      h = hashlib.sha1(readFile.encode())
      print(h.hexdigest())
      if (re.match("[0]{2}", h.hexdigest())):
         print("ganaste wey")
         print(y)
         f.close()
         T = False
      else:
         f = open("/home/Sebastianrza/fichero1.txt", 'w')
         y=y+1
         f.write('Nombre y Apellidos: Sebastian Rafael Zambrano Azuaje\n')
         f.write('Hash Previo: 008AD9491CABD7BD6291D32503647CC191EECC8F\n')
         f.write('Nonce: '+str(y))
         f.close()
         print(y)




