from PIL import Image

def imagem_png():
    image_1 = Image.open(r"\ConvertImagemParaPDF\imagem1.jpg")
    img_1 = image_1.convert('RBG')
    img_1.save(r'\ ConvertImagemParaPDF\ imagem1.pdf')
    
def imagem_jpg():
    image_1 = Image.open(r'C:\Usuários\Gabriel Peres\Documentos\Estudos\python\ConvertImagemParaPDF\imagem1.jpg')
    img_1 = image_1.convert('RBG')
    img_1.save(r'\ ConvertImagemParaPDF\ imagem1.pdf')
    
imagem_png()