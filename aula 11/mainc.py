class Celular:
    def __init__(self, marca, modelo, polegadas, armazenamento, mem_ram):
        self.marca = marca
        self.modelo = modelo
        self.polegadas = polegadas
        self.armazenamento = armazenamento
        self.mem_ram = mem_ram
        self.status_celular = 'desligado'
        self.status_chamada = 'não em chamada'

    def ligar(self):
        if self.status_celular == 'desligado':
            self.status_celular = 'ligado'
            print(f'{self.marca} {self.modelo} está agora ligado.')
        else:
            print(f'{self.marca} {self.modelo} já está ligado.')

    def desligar(self):
        if self.status_celular == 'ligado':
            self.status_celular = 'desligado'
            print(f'{self.marca} {self.modelo} está agora desligado.')
        else:
            print(f'{self.marca} {self.modelo} já está desligado.')

    def fazer_chamada(self, numero):
        if self.status_celular == 'ligado':
            if self.status_chamada == 'não em chamada':
                self.status_chamada = 'em chamada'
                print(f'Fazendo chamada para o número {numero}.')
            else:
                print(f'Já está em uma chamada. Não é possível fazer outra.')
        else:
            print(f'{self.marca} {self.modelo} precisa estar ligado para fazer uma chamada.')

    def encerrar_chamada(self):
        if self.status_chamada == 'em chamada':
            self.status_chamada = 'não em chamada'
            print('Chamada encerrada.')
        else:
            print('Não há chamada para encerrar.')

celular = Celular("Samsung", "Galaxy S23", 6.1, 128, 8)

celular.ligar()  
celular.fazer_chamada("999999999")  
celular.encerrar_chamada()  
celular.desligar()  
