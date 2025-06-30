from rembg import remove
from PIL import Image
import io
import datetime

img = (input("qual imagem deseja remover o fundo?"))

# Abrir imagem original
with open( img , 'rb') as input_file:
    input_data = input_file.read()

# Remover fundo
output_data = remove(input_data)

# Gerar nome único com base na data/hora atual
agora = datetime.datetime.now()
nome_saida = f"imagem-sem-fundo_{agora.strftime('%Y%m%d_%H%M%S')}.png"

# Salvar imagem com fundo removido
with open(nome_saida, 'wb') as output_file:
    output_file.write(output_data)

# Abrir imagem com fundo removido para verificar
output_image = Image.open('matue.png')
output_image.show()
print("Fundo removido com sucesso!")
