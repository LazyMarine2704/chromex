![CHROMEX](https://user-images.githubusercontent.com/86082354/226200929-89bed69a-20b1-47ec-a894-c3a507ae15b5.png)

<h1>Se estiver usando linux, certifique-se de executar o programa pelo terminal com permissões de administrador</h1>

<h1>Chromex</h1>
Chromex é um programa Python que utiliza algumas bibliotecas para processar imagens capturadas pela câmera de um dispositivo e, em seguida, identificar a cor predominante na imagem utilizando uma base de dados de cores.

<h2>Funcionamento</h2>
O programa captura um frame da webcam do computador, percorre esta imagem coletando os valores RGB de cada pixel, e os adiciona em uma lista.
Após isso, o programa envia estes valores para uma função que encontra um valor rgb parecido na base de dados "color.csv".

<h2>Licensa</h2>
A Licensa do Chromex é a GNU General Public License v3.0, encontrada no arquivo <a target="_blank" href="https://github.com/LazyMarine2704/chromex/blob/main/LICENSE.txt">LICENSE</a>

Acesse o repositório em https://github.com/rubensantoniorosa2704/chromex

<h1>Sobre os pacotes</h1>

<h2>get_color_name.py</h2>
A função "getColorName(r, g, b, csv)" recebe 4 parâmetros, um valor para r, outro para g, um para b, e um valor especificando o nome de uma tabela csv, usada para correlacionar os valores rgb com os nomes respectivos da cor mais próxima. A função então realiza um cálculo para comparar o valor rgb recebido na função com o valor mais próximo na tabela, e retorna o nome da cor mais próxima na tabela.

<h2>scan_image.py</h2>
A função "scanImage(imagem, csv)" descobre todos os valores rgb dentro de um retângulo central pré-especificado. Logo após, ele calcula a média para cada valor, e os envia para a função getColorName(), para retornar o nome da cor.

<h2>rgb_list.py</h2>
A classe rgbList() inicializa as listas para os valores de cada canal rgb. A função appendNewRGB(r, g, b) apenas adiciona os parâmetros para cada lista 