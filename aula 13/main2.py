class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.pedidos = []  

    def adicionar_pedido(self, pedido):
        
        self.pedidos.append(pedido)
        pedido.cliente = self  

    def listar_pedidos(self):
        
        if not self.pedidos:
            print(f"{self.nome} não fez nenhum pedido.")
        else:
            print(f"Pedidos de {self.nome}:")
            for pedido in self.pedidos:
                print(f"- Pedido ID: {pedido.id}, Data: {pedido.data}")


class Pedido:
    def __init__(self, id, data, total):
        self.id = id
        self.data = data
        self.total = total
        self.cliente = None  

    def exibir_detalhes(self):
        
        print(f"Pedido ID: {self.id}")
        print(f"Data: {self.data}")
        print(f"Total: R${self.total:.2f}")
        if self.cliente:
            print(f"Cliente: {self.cliente.nome} ({self.cliente.email})")
        else:
            print("Este pedido não está associado a nenhum cliente.")


cliente1 = Cliente("João Silva", "joao.silva@email.com")
cliente2 = Cliente("Maria Oliveira", "maria.oliveira@email.com")


pedido1 = Pedido(1, "2025-02-10", 150.75)
pedido2 = Pedido(2, "2025-02-11", 200.00)
pedido3 = Pedido(3, "2025-02-12", 99.99)


cliente1.adicionar_pedido(pedido1)
cliente1.adicionar_pedido(pedido2)
cliente2.adicionar_pedido(pedido3)


cliente1.listar_pedidos()


pedido1.exibir_detalhes()

