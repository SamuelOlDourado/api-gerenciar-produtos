from flask import Flask, jsonify, request,g
import sqlite3
app = Flask(__name__)

def ligar_banco():
    banco = g._database = sqlite3.connect('banco_produtos.db')
    return banco

@app.teardown_appcontext
def fechar_banco(exception):
    banco=ligar_banco()
    banco.close()

def buscar_por_id(id):
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM Produtos WHERE id = ?', (id,))
    return cursor.fetchone()
@app.route('/')
def home():
    return 'API de Produtos'

@app.route('/todos_produtos', methods=['GET'])
def listar_produtos():
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM Produtos')
    produtos = cursor.fetchall()
    resultados = []
    for linha in produtos:
        produto = {
            'id': linha[0],
            'nome': linha[1],
            'descricao': linha[2],
            'preco': linha[3],
            'estoque': linha[4],
            'categoria': linha[5]
        }
        resultados.append(produto)
    return jsonify(resultados)

@app.route('/adicionar_produto', methods=['POST'])
def adicionar_produto():
    try:
        data = request.get_json()
        banco = ligar_banco()
        cursor = banco.cursor()
        cursor.execute("""INSERT INTO Produtos (nome, descricao, preco, estoque, categoria) 
                       VALUES (?, ?, ?, ?, ?)""",
                       (data['nome'], data['descricao'], data['preco'], data['estoque'], data['categoria']))
        banco.commit()
        return jsonify({'mensagem': 'produto adicionado com sucesso!'})
    except (KeyError, ValueError, TypeError):
        return jsonify({'erro': 'Dados inválidos ou incompletos'}), 400

@app.route('/produto/<int:id>', methods=['GET'])
def buscar_produto(id):
    produto=buscar_por_id(id)
    if produto==None:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    return jsonify({
        'id': produto[0],
        'nome': produto[1],
        'descricao': produto[2],
        'preco': produto[3],
        'estoque': produto[4],
        'categoria': produto[5]
    })

@app.route('/deletar_produto/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    produto=buscar_por_id(id)
    if produto==None:
        return jsonify({'erro': 'Produto não encontrado'}), 404
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute('DELETE FROM Produtos WHERE id = ?', (id,))
    banco.commit()
    return jsonify({'mensagem': 'Produto deletado com sucesso!'})

@app.route('/atualizar_produto/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    produto=buscar_por_id(id)
    if produto == None:
        return jsonify({'erro': 'produto não encontrado'}), 404
    try:
        data = request.get_json()
        banco = ligar_banco()
        cursor = banco.cursor()
        cursor.execute("""UPDATE Produtos SET nome = ?, descricao = ?, preco = ?, estoque = ?, categoria = ? WHERE id = ? """,
                       (data['nome'], data['descricao'], data['preco'], data['estoque'], data['categoria'], id))
        banco.commit()
        return jsonify({'mensagem': 'Produto atualizado com sucesso!'})
    except(KeyError, ValueError, TypeError):
        return jsonify({'erro': 'Dados inválidos ou incompletos'}), 400

if __name__ == '__main__':
    app.run(debug=True)