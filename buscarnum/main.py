import hashlib
import re

if __name__ == "__main__":
   nonce = 0
   T = True
   file = open("/home/Sebastianrza/fichero1.txt", 'w')
   while T:
      inputFile = open("/home/Sebastianrza/fichero1.txt")
      readFile = inputFile.read()
      hash = hashlib.sha1(readFile.encode())
      print(hash.hexdigest())
      if (re.match("[0]{2}", hash.hexdigest())):
         print(nonce)
         file.close()
         T = False
      else:
         file = open("/home/Sebastianrza/fichero1.txt", 'w')
         nonce=nonce+1
         file.write('Nombre y Apellidos: Sebastian Rafael Zambrano Azuaje\n')
         file.write('Hash Previo: 008AD9491CABD7BD6291D32503647CC191EECC8F\n')
         file.write('Nonce: '+str(nonce))
         file.close()
       




