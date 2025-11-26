import os
import shutil

ruta = 'C:\\Users\\ArnauSolaTatjé\\Downloads\\Imatges'
nuevo_nombre = 'Copia_Seguridad'
ruta2 = os.path.join(ruta, nuevo_nombre)
ruta_copiada = shutil.copytree(ruta,ruta2) 
print(ruta_copiada)              


for root, dirs, files in os.walk(ruta):
   for name in files:
      foto = (os.path.join(root, name))
      if nuevo_nombre in foto:
         print(foto)
         continue
      else:
         foto2 = foto.split('.')
         foto3 = os.path.join(foto2[0]+'.jpeg')
         print(foto, foto2)
         os.rename(foto, foto3)

