class Fatura:
    def __init__(self, nome_item, preco_unitario, quantidade):
        self.nome_item = nome_item
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total = 0  

    def gerar_fatura(self):
        
        self.valor_total = self.preco_unitario * self.quantidade
        return self.valor_total


fatura = Fatura("Camiseta", 50.00, 3)
valor = fatura.gerar_fatura()
print(f"Valor total da fatura: R${valor:.2f}")
