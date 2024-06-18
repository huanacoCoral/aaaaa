#3
import cv2
from matplotlib import pyplot as plt
from google.colab import drive

# Montar Google Drive
drive.mount('/content/drive')

# Rutas a las imágenes en Google Drive
ruta_imagen1 = "/content/drive/My Drive/317/rata.png"
ruta_imagen2 = "/content/drive/My Drive/317/pato.png"

# Cargar la primera imagen
imagen1 = cv2.imread(ruta_imagen1)
imagen1_redimensionada = cv2.resize(imagen1, (200, 200))
imagen2_redimensionada = cv2.resize(imagen2, (200, 200))
suma_imagenes = cv2.add(imagen1_redimensionada, imagen2_redimensionada)
resta_imagenes = cv2.subtract(imagen1_redimensionada, imagen2_redimensionada)


plt.subplot(1, 3, 3)
plt.imshow(suma_imagenes, cmap='gray')
plt.title("Suma de Imágenes")
plt.show()

plt.figure(figsize=(5, 5))
plt.imshow(resta_imagenes, cmap='gray')
plt.title("Resta de Imágenes")
plt.axis('off')  # Para desactivar los ejes
plt.show()
