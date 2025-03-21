import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

# Ruta de la carpeta donde están las imágenes
folder_path = "barcodes_images"

# Obtener lista de imágenes PNG en la carpeta
image_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".png")])

# Verificar que haya imágenes
if not image_files:
    print("⚠️ No se encontraron imágenes en la carpeta")
else:
    # Parámetros del PDF
    pdf_filename = "barcodes.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    page_width, page_height = letter

    # Configurar la cuadrícula
    cols = 5  # 12 imágenes por fila
    rows = 12   # 5 filas por página
    margin_x, margin_y = 20, 20  # Márgenes más pequeños
    img_width, img_height = 100, 60  # Tamaño reducido de cada imagen
    spacing_x, spacing_y = 10, 10  # Espaciado reducido entre imágenes

    x_start = margin_x
    y_start = page_height - margin_y - img_height  # Posición inicial desde arriba

    x, y = x_start, y_start
    images_added = 0

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)

        try:
            img = ImageReader(image_path)
            c.drawImage(img, x, y, width=img_width, height=img_height)

            images_added += 1
            if images_added % cols == 0:  # Si se completó una fila
                x = x_start
                y -= img_height + spacing_y  # Mover hacia abajo
            else:
                x += img_width + spacing_x  # Mover hacia la derecha

            # Si se llenó la página, agregar una nueva
            if images_added % (cols * rows) == 0:
                c.showPage()
                x, y = x_start, y_start  # Reiniciar posiciones en nueva página

        except Exception as e:
            print(f"❌ Error al agregar {image_file}: {e}")

    c.save()
    print(f"✅ PDF generado correctamente: {pdf_filename}")
