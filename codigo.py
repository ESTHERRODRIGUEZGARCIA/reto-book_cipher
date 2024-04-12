import PyPDF2

# Diccionario para mapear los números de página del PDF a los números de página del libro
mapa_paginas = {
    1: 9,   # Página 1 del PDF corresponde a la página 9 del libro
    2: 10, 
    10: 18,
    23: 31,
    30: 38,
    35: 43,
    151: 159,
    152: 160
}

def extraer_palabra(pdf_path, pagina_pdf, linea, posicion):
    # Obtener el número de página del libro
    pagina_libro = mapa_paginas[pagina_pdf]
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        page = reader.pages[pagina_pdf - 1]  # Restamos 1 para ajustar al índice base 0
        text = page.extract_text()
        print(f"Texto extraído de la página {pagina_pdf}: {text}")  # Impresión para depuración
        lineas = text.split('\n')
        print(f"Líneas en el texto extraído: {len(lineas)}")  # Impresión para depuración
        # Ajustar índices a 0
        linea -= 1
        posicion -= 1
        try:
            print(f"Palabras en la línea {linea}: {lineas[linea]}")  # Impresión para depuración
            palabra = lineas[linea].split()[posicion]
            return palabra
        except IndexError:
            return None

# Ejemplo de uso
pdf_path = 'quijote.pdf'
palabras_a_buscar = [
    ("18:9:2", 18, 9, 2),
    ("31:11:1", 31, 11, 1),
    ("38:9:2", 38, 9, 2),
    ("38:27:7", 38, 27, 7),
    ("43:2:7", 43, 2, 7),
    ("159:20:10", 159, 20, 10),
    ("159:12:8", 159, 12, 8),
    ("160:12:5", 160, 12, 5)
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
