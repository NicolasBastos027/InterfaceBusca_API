from flask import Flask, jsonify, request  # Para criar a API e manipular as respostas HTTP
import pandas as pd  # Para ler e manipular arquivos CSV
from flask_cors import CORS  # Para permitir requisições de origens diferentes (cross-origin)
from unidecode import unidecode  # Para remover acentuação e normalizar textos

# Inicializando o aplicativo Flask
app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir requisições de outros domínios

# Função que carrega o CSV em pedaços (chunks), com um tamanho padrão de 1000 linhas por pedaço
def carregar_csv(chunk_size=1000):
    # Carrega o arquivo CSV em pedaços, o que é útil para arquivos grandes
    return pd.read_csv("Relatorio_cadop.csv", delimiter=";", on_bad_lines="skip", chunksize=chunk_size)

# Rota GET para buscar empresas com base em um termo de pesquisa
@app.route('/buscar', methods=['GET'])
def buscar_empresas():
    termo = request.args.get('termo', '').lower().strip()  # Pega o termo de busca e remove espaços extras
    empresas_com_termo = []  # Lista para armazenar as empresas que atendem ao critério de busca

    try:
        # Carrega o CSV em pedaços
        chunks = carregar_csv()

        # Itera sobre os pedaços de dados
        for chunk in chunks:
            # Normaliza todos os dados nas colunas para permitir buscas insensíveis a acentuação e caso
            for column in chunk.columns:
                # Aplica unidecode e transforma todos os dados em minúsculas
                chunk[column] = chunk[column].apply(lambda x: unidecode(str(x)).lower().strip() if isinstance(x, str) else x)

            # Busca o termo em todos os campos de cada linha
            for _, row in chunk.iterrows():
                # Verifica se o termo aparece em qualquer coluna da linha
                if any(isinstance(value, str) and termo in value for value in row):
                    empresas_com_termo.append(row.to_dict())  # Adiciona a linha (empresa) na lista

        # Remove duplicatas com base no CNPJ
        if empresas_com_termo:
            cnpjs_vistos = set()  # Conjunto para rastrear os CNPJs já vistos
            empresas_com_termo = [
                empresa for empresa in empresas_com_termo
                if empresa.get('CNPJ') not in cnpjs_vistos and not cnpjs_vistos.add(empresa.get('CNPJ'))
            ]

        # Retorna todas as empresas encontradas que correspondem ao termo de busca em formato JSON
        return jsonify({'empresas': empresas_com_termo})

    except FileNotFoundError:
        # Caso o arquivo CSV não seja encontrado
        return jsonify({"error": "O arquivo 'Relatorio_cadop.csv' não foi encontrado."}), 404
    except KeyError as e:
        # Caso falte alguma coluna no arquivo
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Captura qualquer outro erro
        return jsonify({"error": str(e)}), 500

# Inicializa o servidor Flask para rodar o aplicativo
if __name__ == '__main__':
    app.run(debug=True)
