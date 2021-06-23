<div align="center">
    <h1>RA Scraper</h1>
    <hr width="50%">
    <hr>
</div>
<p>
    Um Web Scraper escrito com Selenium que extrai informações sobre uma empresa do 
    site Reclame Aqui, e gera tabelas num arquivo xlsx com elas.
</p>
<div>
    <h3>Uso</h3>
    <hr>
    <div>
        <h4>Pré-requisitos</h4>
        <hr width="20%">
        <lu>
            <li>Selenium Framework</li>
                <p>
                    Esse projeto tem como ferramenta principal o Framework Selenium, por isso é necessário sua instalação prévia para que o programa rode normalmente.
                    Para isso, você pode utilizar o gerenciador de pacotes para Python (pip), basta abrir o terminal de comandos e digitar:<br><br>
                    <img src=".Screenshots/pip_selenium.png">
                </p>
            <li>XlsxWriter Module</li>
                <p>
                    Para a criação e manipulação de arquivos Xlsx é necessário a instalação do módulo XlsxWriter.<br><br>
                    <img src=".Screenshots/pip_xlsxwriter.png">
                </p>
            <li>Google Chrome Web Browser</li>
                <p>
                    O projeto utiliza o Google Chrome (v91.0) como seu browser, por isso é necessário que ele estaja previamente instalado e na versão compatível com o WebDriver (localizado na pasta Driver). Para utilizar outras versões do Google Chrome, substitua o driver por um compatível com a versão desejada (<a href="https://chromedriver.chromium.org/downloads"> ChromeDrivers </a>).<br>
                    <strong>ATENÇÃO: Para utilizar um browser diferente, além de ser necessário que o driver seja substituido por um compatível com o browser desejado, também é necessário que sejam feitas alterações no código do ra_scraper para que o webdriver seja instanciado com a classe compatível com o browser desejado.</strong>
                </p>
        </lu>
    </div>
    <div>    
        <h4>Execução</h4>
        <hr width="20%">
        <p>
            Para iniciar o programa, utilize o Python para executar o arquivo main.py<br>
            <img src=".Screenshots/exec1.png"><br>
            Ao se executar o arquivo, sera requisitado que o usuário informe o nome de uma empresa na qual deseja realizar o scraping.<br>
            <img src=".Screenshots/exec2.png"><br>
            Assim que o nome é informado, o programa inicia a pesquisa <br>
            <img src=".Screenshots/exec3.png"><br>
            O browser é aberto e direcionado para o site "Reclame Aqui", onde é pesquisado o nome da empresa.<br>
            <img width='33%' src=".Screenshots/exec4.png">
            <img width='33%' src=".Screenshots/exec5.png">
            <img width='33%' src=".Screenshots/exec6.png"><br>
            Ao finalizar a pesquisa o browser é fechado e os resultados são passado para um arquivo xlsx no diretório "Resultados" com o mesmo nome que a empresa<br>
            <img src=".Screenshots/exec7.png"><br>
            <img width='50%' src=".Screenshots/exec8.png"><br>
            As informações no arquivo são escritas em forma de tabelas, divididas em 6 planilhas. <br>
            <img width='33%' src=".Screenshots/exec9.png">
            <img width='33%' src=".Screenshots/exec10.png">
            <img width='33%' src=".Screenshots/exec11.png">
            <img width='33%' src=".Screenshots/exec12.png">
            <img width='33%' src=".Screenshots/exec13.png">
            <img width='33%' src=".Screenshots/exec14.png">
        </p>
    </div>
</div>
<div align="center">
    <h4>Versão & Tech</h4>
    <hr>
        <img src="https://img.shields.io/badge/version-v%201.01-blueviolet"><br>
    <a href="selenium.dev">
        <img src="https://www.selenium.dev/images/selenium_logo_large.png" width="110px" >
    </a><br>
    <a href="https://www.python.org/downloads/">
        <img src="https://img.shields.io/badge/Python 3-3776AB?style=for-the-badge&logo=python&logoColor=white">
    </a>
</div>
<div align="center">
    <h4>Autor</h4>
    <hr>
    <a href="https://github.com/VitorioValer">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/82197650?s=400&u=6ad826279ad63feee1609b0eca16b47dad344cc3&v=4" width="100px;"/>
        <br>
        <b>__V__</b>
    </a>
    <br>
    <a href="https://www.linkedin.com/in/vit%C3%B3rio-valer-b752b6209/">
        <img src="https://img.shields.io/badge/-Vitorio-blue?style=flat-square&logo=Linkedin&logoColor=white">
    </a>
    <a href="mailto:vitoriovaler@gmail.com">
        <img src="https://img.shields.io/badge/-vitoriovaler@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white">
    </a>
</div>