from rembg import remove
from PIL import Image
import io

# Abrir imagem original
with open('matue.jpg', 'rb') as input_file:
    input_data = input_file.read()

# Remover fundo
output_data = remove(input_data)

# Salvar imagem com fundo removido
with open('matue.png', 'wb') as output_file:
    output_file.write(output_data)

# Abrir imagem com fundo removido para verificar
output_image = Image.open('matue.png')
output_image.show()
print("Fundo removido com sucesso!")
