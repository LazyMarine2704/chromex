from packages.get_color_name import getColorName

def scanImage(imagem, csv):
    height, width, channels = imagem.shape
    print(height, width, channels)

    # Calculate central rectangle
    central_height = int(height * 0.1)
    central_width = int(width * 0.1)
    central_top = int(height * 0.45)
    central_left = int(width * 0.45)

    # Calculate the mean of each channel in the central rectangle
    r_mean = int(imagem[central_top:central_top+central_height, central_left:central_left+central_width, 0].mean())
    g_mean = int(imagem[central_top:central_top+central_height, central_left:central_left+central_width, 1].mean())
    b_mean = int(imagem[central_top:central_top+central_height, central_left:central_left+central_width, 2].mean())

    # Get the color name from the CSV file
    color_name = getColorName(r_mean, g_mean, b_mean, csv)
    print(color_name, r_mean, g_mean, b_mean)

    return color_name
