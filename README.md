# Sistema de Busca de Empresas com API e Interface Web

Este projeto consiste em um sistema de busca de empresas com base em dados de um arquivo CSV, desenvolvido utilizando Python para o servidor e Vue.js para a interface web. O sistema permite que os usuários realizem buscas pelo nome (razão social) das empresas, e os resultados são exibidos na interface web.

## Componentes do Projeto:

- Servidor Python (API): Utiliza o framework Flask para criar a API que lida com as requisições de busca. A API lê os dados de um arquivo CSV contendo informações sobre empresas de saúde e realiza buscas com base no termo inserido pelo usuário.

- Interface Web Vue.js: A interface web foi construída utilizando Vue.js com a Options API. Ela permite que os usuários pesquisem empresas e exibam os resultados de forma intuitiva.

## Funcionalidades:

- Barra de pesquisa: Permite ao usuário inserir um termo de busca (pode ser o nome da empresa, CNPJ ou Código ANS) e realiza a consulta ao servidor.
- Exibição dos resultados: Mostra uma lista com as informações das empresas encontradas, incluindo Código ANS, CNPJ e Razão Social.
- Comunicação entre Frontend e Backend: A interface web se comunica com o servidor Python via requisições HTTP para realizar a busca.

## Tecnologias Utilizadas:

### Servidor Python:
- Flask: Framework web para criação da API.
- Flask-Cors: Para lidar com CORS (Cross-Origin Resource Sharing).
- csv: Para ler e processar os dados do arquivo CSV.

### Interface Web Vue.js:

- Vue.js: Framework JavaScript utilizado para construir a interface web.
- HTML e CSS: Para estruturar e estilizar a interface de forma simples e eficiente.


### Estrutura da Interface:
A interface em Vue.js é baseada na Options API, que permite uma estrutura clara e simples. A interface é composta por:

- Campo de busca: O usuário pode digitar um termo para buscar empresas no banco de dados.
- Resultados: A lista de empresas é exibida com informações como Razão Social, Nome Fantasia, CNPJ, Representante, entre outras.
- Mensagens de erro e carregamento: Exibe mensagens informando o status da busca, como "Carregando..." ou "Nenhuma empresa encontrada".

### Dados:
- termoBusca: Armazena o termo inserido pelo usuário na barra de pesquisa.
- empresas: Armazena a lista de empresas retornadas pela API após a busca.
- erroMensagem: Armazena qualquer mensagem de erro, como falhas na comunicação com o servidor ou falta de resultados.

### Métodos:
- buscarEmpresas: Realiza a requisição HTTP para a API com o termo de busca e atualiza a lista de empresas exibidas.
- debouncedBuscarEmpresas: Utiliza a função de debouncing (com 500ms de delay) para otimizar as buscas e evitar requisições excessivas enquanto o usuário digita.

## Instruções de Instalação:

- Primeiramente clone o repositório
```bash
git clone https://github.com/NicolasBastos027/InterfaceBusca_API.git]
```
### Siga as instruções abaixo para configurar o ambiente de desenvolvimento:

### Servidor Python:

- Instale o Python (versão 3.6 ou superior).
- Instale as dependências com o comando:
```bash
pip install flask flask-cors
```
```bash
pip install Flask
```
```bash
pip install pandas
```
```bash
pip install unidecode
```

- Execute o servidor:
```bash
python server.py
```
O servidor estará rodando na porta http://localhost:3000/.

## Interface Web Vue.js:

- Instale o Node.js (versão 14 ou superior).
- Navegue até o diretório da interface web:

Instale as dependências com:
```bash
npm install
```
Inicie o servidor de desenvolvimento com:
```bash
npm run dev
```

## Screenshots

### Interface WEB

![Interface WEB](https://github.com/NicolasBastos027/InterfaceBusca_API/blob/main/abertta.png)

### Resposta do Servidor

![Código de respota do servidor](https://github.com/NicolasBastos027/InterfaceBusca_API/blob/main/resposta%20servidor.png)

### Resposta do Console

![Resposta do console](https://github.com/NicolasBastos027/InterfaceBusca_API/blob/main/empresa%20encontrada.png)

## Licença

