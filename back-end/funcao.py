from conexao import conectar

def adicionar_produto(nome, categoria, preco, quantidade):
    conn = conectar()
    if not conn:
        return {"erro": "Não foi possível conectar ao banco de dados"}

    cursor = conn.cursor()
    sql = "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nome, categoria, preco, quantidade))
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensagem": "Produto adicionado com sucesso"}


