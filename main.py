from rembg import remove
from PIL import Image
import io
import datetime
from tkinter import Tk, filedialog


while True:
    yes_or_not = input("Deseja remover o fundo de uma imagem? (sim/nao): ").strip().lower()
    if yes_or_not != "sim":
        print('finalizando aplicação... até mais!')
        break

    # Solicitar ao usuário o caminho da imagem
    Tk().withdraw()  # Oculta a janelinha principal
    img = filedialog.askopenfilename(title="Selecione a imagem")

    # Abrir imagem original, le e quanda a informação na variavel 'input_data'
    with open( img , 'rb') as input_file:
        input_data = input_file.read()

    # Remover fundo da imagem
    output_data = remove(input_data)

    # Gerar nome único com base na data/hora atual
    agora = datetime.datetime.now()
    nome_saida = f"imagem-sem-fundo_{agora.strftime('%Y%m%d_%H%M%S')}.png"

    # Salvar imagem com fundo removido
    with open(nome_saida, 'wb') as output_file:
        output_file.write(output_data)

    # Abrir imagem com fundo removido para verificar
    output_image = Image.open(nome_saida)
    output_image.show()
    print("Fundo removido com sucesso!")
