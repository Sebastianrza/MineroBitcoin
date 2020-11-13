import hashlib
import re

if __name__ == "__main__":
   nonce = 0
   T = True
   file = open("ruta fichero")
   while T:
      inputFile = open("ruta fichero")
      readFile = inputFile.read()
      hash = hashlib.sha1(readFile.encode())
      print(hash.hexdigest())
      if (re.match("[0]{2}", hash.hexdigest())):
         print(nonce)
         file.close()
         T = False
      else:
         file = open("ruta fichero", 'w')
         nonce=nonce+1
         file.write('Nombre y Apellidos: \n')
         file.write('Hash Previo: ******************(si lo hay)***************\n')
         file.write('Nonce: '+str(nonce))
         file.close()
       




