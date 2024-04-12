import PyPDF2

def extraer_palabra(pdf_path, pagina_pdf, linea, posicion):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        page = reader.pages[pagina_pdf - 1]  # Restamos 1 para ajustar al índice base 0
        text = page.extract_text()
        #print(f"Texto extraído de la página {pagina_pdf}: {text}")  # Impresión para depuración
        lineas = text.split('\n')
        #print(f"Líneas en el texto extraído: {len(lineas)}")  # Impresión para depuración
        # Ajustar índices a 0
        linea -= 1
        posicion -= 1
        try:
            #print(f"Palabras en la línea {linea}: {lineas[linea]}")  # Impresión para depuración
            palabra = lineas[linea].split()[posicion]
            return palabra
        except IndexError:
            return None

# Ejemplo de uso
pdf_path = 'quijote.pdf'
palabras_a_buscar = [
    ("18:9:2", 18, 9, 2),
    ("33:13:1", 33, 13, 1),
    ("40:9:2", 40, 9, 2),
    ("40:27:7", 40, 27, 7),
    ("45:2:7", 45, 2, 7),
    ("163:20:10", 163, 20, 10),
    ("163:12:8", 163, 12, 8),
    ("164:12:5", 164, 12, 5)
]

palabras_encontradas = []
for palabra_info in palabras_a_buscar:
    coordenadas, pagina, linea, posicion = palabra_info
    palabra = extraer_palabra(pdf_path, pagina, linea, posicion)
    if palabra:
        palabras_encontradas.append(palabra)

# Concatenar las palabras encontradas
mensaje_oculto = '_'.join(palabras_encontradas)
print("Mensaje oculto:", mensaje_oculto)
