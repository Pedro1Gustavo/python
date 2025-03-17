import sqlite3
import datetime


def get_db_connection():
    return sqlite3.connect('estoque.db')


def criar_banco():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT NOT NULL,
                quantidade_disponivel INTEGER NOT NULL,
                preco REAL NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_produto INTEGER NOT NULL,
                quantidade_vendida INTEGER NOT NULL,
                data_venda TEXT NOT NULL,
                FOREIGN KEY(id_produto) REFERENCES produtos(id)
            )
        ''')


criar_banco()


class Produto:
    def __init__(self, id=None, nome=None, descricao=None, quantidade_disponivel=0, preco=0.0):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade_disponivel = quantidade_disponivel
        self.preco = preco

    def salvar(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute('''
                    INSERT INTO produtos (nome, descricao, quantidade_disponivel, preco)
                    VALUES (?, ?, ?, ?)
                ''', (self.nome, self.descricao, self.quantidade_disponivel, self.preco))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                    UPDATE produtos
                    SET nome = ?, descricao = ?, quantidade_disponivel = ?, preco = ?
                    WHERE id = ?
                ''', (self.nome, self.descricao, self.quantidade_disponivel, self.preco, self.id))

    @staticmethod
    def consultar_todos():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM produtos')
            return cursor.fetchall()

    @staticmethod
    def consultar_por_id(produto_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM produtos WHERE id = ?', (produto_id,))
            return cursor.fetchone()

    @staticmethod
    def remover(produto_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM produtos WHERE id = ?', (produto_id,))


class Venda:
    def __init__(self, id=None, id_produto=None, quantidade_vendida=0, data_venda=None):
        self.id = id
        self.id_produto = id_produto
        self.quantidade_vendida = quantidade_vendida
        self.data_venda = data_venda if data_venda else datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def salvar(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO vendas (id_produto, quantidade_vendida, data_venda)
                VALUES (?, ?, ?)
            ''', (self.id_produto, self.quantidade_vendida, self.data_venda))

    @staticmethod
    def consultar_todas():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM vendas')
            return cursor.fetchall()


def cadastrar_produto(nome, descricao, quantidade, preco):
    produto = Produto(nome=nome, descricao=descricao, quantidade_disponivel=quantidade, preco=preco)
    produto.salvar()
    print(f'Produto "{nome}" cadastrado com sucesso.')


def listar_produtos():
    produtos = Produto.consultar_todos()
    if produtos:
        for produto in produtos:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Descrição: {produto[2]}, Quantidade: {produto[3]}, Preço: {produto[4]:.2f}")
    else:
        print("Nenhum produto encontrado.")


def atualizar_quantidade(produto_id, quantidade):
    produto = Produto.consultar_por_id(produto_id)
    if produto:
        nova_quantidade = produto[3] + quantidade
        if nova_quantidade < 0:
            print("Erro: Quantidade insuficiente para a atualização.")
        else:
            produto_obj = Produto(id=produto_id, nome=produto[1], descricao=produto[2],
                                  quantidade_disponivel=nova_quantidade, preco=produto[4])
            produto_obj.salvar()
            print(f"Quantidade do produto {produto[1]} atualizada para {nova_quantidade}.")
    else:
        print("Produto não encontrado.")


def remover_produto(produto_id):
    Produto.remover(produto_id)
    print(f"Produto com ID {produto_id} removido com sucesso.")


def registrar_venda(id_produto, quantidade_vendida):
    produto = Produto.consultar_por_id(id_produto)
    if produto:
        quantidade_disponivel = produto[3]
        if quantidade_vendida <= quantidade_disponivel:
            venda = Venda(id_produto=id_produto, quantidade_vendida=quantidade_vendida)
            venda.salvar()
            atualizar_quantidade(id_produto, -quantidade_vendida)
            print(f"Venda de {quantidade_vendida} unidades do produto {produto[1]} registrada com sucesso.")
        else:
            print("Quantidade em estoque insuficiente.")
    else:
        print("Produto não encontrado.")


cadastrar_produto('Camiseta', 'Camiseta de algodão', 50, 29.99)
cadastrar_produto('Calça', 'Calça jeans', 30, 79.99)


listar_produtos()


registrar_venda(1, 5)


listar_produtos()


remover_produto(4)


listar_produtos()


