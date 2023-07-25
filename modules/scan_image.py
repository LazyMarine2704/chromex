from modules.get_color_name import getColorName

def scanImage(imagem, csv):
    height, width, channels = imagem.shape

    #Calcula o retângulo central
    central_height = int(height * 0.1)
    central_width = int(width * 0.1)
    central_top = int(height * 0.45)
    central_left = int(width * 0.45)

    #Calcula a média de cada canal no retângulo central
    r_mean = int(imagem[central_top:central_top+central_height, central_left:central_left+central_width, 0].mean())
    g_mean = int(imagem[central_top:central_top+central_height, central_left:central_left+central_width, 1].mean())
    b_mean = int(imagem[central_top:central_top+central_height, central_left:central_left+central_width, 2].mean())

    #Encontra o nome da cor no arquivo CSV
    color_name = getColorName(r_mean, g_mean, b_mean, csv)
    return color_name
