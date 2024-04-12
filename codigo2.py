import PyPDF2

def extraer_palabra(pdf_path, pagina, linea, posicion):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        page = reader.getPage(pagina)
        text = page.extractText()
        lineas = text.split('\n')
        # Ajustar índices a 0
        linea -= 1
        posicion -= 1
        try:
            palabra = lineas[linea].split()[posicion]
            return palabra
        except IndexError:
            return None

# Ejemplo de uso
pdf_path = 'quijote.pdf'
palabra1 = extraer_palabra(pdf_path, 5, 10, 3)  
palabra2 = extraer_palabra(pdf_path, 12, 4, 7)  


print("Palabra 1:", palabra1)
print("Palabra 2:", palabra2)

