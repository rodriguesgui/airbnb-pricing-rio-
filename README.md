# 🏡 Airbnb Pricing Rio de Janeiro

Este projeto utiliza Machine Learning para prever o preço de imóveis no Rio de Janeiro anunciados no Airbnb. Criamos um modelo com dados históricos e desenvolvemos um app interativo com Streamlit.

---

## 🚀 Funcionalidades

- Previsão de preços com base nas características do imóvel
- Interface interativa com Streamlit
- Modelo salvo com `joblib` pronto para deploy
- Dados preparados e exportados no formato `.csv`

---

## 📂 Estrutura do Projeto

airbnb-pricing-rio/
│
├── notebooks/             # Jupyter Notebooks com análise e desenvolvimento
│   └── airbnb_modelo.ipynb
│
├── dataset/               # Dados históricos para treinamento do modelo
│
├── app/                   # Aplicação em Streamlit e modelo treinado
│   ├── dados.csv          # Arquivo de dados utilizado para a previsão
│   ├── modelo.joblib      # Modelo treinado
│   └── app.py             # Código do app em Streamlit
│
└── README.md              # Documentação do projeto




📦 Como rodar o projeto localmente
1 - Clone o repositório:

    ```bash
git clone https://github.com/seu-usuario/airbnb-pricing-rio.git
cd airbnb-pricing-rio/app
    ```

2 - Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3 - Execute o app com Streamlit:

    ```bash
    streamlit run app.py
    ```

🔧 Tecnologias Utilizadas
Python: Linguagem principal.

Pandas: Manipulação de dados.

Scikit-learn: Modelo de machine learning.

Streamlit: Framework para criação de aplicativos interativos.

Joblib: Salvamento e carregamento do modelo treinado.

## Download dos Arquivos
Você pode baixar os arquivos necessários diretamente do [Google Drive] e coloque dentro da pasta dataset(https://drive.google.com/drive/folders/1pzUiazh12EwBc7Lu5L0o-4wX4g9V5ybU?usp=drive_link).

✨ Autor
Guilherme Rodrigues de Quadros
📧 Email: guilhermeddq@gmail.com
📱 LinkedIn: https://www.linkedin.com/in/guilhermedequadros/