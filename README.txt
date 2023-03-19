Chromex v.1.2

--------------------ENGLISH:
Chromex is a Python program that uses some libraries to process images captured by a device's camera and then identify the predominant color in the image using a color database.

The program is mainly composed of three parts: defining classes and functions, capturing images from the camera and processing the captured images.

In the first part of the code, two classes are defined: rgbList and getColorName, which are used later in image processing.

The rgbList class is responsible for storing a list of RGB values, allowing to calculate the average of these values ​​later.

The getColorName class is responsible for identifying the color corresponding to the RGB values ​​passed as a parameter.

Then the program imports the color database, which contains the RGB values ​​corresponding to each color.

This database is stored in a csv object, which is used later in the processing of captured images.

In the second part of the code, the program initializes the camera and starts capturing frames from the camera in an infinite loop.

The program uses the cv2 library to capture frames and display them in a window called "Chromex".

In the third part of the code, the program waits for the 's' key to be pressed.

When the 's' key is pressed, the program saves the captured image to a file, converts the image to RGB format and calls the scanImage function.

The scanImage function processes the captured image and identifies the predominant color in the image.

First, the function creates an rgbList object, which is used to store the RGB values ​​of each pixel in the image.

Then the function loops through all the pixels in the image and stores the RGB values ​​in the rgbList list.

After getting the list of RGB values ​​from the image, the function calculates the average of the RGB values ​​using the average method of the rgbList class.

Finally, the function uses the getColorName function to identify the color corresponding to the calculated RGB values ​​and returns the name of the color.

After processing the image, the program uses the pyttsx3 library to synthesize a voice that speaks the name of the predominant color in the captured image.

Finally, the program waits for the 'q' key to be pressed to end image capture and close the program.


--------------------PORTUGUESE(BR):
Chromex é um programa Python que utiliza algumas bibliotecas para processar imagens capturadas pela câmera de um dispositivo e, em seguida, identificar a cor predominante na imagem utilizando uma base de dados de cores.

O programa é composto principalmente de três partes: a definição de classes e funções, a captura de imagens da câmera e o processamento das imagens capturadas.

Na primeira parte do código, são definidas duas classes: rgbList e getColorName, que são utilizadas posteriormente no processamento das imagens.

A classe rgbList é responsável por armazenar uma lista de valores RGB, permitindo calcular a média desses valores posteriormente.

A classe getColorName é responsável por identificar a cor correspondente aos valores RGB passados como parâmetro.

Em seguida, o programa importa a base de dados de cores, que contém os valores RGB correspondentes a cada cor.

Essa base de dados é armazenada em um objeto csv, que é utilizado posteriormente no processamento das imagens capturadas.

Na segunda parte do código, o programa inicializa a câmera e começa a capturar os frames da câmera em um loop infinito.

O programa utiliza a biblioteca cv2 para capturar os frames e exibi-los em uma janela chamada "Chromex".

Na terceira parte do código, o programa aguarda pela tecla 's' ser pressionada. 

Quando a tecla 's' é pressionada, o programa salva a imagem capturada em um arquivo, converte a imagem para o formato RGB e chama a função scanImage.

A função scanImage processa a imagem capturada e identifica a cor predominante na imagem. 

Primeiro, a função cria um objeto rgbList, que é utilizado para armazenar os valores RGB de cada pixel da imagem. 

Em seguida, a função percorre todos os pixels da imagem e armazena os valores RGB na lista rgbList.

Após obter a lista de valores RGB da imagem, a função calcula a média dos valores RGB utilizando o método media da classe rgbList.

Finalmente, a função utiliza a função getColorName para identificar a cor correspondente aos valores RGB calculados e retorna o nome da cor.

Após o processamento da imagem, o programa utiliza a biblioteca pyttsx3 para sintetizar uma voz que fala o nome da cor predominante na imagem capturada.

Por fim, o programa aguarda pela tecla 'q' ser pressionada para encerrar a captura de imagens e encerrar o programa
