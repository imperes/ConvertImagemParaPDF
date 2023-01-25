from PIL import Image
import win32com.client as win32

#### Transforma o formato PNG em PDF #### 
def imagem_png():
    image_1 = Image.open(r"imagempng.png")
    img_1 = image_1.convert('RGB')
    img_1.save(r'Documentopng_to_pdf.pdf')

#### Transforma o formato JPG em PDF #### 
def imagem_jpg():
    image_1 = Image.open(r'imagemjpg.jpg')
    img_1 = image_1.convert('RGB')
    img_1.save(r'Documentojpg_to_pdf.pdf')

#### Chama a função PNG para PDF #### 
imagem_png()

#### Chama a função JPG para PDF #### 
imagem_jpg()