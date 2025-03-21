import barcode
import os
import random
from barcode.writer import ImageWriter

# Carpeta para guardar los códigos de barras como imágenes
IMAGE_FOLDER = "barcodes_images"

# Crear carpeta de imágenes si no existe
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

# Función para generar códigos únicos
def generate_unique_codes(count=80):
    new_codes = set()
    ean13 = barcode.get_barcode_class("ean13")

    while len(new_codes) < count:
        code = str(random.randint(10**11, 10**12 - 1))  # 12 dígitos aleatorios
        new_codes.add(code)  # Sin verificar duplicados, ya que son nuevos códigos siempre

    return list(new_codes)

# Crear códigos de barras y guardarlos como imágenes
def create_barcode_images(codes):
    image_files = []
    for code in codes:
        ean = barcode.get_barcode_class("ean13")
        ean_instance = ean(code, writer=ImageWriter())
        file_path = os.path.join(IMAGE_FOLDER, f"{code}.png")  # Ruta absoluta
        ean_instance.save(file_path)
        if os.path.exists(file_path):
            print(f"✅ Imagen creada: {file_path}")
            image_files.append(file_path)
        else:
            print(f"⚠️ ERROR: No se creó la imagen {file_path}")
    return image_files

# Ejecutar el programa
codes = generate_unique_codes()
print(f"📌 {len(codes)} códigos generados.")

images = create_barcode_images(codes)
if not images:
    print("❌ ERROR: No se generaron imágenes. Revisa posibles problemas.")

# Limpiar imágenes generadas al final de la ejecución
print("🎉 Proceso de generación completado. Las imágenes están en la carpeta:", IMAGE_FOLDER)
