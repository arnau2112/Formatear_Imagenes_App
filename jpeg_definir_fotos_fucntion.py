import os
import shutil
import sys
from tkinter import messagebox
from PyQt5 import QtWidgets, uic

ruta = 'C:\\Users\\ArnauSolaTatjé\\Downloads\\Imatges'
nuevo_nombre = 'Copia_Seguridad'


def calculadora_fotos(ruta, nuevo_nombre):
    ruta2 = os.path.join(ruta, nuevo_nombre)
    ruta_copiada = shutil.copytree(ruta,ruta2) 
    print(ruta_copiada)              

    x = 0
    for root, dirs, files in os.walk(ruta):
        for name in files:
            foto = (os.path.join(root, name))
            if nuevo_nombre in foto:
                print(foto)
                continue
            else:
                x += 1
                foto2 = foto.split('.')
                foto3 = os.path.join(foto2[0]+'.jpeg')
                print(foto, foto2)
                os.rename(foto, foto3)

    print(f"Proceso finalizado correctamente. Se han analizado {x} documentos")

calculadora_fotos(ruta,nuevo_nombre)

messagebox.showinfo('Informació', 'Procés finalitzat, revisa els documents.')