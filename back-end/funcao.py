from conexao import conectar

def adicionar_produto(nome, categoria, preco, quantidade):
    conn = conectar()
    if not conn:
        return {"erro": "Não foi possível conectar ao banco de dados"}

    try:
        cursor = conn.cursor()
        sql = "INSERT INTO produto (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, categoria, preco, quantidade))
        conn.commit()
        return {"mensagem": "Produto adicionado com sucesso"}
    except Exception as e:
        return {"erro": str(e)}
    finally:
        cursor.close()
        conn.close()

def listar_produtos():
    conn = conectar()
    if not conn:
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produto")
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print(f"Erro ao listar produtos: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def atualizar_produto(id, nome=None, categoria=None, preco=None, quantidade=None):
    conn = conectar()
    if not conn:
        return {"erro": "Não foi possível conectar ao banco de dados"}

    try:
        cursor = conn.cursor()
        campos = []
        valores = []

        if nome is not None:
            campos.append("nome=%s")
            valores.append(nome)
        if categoria is not None:
            campos.append("categoria=%s")
            valores.append(categoria)
        if preco is not None:
            campos.append("preco=%s")
            valores.append(preco)
        if quantidade is not None:
            campos.append("quantidade=%s")
            valores.append(quantidade)

        if not campos:
            return {"erro": "Nenhum campo para atualizar"}

        valores.append(id)
        sql = f"UPDATE produto SET {', '.join(campos)} WHERE id=%s"
        cursor.execute(sql, tuple(valores))
        conn.commit()
        return {"mensagem": "Produto atualizado com sucesso"}
    except Exception as e:
        return {"erro": str(e)}
    finally:
        cursor.close()
        conn.close()

def excluir_produto(id):
    conn = conectar()
    if not conn:
        return {"erro": "Não foi possível conectar ao banco de dados"}

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produto WHERE id=%s", (id,))
        conn.commit()
        return {"mensagem": "Produto excluído com sucesso"}
    except Exception as e:
        return {"erro": str(e)}
    finally:
        cursor.close()
        conn.close()

def valor_total_estoque():
    conn = conectar()
    if not conn:
        return {"valor_total": 0}

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(preco * quantidade) FROM produto")
        total = cursor.fetchone()[0]
        return {"valor_total": total if total else 0}
    except Exception as e:
        return {"erro": str(e)}
    finally:
        cursor.close()
        conn.close()
