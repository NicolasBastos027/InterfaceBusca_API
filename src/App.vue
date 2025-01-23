<template>
  <div class="container">
    <h1>Empresas Encontradas</h1>

    <!-- Campo de busca -->
    <input 
      v-model="termoBusca" 
      placeholder="Pesquisar empresa (Código ANS, CNPJ, Razão Social)..." 
      @input="debouncedBuscarEmpresas" 
      :disabled="loading" 
      class="search-input"
    />

    <!-- Exibição dos resultados -->
    <p v-if="loading" class="loading">Carregando...</p>

    <!-- Caso o termo de busca tenha retornado resultados -->
    <ul v-if="empresas.length > 0 && !loading" class="results-list">
      <!-- Exibe cada empresa individualmente -->
      <li v-for="(empresa, index) in empresas" :key="index" class="result-item">
        <strong>Razão Social:</strong> {{ empresa.Razao_Social || 'Não informado' }} <br>
        <strong>Nome Fantasia:</strong> {{ empresa.Nome_Fantasia || 'Não informado' }} <br>
        <strong>CNPJ:</strong> {{ empresa.CNPJ || 'Não informado' }} <br>
        <strong>Representante:</strong> {{ empresa.Representante || 'Não informado' }} <br>
        <strong>Cargo:</strong> {{ empresa.Cargo_Representante || 'Não informado' }} <br>
        <strong>Região de Comercialização:</strong> {{ empresa.Regiao_de_Comercializacao || 'Não informado' }} <br>
        <strong>Endereço:</strong> {{ empresa.Logradouro || 'Não informado' }} {{ empresa.Numero || 'Não informado' }} <br>
        <strong>Bairro:</strong> {{ empresa.Bairro || 'Não informado' }} <br>
        <strong>Cidade:</strong> {{ empresa.Cidade || 'Não informado' }} <br>
        <strong>UF:</strong> {{ empresa.UF || 'Não informado' }} <br>
        <strong>Telefone:</strong> {{ empresa.Telefone || 'Não informado' }} <br>
        <strong>Email:</strong> {{ empresa.Endereco_eletronico || 'Não informado' }} <br>
      </li>
    </ul>

    <!-- Caso não haja resultados -->
    <p v-if="empresas.length === 0 && !loading && termoBusca.trim().length > 0" class="no-results">Nenhuma empresa encontrada.</p>

    <!-- Exibição de erros -->
    <p v-if="erroMensagem" class="error">{{ erroMensagem }}</p>
  </div>
</template>

<script>
import axios from 'axios';
import { debounce } from 'lodash';

export default {
  data() {
    return {
      empresas: [], // Dados das empresas retornados pela API
      termoBusca: "", // Termo de busca inserido pelo usuário
      loading: false, // Controle de carregamento
      erroMensagem: "", // Mensagem de erro, caso ocorra
    };
  },
  methods: {
    // Função para buscar as empresas
    async buscarEmpresas() {
      if (this.termoBusca.trim().length > 0) {  // Verifica se o termo não é vazio
        this.loading = true;
        this.erroMensagem = "";  // Limpa a mensagem de erro antes de tentar buscar
        try {
          const response = await axios.get('http://127.0.0.1:5000/buscar', {
            params: { termo: this.termoBusca },
          });

          console.log('Resposta da API:', response.data);
          console.log('Empresas encontradas:', response.data.empresas);

          // Verifica se a chave 'empresas' existe e é um array
          if (response.data && Array.isArray(response.data.empresas)) {
            this.empresas = response.data.empresas;
          } else {
            this.erroMensagem = "Nenhuma empresa encontrada.";
            this.empresas = [];  // Limpa os resultados da pesquisa caso a chave não seja encontrada ou esteja vazia
          }
        } catch (error) {
          console.error('Erro ao buscar dados:', error);
          this.erroMensagem = "Ocorreu um erro ao buscar os dados.";
        } finally {
          this.loading = false;
        }
      } else {
        // Quando o termo de busca está vazio, limpa os resultados
        this.empresas = [];
        this.erroMensagem = "";  // Limpa qualquer mensagem de erro anterior
      }
    }
  },
  created() {
    // Aguarda 500ms para disparar a busca após digitar
    this.debouncedBuscarEmpresas = debounce(this.buscarEmpresas, 500);
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Garante que ocupe toda a altura da página */
  padding: 20px;
  font-family: Arial, sans-serif;
  color: #333;
  text-align: center;
}

h1 {
  color: #0056b3;
  margin-bottom: 20px;
}

.search-input {
  width: 100%;
  max-width: 600px; /* Limita a largura da caixa de pesquisa */
  padding: 12px;
  font-size: 18px;
  border: 2px solid #0056b3;
  border-radius: 5px;
  margin-bottom: 20px;
  transition: border-color 0.3s;
}

.search-input:focus {
  border-color: #004494;
}

.loading {
  color: #0056b3;
  font-size: 18px;
}

.results-list {
  list-style-type: none;
  padding: 0;
  width: 100%;
  max-width: 600px; /* Limita a largura da lista */
}

.result-item {
  background-color: #e6f2ff;
  border: 1px solid #0056b3;
  border-radius: 5px;
  padding: 15px;
  margin-bottom: 10px;
  text-align: left;
  transition: background-color 0.3s;
}

.result-item:hover {
  background-color: #d0e1ff;
}

.no-results {
  color: #0056b3;
  font-size: 18px;
}

.error {
  color: red;
  font-weight: bold;
  margin-top: 10px;
}
</style>
