![banner](https://github.com/rubensantoniorosa2704/chromex/assets/86082354/1eec9b93-7db3-46aa-a1d4-7ba6f454fd3f)

<h1>Chromex</h1>
Chromex é uma biblioteca desenvolvida em Python que processa imagens da câmera e identifica a cor predominante. Este foi um projeto criado no curso de Graduação de Sistemas de Informação. O objetivo era aplicar conceitos de visão computacional ao desenvolvimento de software e fornecer uma ferramenta para a Associação de Deficientes Visuais de Brusque (ADVB).

<h2>Aviso</h2>
Os arquivos 'app.py' e os respectivos arquivos kivy foram criados a fim de exemplificar o uso do programa, por isso, não são necessários para a execução das funções principais.

<h2>Funcionamento</h2>
O programa usa a câmera do computador para capturar uma imagem em tempo real. Ele então analisa essa imagem para determinar a cor predominante na área central. Em seguida, utiliza um arquivo CSV para associar os valores de cor a nomes de cores conhecidos e pronuncia o nome da cor predominante usando um mecanismo text-to-speech.

<h2>Licensa</h2>
A Licensa do Chromex é a GNU General Public License v3.0, encontrada no arquivo <a target="_blank" href="https://github.com/LazyMarine2704/chromex/blob/main/LICENSE.txt">LICENSE</a>

Acesse o repositório em https://github.com/rubensantoniorosa2704/chromex

<h2>Documentação</h2>
<p>Nesta versão, o propósito foi modularizar simplificar a lógica das funções já existentes. Agora, ao invés de arquivos separados, todas as funções se encontram no mesmo arquivo, dentro da classe <b>Chromex()</b>, o cerne do nosso código. A classe Chromex() leva os seguinte parâmetros: o nome do arquivo que será salvo como a captura da imagem; e o caminho para a base de dados de cores.</p>

<ul>
<li>
<h2>getColorName()</h2>
<p> A função getColorName determina o nome da cor predominante em uma imagem RGB fornecida. Ela calcula as médias dos canais de cor (vermelho, verde e azul) em uma área central da imagem, compara essas médias com uma tabela de cores e retorna o nome da cor mais próxima. Um limiar é usado para garantir correspondências precisas, e "Cor desconhecida" é retornado se nenhuma cor correspondente for encontrada.
  
        """
        Esta função recebe uma imagem capturada em formato RGB como entrada e calcula a cor predominante
        na área central da imagem. Para isso, ela divide a imagem em um retângulo central e calcula a
        média dos valores de cor (R, G, B) nessa área. Em seguida, compara esses valores com uma tabela
        de cores predefinida carregada a partir de um arquivo CSV para encontrar a cor mais próxima.

        Parâmetros:
            - image (numpy.ndarray): A imagem capturada em formato RGB.

        Retorna:
            str: O nome da cor predominante na imagem.
        """
        
</p>
</li>
  
<li>
<h2>capturarImagem()</h2>
<p> Captura e converte a imagem da câmera.
  
        """
        Captura uma imagem da câmera e a converte para o formato RGB.

        Esta função ativa a câmera do computador, captura uma imagem em tempo real e a converte para
        o formato RGB. Ela permite que o usuário visualize a imagem em uma janela, pressione a tecla 's'
        para salvar a imagem capturada no arquivo especificado e, em seguida, retorna a imagem em RGB.

        Retorna:
            numpy.ndarray: A imagem capturada em formato RGB.
        """
    
</p>
</li>

<li>
<h2>sayColorName()</h2>
<p>A classe rgbList() inicializa as listas para os valores de cada canal rgb. A função appendNewRGB(r, g, b) apenas adiciona os parâmetros para cada lista.

        """
        Diz o nome da cor usando um mecanismo text-to-speech.

        Esta função utiliza a biblioteca `pyttsx3` para pronunciar o nome da cor especificada em voz alta.
        Ela recebe o nome da cor como entrada e utiliza um mecanismo de síntese de voz para produzir a
        saída de áudio correspondente. Além disso, imprime o nome da cor no console antes de pronunciá-lo.

        Parâmetros:
            - color_name (str): O nome da cor a ser pronunciado.
        """
      
</p>
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

<h2>Perguntas Frequentes</h2>
<ul>
  <li><h3>Estou tentando executar o programa e não funciona.</h3></li>
  <p>Confira se você tem o Python instalado, e se instalou todas as dependências necessárias. Antes de rodar o programa, navegue até a pasta raiz do projeto e digite o comando: pip install requirements.txt. Se estiver executando no Linux, não esqueça de executar como sudo, pois, devido ao acesso à câmera e ao teclado, o programa requer privilégios de administrador</p>
  <li><h3>Quais são os comandos?</h3></li>
  <p>Pressione 'S' para capturar a imagem e retornar a cor em voz alta, e pressione 'Q' para sair do programa.</p>
  <li><h3>Onde encontro a documentação?</h3></li>
  <p>A documentação detalhada das funções pode ser encontrada no próprio código, além deste arquivo README.md</p>
  <br/>
</ul>

<h2>Futuramente...</h2>
<ul>
  <li>Criação de um pacote para o Python Package Index.</li>
  <li>Novas funcionalidades...</li>
</ul>

<h1>Contatos</h1>
<p>Caso precise de ajuda ou tenha algum feedback, mande um email para <a href="mailto:https://rubensrosaneto27@gmail.com">rubensrosaneto27@gmail.com</a></p>
