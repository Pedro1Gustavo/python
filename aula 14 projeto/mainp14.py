import flet as ft


class Cliente:
    def __init__(self, nome, telefone, email, id_cliente):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id = id_cliente

    def __str__(self):
        return f"{self.nome} ({self.telefone}, {self.email})"


class Quarto:
    def __init__(self, numero, tipo, preco_diaria, status_disponibilidade=True):
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria
        self.status_disponibilidade = status_disponibilidade

    def verificar_disponibilidade(self):
        return self.status_disponibilidade


class Reserva:
    def __init__(self, dono_reserva, quarto_reservado, data_checkin, data_checkout):
        self.dono_reserva = dono_reserva
        self.quarto_reservado = quarto_reservado
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.status_reserva = "Confirmada"

    def modificar_reserva(self, nova_data_checkin, nova_data_checkout):
        self.data_checkin = nova_data_checkin
        self.data_checkout = nova_data_checkout

    def cancelar_reserva(self):
        self.status_reserva = "Cancelada"
        self.quarto_reservado.status_disponibilidade = True


class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def criar_reserva(self, cliente, quarto, data_checkin, data_checkout):
        if quarto.verificar_disponibilidade():
            nova_reserva = Reserva(cliente, quarto, data_checkin, data_checkout)
            self.reservas.append(nova_reserva)
            quarto.status_disponibilidade = False
            return "Reserva confirmada"
        else:
            return "Quarto indisponível"

    def cancelar_reserva(self, reserva):
        reserva.cancelar_reserva()

    def listar_reservas(self):
        return [f"Reserva de {reserva.dono_reserva.nome} para o quarto {reserva.quarto_reservado.numero} - Status: {reserva.status_reserva}" for reserva in self.reservas]

    def listar_clientes(self):
        return [str(cliente) for cliente in self.clientes]


def main(page):
    gerente_reservas = GerenciadorDeReservas()

   
    cliente1 = Cliente("João Silva", "123456789", "joao@email.com", 1)
    cliente2 = Cliente("Maria Oliveira", "987654321", "maria@email.com", 2)
    cliente3 = Cliente("Douglas Carvalho", "987654312", "mario@email.com", 3)

    
    quarto1 = Quarto(101, "single", 100)
    quarto2 = Quarto(102, "double", 150)
    quarto3 = Quarto(103, "double", 200)

    gerente_reservas.adicionar_cliente(cliente1)
    gerente_reservas.adicionar_cliente(cliente2)
    gerente_reservas.adicionar_cliente(cliente3)
    gerente_reservas.adicionar_quarto(quarto1)
    gerente_reservas.adicionar_quarto(quarto2)
    gerente_reservas.adicionar_quarto(quarto3)

    
    gerente_reservas.criar_reserva(cliente1, quarto1, "2025-02-10", "2025-02-15")
    gerente_reservas.criar_reserva(cliente2, quarto2, "2025-02-12", "2025-02-18")
    gerente_reservas.criar_reserva(cliente3, quarto3, "2025-02-14", "2025-02-21")

    def mostrar_reservas():
        page.controls.clear()
        reservas = gerente_reservas.listar_reservas()
        if reservas:
            page.add(ft.Column([ft.Text(r) for r in reservas]))
        else:
            page.add(ft.Text("Não há reservas para exibir."))

    def tela_inicial():
        page.controls.clear()
        
        for q in gerente_reservas.quartos:
            disponibilidade = 'Disponível' if q.status_disponibilidade else 'Ocupado'
            page.add(ft.Text(f"Quarto {q.numero} - {q.tipo} - R${q.preco_diaria}/diária - {disponibilidade}"))
        
        page.add(ft.ElevatedButton("Ver Reservas", on_click=lambda e: mostrar_reservas()))

    tela_inicial()


ft.app(target=main)


