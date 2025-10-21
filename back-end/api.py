from fastapi import FastAPI, HTTPException
import funcao

app = FastAPI(title="API Controle de Produtos e Estoque")

# -------------------- Adicionar Produto --------------------
@app.post("/produtos")
def criar_produto(nome: str, categoria: str = "", preco: float = 0, quantidade: int = 0):
    resultado = funcao.adicionar_produto(nome, categoria, preco, quantidade)
    if "erro" in resultado:
        raise HTTPException(status_code=500, detail=resultado["erro"])
    return resultado

# -------------------- Listar Produtos --------------------
@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produtos()
    return {"produtos": produtos}

# -------------------- Atualizar Produto --------------------
@app.put("/produtos/{id}")
def atualizar_produto(
    id: int,
    nome: str = None,
    categoria: str = None,
    preco: float = None,
    quantidade: int = None
):
    resultado = funcao.atualizar_produto(id, nome, categoria, preco, quantidade)
    if "erro" in resultado:
        raise HTTPException(status_code=500, detail=resultado["erro"])
    return resultado

# -------------------- Excluir Produto --------------------
@app.delete("/produtos/{id}")
def excluir_produto(id: int):
    resultado = funcao.excluir_produto(id)
    if "erro" in resultado:
        raise HTTPException(status_code=500, detail=resultado["erro"])
    return resultado

# -------------------- Valor Total do Estoque --------------------
@app.get("/produtos/valor_total")
def valor_total_estoque():
    resultado = funcao.valor_total_estoque()
    if "erro" in resultado:
        raise HTTPException(status_code=500, detail=resultado["erro"])
    return resultado