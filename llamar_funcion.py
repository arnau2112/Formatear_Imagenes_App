import sys
from PyQt5 import QtWidgets, uic
#librerias importadas por mi
import os
from PyQt5.QtWidgets import  QFileDialog
import shutil
import sys
from tkinter import messagebox
import img2pdf
from PIL import Image

# Cargar el archivo .ui directamente
class MiVentana(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\IP_DIARI\000_Repositori_Arnau\001_Repositori_Scripts_Python\001_JPEG_DEFINIR_FOTOS\interfac_grafica.ui", self)  # Aquí cargas tu interfaz

          # Conectar el botón a una función
        self.buttonBox.accepted.connect(self.mostrar_texto)
        #provando
        self.pushButton.clicked.connect(self.select_output_folder)

        self.comboBox.addItems([".png",".jpeg",".PDF"])

        self.folder_path = None
        
    def mostrar_texto(self):
        # Obtener el texto del QLineEdit
        texto = self.lineEdit.text()
        formato = self.comboBox.currentText()
        print(texto)
        print(formato)

        self.calculadora_fotos(texto, formato)


    #provando2
    def select_output_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self, "Selecciona la carpeta con los documentos", "")
        if folder:
            self.lineEdit_2.setText(folder)
            self.folder_path = folder
            print(self.folder_path)


    def calculadora_fotos(self, nuevo_nombre, formato):
        ruta = self.folder_path
        print(nuevo_nombre)
        print(formato)
        ruta2 = os.path.join(ruta, nuevo_nombre)

        try:
            ruta_copiada = shutil.copytree(ruta,ruta2) 
            print(ruta_copiada)   
        except:
            messagebox.showwarning('Informació', 'Ja hi ha una altre subcarpeta amb el mateix nom')     
            return      

        x = 0
        for root, dirs, files in os.walk(ruta):
            for name in files:
                foto = (os.path.join(root, name))
                print(foto)
                if nuevo_nombre in foto:
                    print(foto)
                    continue
                if formato != '.PDF':
                    x += 1
                    foto2 = foto.split('.')
                    foto3 = os.path.join(foto2[0]+formato)
                    print(foto, foto2)
                    os.rename(foto, foto3)
                if formato == '.PDF':
                    x += 1
                    foto2 = foto.split('.')
                    foto3 = os.path.join(foto2[0]+formato)
                    image = Image.open(foto)
                    pdf_bytes = img2pdf.convert(image.filename)
                    file = open(foto3, "wb")
                    file.write(pdf_bytes)
                    image.close()
                    file.close()
                    os.remove(foto)


        print(f"Proceso finalizado correctamente. Se han analizado {x} documentos")
        messagebox.showinfo('Informació', 'Procés finalitzat, revisa els documents.')

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())