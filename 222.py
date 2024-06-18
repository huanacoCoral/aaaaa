import cv2
from matplotlib import pyplot as plt
from google.colab import drive
from scipy.sparse import csr_matrix

# Montar Google Drive
drive.mount('/content/drive')

# Rutas a las imágenes en Google Drive
ruta_imagen1 = "/content/drive/My Drive/317/rata.png"
ruta_imagen2 = "/content/drive/My Drive/317/pato.png"

# Cargar la primera imagen en escala de grises
imagen1 = cv2.imread(ruta_imagen1, cv2.IMREAD_GRAYSCALE)
if imagen1 is None:
    print("Error al cargar la imagen 1. Verifica la ruta del archivo.")
else:
    # Redimensionar la primera imagen
    imagen1_redimensionada = cv2.resize(imagen1, (200, 200))
    
# Cargar la segunda imagen en escala de grises
imagen2 = cv2.imread(ruta_imagen2, cv2.IMREAD_GRAYSCALE)
if imagen2 is None:
    print("Error al cargar la imagen 2. Verifica la ruta del archivo.")
else:
    # Redimensionar la segunda imagen
    imagen2_redimensionada = cv2.resize(imagen2, (200, 200))

# Verificar si ambas imágenes se han cargado y redimensionado correctamente
if imagen1 is not None and imagen2 is not None:
    # Asegurar que ambas imágenes tengan las mismas dimensiones
    if imagen1_redimensionada.shape == imagen2_redimensionada.shape:
        # Convertir ambas imágenes a color (3 canales)
        imagen1_color = cv2.cvtColor(imagen1_redimensionada, cv2.COLOR_GRAY2BGR)
        imagen2_color = cv2.cvtColor(imagen2_redimensionada, cv2.COLOR_GRAY2BGR)

        # Superponer imagen2 sobre imagen1 usando addWeighted
        alpha = 0.5  # Transparencia para imagen1
        beta = 1 - alpha  # Transparencia para imagen2
        imagen_superpuesta = cv2.addWeighted(imagen1_color, alpha, imagen2_color, beta, 0)

        # Mostrar la imagen superpuesta
        plt.imshow(cv2.cvtColor(imagen_superpuesta, cv2.COLOR_BGR2RGB))
        plt.title("Imagen superpuesta")
        plt.axis('off')  # Para desactivar los ejes
        plt.show()

        imagen_concatenada = cv2.hconcat([imagen1_color, imagen2_color])

        # Mostrar la imagen concatenada
        plt.imshow(cv2.cvtColor(imagen_concatenada, cv2.COLOR_BGR2RGB))
        plt.title("Imagen 1 y 2 concatenadas")
        plt.axis('off')  # Para desactivar los ejes
        plt.show()

        # Convertir las imágenes a matrices binarias
        _, imagen1_binaria = cv2.threshold(imagen1_redimensionada, 127, 1, cv2.THRESH_BINARY)
        _, imagen2_binaria = cv2.threshold(imagen2_redimensionada, 127, 1, cv2.THRESH_BINARY)

        # Convertir las matrices binarias en matrices dispersas
        matriz_sparce1 = csr_matrix(imagen1_binaria)
        matriz_sparce2 = csr_matrix(imagen2_binaria)

        # Imprimir las matrices dispersas
        print("Matriz sparce de la imagen 1:")
        print(matriz_sparce1)
        print("\nMatriz sparce de la imagen 2:")
        print(matriz_sparce2)
        
    else:
        print("Las imágenes no tienen las mismas dimensiones después de redimensionar.")
else:
    print("Una o ambas imágenes no se han cargado correctamente.")
