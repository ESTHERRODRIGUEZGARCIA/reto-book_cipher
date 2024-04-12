import PyPDF2

def extract_words(pdf_path, coordinates):
    # Abrir el archivo PDF
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        result = []
        
        for coordinate in coordinates:
            page_num, line_num, word_pos = map(int, coordinate.split(':'))
            
            # Obtener la página específica y extraer el texto
            page = reader.pages[page_num - 1]
            text = page.extract_text()
            
            # Dividir el texto en líneas y luego en palabras
            lines = text.split('\n')
            line = lines[line_num - 1]
            words = line.split()
            
            # Agregar la palabra específica a los resultados
            # Verificar primero si la línea y la palabra existen
            if word_pos <= len(words):
                result.append(words[word_pos - 1])
            else:
                result.append("PalabraNoEncontrada")
                
        # Unir las palabras extraídas con un guión bajo
        return '_'.join(result)

# Coordenadas del formato "página:línea:posición"
coordinates = ["1:5:3", "2:3:1", "3:4:2"]

# Llamar a la función y pasar el path del PDF y las coordenadas
words = extract_words("quijote.pdf", coordinates)
print(words)
