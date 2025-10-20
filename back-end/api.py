from fastapi import FastAPI
import funcao

#Roda fastapi = python -m uvicorn api:app --reload

#Testar as rotas no fastapi
# /docs > documentação Swagger
# /redoc > Documentação Redoc

app = FastAPI(title="Gerenciador de Produtos e Estoque")

#GET > Pegar/Listar
#POST > Enviar/Cadastrar
#PUT > Aualizar
#DELETE > Deletar

#API sempre retorna dados em JSON (Chave: Valor)

@app.get("/")
def home():
    return {"Mensagem": "Bem-vindo ao gerenciador de Produtos e Estoque"}


@app.get("/produto")
def catalogo():
    produtos = funcao.listar_produtos()
    lista = []
    for produto in produtos:
        lista.append({
            "id": produto[0],
            "nome": produto[1],
            "categoria": produto[2],
            "preço": produto[3]
        })
    return {"produtos": lista}


@app.post("/produto")
def adicionar_produto(id: str, nome: str, categoria: int, preco: float):
    funcao.criar_produto(id, nome, categoria, preco)
    return {"mensagem": "Produto adicionado com sucesso"}


@app.put("/produto/{id_produto}")
def atualizar_produto(id_produto: int, novo_preco: float):
    produto = funcao.buscar_produto(id_produto)
    if produto:
        funcao.atualizar_produto(id_produto, novo_preco)
        return {"mensagem": "Produto atualizado com sucesso!"}
    else:
        return {"erro": "Produto não encontrado"}
