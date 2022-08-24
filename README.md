# README

<h2><a>1. Pré-Requisitos</a></h2>

<p><b>*</b> Para instalação do projeto será preciso utilizar o Poetry, gerenciador de dependencias e pacotes.</p>

<p>O passo a passo para instalação do Poetry está neste link: <a href="https://python-poetry.org/docs/#installation">https://python-poetry.org/docs/#installation</a></p>

<p>Também será necessário Python 3.10 +</p><br>

<h2><a>2. Instalação</a></h2>

<h3>Passo a passo para instalação do projeto:</h3>

<ol>
<li>Ter o poetry instalado em sua máquina.</li>
<li>Clonar o repositório em alguma pasta de preferencia via terminal, utilizando o seguinte comando: <b>git clone https://github.com/Gustavobr20/Pharmacy-api.git</b>.</li>
<li>Dentro do terminal, na raiz do projeto, utilizar o seguinte comando: <b>poetry install</b>. Com isso ele irá criar um ambiente virtual e instalar todas as dependencias para rodar o projeto.</b></li>
<li>Verificar se o ambiente virtual está ativado, se não estiver, ativar utilizando comando: <b>poetry shell</b>.</li>
<li>Pronto, agora a API está totalmente pronta para ser utilizada :)</li>
</ol><br>

<h2><a>3. Como utilizar</a></h2>

<p>Comando para inicializar o servidor: <b>poetry run app</b>.</p>

<p>Documentação do Swagger com as rotas da API e informações, disponível neste link: <a href="127.0.0.1/docs">127.0.0.1:8000/docs</a>. É necessário estar com o servidor rodando.</p>

<p>Endpoints disponíveis</p>
<ul>
    <li><a href="#">127.0.0.1:8000/</a> (Retorna o token do usuário logado).</li>
    <li><a href="#">127.0.0.1:8000/token</a> (Gerá o Token passando os dados de login do usuário).</li>
    <li><a href="#">127.0.0.1:8000/user/create</a> (Cria um novo usuário).</li>
    <li><a href="#">127.0.0.1:8000/api/v1/patients</a> (Lista todos os pacientes cadastrados no banco de dados).</li>
    <li><a href="#">127.0.0.1:8000/api/v1/patients/?uuid=PATIENT0001</a> (Retorna o paciente filtrado pelo uuid, utilizando query params).</li>
    <li><a href="#">127.0.0.1:8000/api/v1/pharmacies</a> (Lista todas as farmácias cadastradas no banco de dados).</li>
    <li><a href="#">127.0.0.1:8000/api/v1/pharmacies/?name=DROGA MAIS</a> (Retorna os dados filtrando pelo nome da farmácia, utilizando query params).</li>
    <li><a href="#">127.0.0.1:8000/api/v1/transactions</a> (Lista todos as transações feitas pelos pacientes nas farmácias cadastradas).</li>
    <li><a href="#">127.0.0.1:8000/api/v1/transactions/?uuid_patient=PATIENT0001</a> (Retorna as transações de determinado paciente filtrado pelo uuid, utilizando query params).</li>
</ul>

<p>OBS.: Todas as rotas, exceto: <a href="#">/token</a> e <a href="#">/user/create</a>, são necessárias utilização do token de authenticação Bearer, exemplo: "Authentication": "Bearer teste123"</p>

<h3>Dentro do projeto existe a pasta chamda <b>tests</b>, nela contém alguns testes da API sendo feitos utilizando a biblioteca <b>Pytest</b></h3>
<p>Para executar os testes dentro de <b>test_app.py</b>, utilizar o comando via terminal: <b>poetry run pytest</b>.</p><br>

<h2><a>4. Sobre o projeto</a></h2>
<p>O objetivo deste projeto é, desenvolver uma API REST privada para uma empresa da área da saúde, para que o seu setor financeiro tenha acesso às informações de
compras dos pacientes/clientes da empresa / recebidas pelas farmácias.</p>