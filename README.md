![CHROMEX (1)](https://github.com/rubensantoniorosa2704/chromex/assets/86082354/c8521e66-14f0-4584-845e-415ebfe38dc3)

<h1>Chromex</h1>
Chromex é um programa Python que utiliza algumas bibliotecas para processar imagens capturadas pela câmera de um dispositivo e, em seguida, identificar a cor predominante na imagem utilizando uma base de dados.

<h2>Funcionamento</h2>
O programa captura um frame da webcam do computador, percorre esta imagem coletando os valores RGB de cada pixel, e os adiciona em uma lista.
Após isso, o programa envia estes valores para uma função que encontra um valor rgb parecido na base de dados "color.csv".

<p><b>Se estiver usando linux, certifique-se de executar o programa pelo terminal com permissões de administrador</b></p>

<h2>Licensa</h2>
A Licensa do Chromex é a GNU General Public License v3.0, encontrada no arquivo <a target="_blank" href="https://github.com/LazyMarine2704/chromex/blob/main/LICENSE.txt">LICENSE</a>

Acesse o repositório em https://github.com/rubensantoniorosa2704/chromex

<h2>Sobre os pacotes</h2>
<h4>Os arquivos do programa foram organizados em módulos para facilitar a manutenção e o compreendimento.</h4>

<ul>
<li>
<h2>get_color_name.py</h2>
<p> A função "getColorName(r, g, b, csv)" recebe 4 parâmetros, um valor para r, outro para g, um para b, e um valor especificando o nome de uma tabela csv, usada para correlacionar os valores rgb com os nomes respectivos da cor mais próxima. A função então realiza um cálculo para comparar o valor rgb recebido na função com o              valor mais próximo na tabela, e retorna o nome da cor mais próxima na tabela.
</p>
</li>
  
<li>
<h2>scan_image.py</h2>
<p>A função "scanImage(imagem, csv)" descobre todos os valores rgb dentro de um retângulo central pré-especificado. Logo após, ele calcula a média para cada valor, e os envia para a função getColorName(), para retornar o nome da cor.
</p>
</li>

<li>
<h2>rgb_list.py</h2>
<p>A classe rgbList() inicializa as listas para os valores de cada canal rgb. A função appendNewRGB(r, g, b) apenas adiciona os parâmetros para cada lista.</p>
</li>
</ul>

<h2>Contribuição</h2>
<h4>Deseja contribuir com o projeto? Fique atento às orientações abaixo!</h4>
<ul>
  <li>Comece com um issue aberto: precisamos da sua ajuda para resolver bugs, ou mesmo para aprimorar a documentação! Iniciantes são bem vindos, procure pela tag "good first issue" para saber onde começar.</li>
  
  <li>Crie um fork do projeto. Isso criará uma cópia do repositório original em sua conta do GitHub.</li><br>
  <img width="449" alt="capturar2" src="https://github.com/rubensantoniorosa2704/chromex/assets/86082354/304d1f64-4118-4e2d-a4eb-7ded21ddf3af"><br>
  
  <li>Clone o repositório: vá para o repositório recém-forked e copie o URL do repositório. Em sua máquina local, abra um terminal e execute o seguinte comando para clonar o repositório em sua máquina:
  </li><br>
  <img width="442" alt="Capturar" src="https://github.com/rubensantoniorosa2704/chromex/assets/86082354/d1bc1e30-5f80-4d4f-92b6-f3a193129881"><br>

  <li>Crie um branch: Isso manterá seu trabalho isolado do branch principal. </li><br>
  <img width="267" alt="Capturar" src="https://github.com/rubensantoniorosa2704/chromex/assets/86082354/388b2b72-da65-4f0a-8e46-519ae39772ce"><br>

  <li>Agora já podemos por a mão na massa! Faça as alterações necessárias, e salve-as usando os comandos git add e git commit</li><br>
  <img width="286" alt="Capturar" src="https://github.com/rubensantoniorosa2704/chromex/assets/86082354/549c9c74-6f14-4573-b349-2d3e45a74c8c"><br>

  <li>Sincronize com o repositório original: antes de enviar suas alterações, lembre-se de sincronizar seu fork com o repositório original. Os seguintes comandos servem para definir o repositório remoto e sincronizar os seus arquivos com o repositório original</li><br>
  <img width="428" alt="Capturar" src="https://github.com/rubensantoniorosa2704/chromex/assets/86082354/a23590bb-69f8-4759-bfd8-0bc8cc3ca5dc"><br>
  
  <li>Subir alterações. Agora é hora de subir o que você criou para o repositório remoto. Para isso, use o seguinte comando:</li><br>
  <img width="218" alt="Capturar" src="https://github.com/rubensantoniorosa2704/chromex/assets/86082354/93fda74e-4457-4d8a-a11c-0a1c3cdd6095"><br>

  <li>Crie um pull request: Vá para a página do seu fork no GitHub e clique no botão "Compare & pull request" (Comparar e abrir um pull request). Preencha as informações necessárias, incluindo uma descrição clara do que você fez nas alterações.</li>
  
  <li>Espere pelo feedback dos mantenedores, e depois que o pull request for aceito e mesclado (merged) no projeto original, sincronize seu fork com o projeto principal usando o comando "git pull upstream main"</li>
</ul>

<h3>Parabéns!</h3>
<p>Você contribuiu com sucesso para o projeto! Agradecemos imensamente pelo seu apoio até aqui. S2</p>

<h1>Contatos</h1>
<p>Caso precise de ajuda ou tenha algum feedback, mande um email para <a href="mailto:https://rubensrosaneto27@gmail.com">rubensrosaneto27@gmail.com</a></p>
