📋 Validação de Documentos com Azure
Um sistema de validação de documentos desenvolvido em Python usando Streamlit e serviços Azure para análise e reconhecimento de cartões de crédito.

🚀 Funcionalidades
Upload de documentos: Suporte a arquivos PDF, PNG, JPG e JPEG

Armazenamento em nuvem: Integração com Azure Blob Storage

Reconhecimento inteligente: Uso do Azure AI Document Intelligence para extrair informações de cartões de crédito

Interface amigável: Dashboard interativo com Streamlit

Validação em tempo real: Análise instantânea dos documentos enviados

🛠️ Tecnologias Utilizadas
Python 3.x

Streamlit - Interface web

Azure Blob Storage - Armazenamento de arquivos

Azure AI Document Intelligence - OCR e análise de documentos

Azure Core SDK - Integração com serviços Azure

📦 Instalação
Pré-requisitos
Python 3.8+

Conta Azure com os seguintes serviços:

Azure Blob Storage

Azure AI Document Intelligence

Configuração
Clone o repositório:

bash
git clone <url-do-repositorio>
cd azureprojeto2
Instale as dependências:

bash
pip install -r requirements.txt
Configure as variáveis de ambiente:
Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

env
AZURE_STORAGE_CONNECTION_STRING=sua_string_de_conexao_azure_storage
CONTAINER_NAME=nome_do_seu_container
ENDPOINT=seu_endpoint_azure_ai
API_KEY=sua_chave_api_azure_ai
Execute a aplicação:

bash
streamlit run src/app.py
🏗️ Estrutura do Projeto

text

azureprojeto2/
├── src/
│   ├── app.py                 # Aplicação principal Streamlit
│   ├── services/
│   │   ├── blob_service.py    # Serviço de upload para Azure Blob
│   │   └── credit_card_service.py # Serviço de análise de cartões
│   └── utils/
│       └── Config.py          # Configurações e variáveis de ambiente
├── requirements.txt           # Dependências do projeto
└── README.md                 # Documentação

🔧 Configuração Azure
Azure Blob Storage
Crie uma Storage Account no Azure Portal

Crie um container para armazenar os documentos

Obtenha a string de conexão no menu "Access Keys"

Azure AI Document Intelligence
Crie um recurso de Document Intelligence no Azure Portal

Ative o modelo "prebuilt-creditCard"

Obtenha o endpoint e a chave API nas configurações do recurso

📋 Como Usar
Inicie a aplicação:

bash
streamlit run src/app.py
Acesse a interface:
Abra o navegador em http://localhost:8501

Faça upload de um documento:

Clique em "Escolha um arquivo pdf ou Imagem"

Selecione um arquivo de cartão de crédito (PDF, PNG, JPG, JPEG)

Visualize os resultados:

O sistema fará upload para o Azure Blob Storage

Processará o documento com Azure AI Document Intelligence

Exibirá as informações extraídas do cartão

🎯 Funcionalidades de Análise
O sistema extrai as seguintes informações dos cartões de crédito:

✅ Nome no Cartão (Card Holder Name)

✅ Número do Cartão (Card Number)

✅ Banco Emissor (Issuing Bank)

✅ Data de Validade (Expiration Date)

🔒 Segurança
As credenciais Azure são armazenadas em variáveis de ambiente

Os arquivos são armazenados de forma segura no Azure Blob Storage

As análises são processadas pelos serviços Azure com criptografia

🐛 Solução de Problemas
Erros Comuns
"Connection string not found"

Verifique se o arquivo .env está configurado corretamente

Confirme se as variáveis de ambiente estão acessíveis

"Container does not exist"

Certifique-se de que o container especificado existe no Azure Blob Storage

"Invalid API key"

Verifique se a chave API do Azure AI Document Intelligence está correta

Confirme se o recurso está ativo na Azure

Logs e Debug
A aplicação inclui mensagens de debug detalhadas para ajudar na identificação de problemas durante o desenvolvimento.

📄 Licença
Este projeto é para fins educacionais e de demonstração.

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

📞 Suporte
Para dúvidas ou problemas:

Verifique a documentação do Azure

Consulte os logs da aplicação

Abra uma issue no repositório

Desenvolvido com ❤️ usando Azure Services e Python
