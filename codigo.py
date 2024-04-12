import PyPDF2

def extract_words_with_offset(pdf_path, coordinates, page_offset):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        result = []
        
        for coordinate in coordinates:
            parts = coordinate.split(':')
            page_num = int(parts[0]) + page_offset  # Ajuste del desplazamiento
            line_num = int(parts[1])
            word_pos = int(parts[2])
            
            try:
                page = reader.pages[page_num - 1]
                text = page.extract_text()
                
                if not text:
                    result.append("TextoNoExtraído")
                    continue
                
                lines = text.split('\n')
                
                if line_num <= len(lines):
                    line = lines[line_num - 1]
                    words = line.split()
                    
                    if word_pos <= len(words):
                        result.append(words[word_pos - 1])
                    else:
                        result.append("PalabraNoEncontrada")
                else:
                    result.append("LíneaNoEncontrada")
            except IndexError:
                result.append("PáginaNoEncontrada")
                
        return '_'.join(result)

# Asumiendo que las primeras 3 páginas no se cuentan en las coordenadas proporcionadas
page_offset = 8

# Coordenadas del formato "página:línea:posición"
coordinates = ["10:8:2", "23:10:1", "30:8:2", "30:26:7", "35:1:7", "151:19:10", "151:11:8", "152:11:5"]

# Llamar a la función y pasar el path del PDF, las coordenadas y el desplazamiento
words = extract_words_with_offset("quijote.pdf", coordinates, page_offset)
print(words)
