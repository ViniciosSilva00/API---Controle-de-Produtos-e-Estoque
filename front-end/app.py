import streamlit as st
import requests

#Rodar o streamlit
# python -m streamlit run app.py

#URL da API do FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Produtos", page_icon="🛒")

st.title("🛍️ Gerenciador de Produtos")

#Menu lateral sidebar
menu = st.sidebar.radio("Navegação", ["Estoque", "Adicionar produto", "Atualizar produto", "Deletar produto"])

if menu == "Estoque":
    st.subheader("Todos os produtos 🏷️")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            for produto in produtos:
                st.write(f" **{produto['nome']}** - 💰 R$ {produto['preco']} - 📦 {produto['quantidade']} unidades")
        else:
            st.info("Nenhum produto cadastrado")
    else:
        st.error("Erro ao conectar com a API")

elif menu == "Adicionar produto":
    st.subheader("➕ Adicionar Produto")
    nome = st.text_input("Nome do produto")
    preco = st.number_input("Preço (R$)", min_value=0.0, step=0.01)
    quantidade = st.number_input("Quantidade em estoque", min_value=0, step=1)

    if st.button("Salvar produto"):
        params = {"nome": nome, "preco": preco, "quantidade": quantidade}
        response = requests.post(f"{API_URL}/produtos", params=params)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar o produto")

elif menu == "Atualizar produto":
    st.subheader("Atualizar produto")
    id_produto = st.number_input("ID do produto a atualizar", min_value=1, step=1)
    nova_qtd = st.number_input("Nova quantidade em estoque", min_value=0, step=1)
    if st.button("Atualizar"):
        dados = {"nova_qtd": nova_qtd}
        response = requests.put(f"{API_URL}/produtos/{id_produto}", params=dados)
        if response.status_code == 200:
            data = response.json()
            if "erro" in data:
                st.warning(data["erro"])
            else: 
                st.success("Produto atualizado com sucesso!")
        else:
            st.error("Erro ao atualizar produto")

elif menu == "Deletar produto":
    st.subheader("Deletar produto")
    id_produto = st.number_input("ID do produto para deletar", min_value=1, step=1)
    if st.button("Deletar"):
        dados = {"id": id_produto}
        response = requests.delete(f"{API_URL}/produtos/{id_produto}", params=dados)
        if response.status_code == 200:
            data = response.json()
            if "erro" in data:
                st.warning(data["erro"])
            else: 
                st.success("Produto deletado com sucesso!")
        else:
            st.error("Erro ao deletar produto")
