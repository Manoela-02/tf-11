class Cpf:
    def __init__(self, numero):
        self.numero = numero

    def eh_valido(self):
        if len(self.numero) != 11:
            return False
        return True

class Email:
    def __init__(self, endereco):
        self.endereco = endereco

    def eh_valido(self):
        if "@" not in self.endereco:
            return False
        if self.endereco == "":
            return False
        return True

class Cep:
    def __init__(self, codigo):
        self.codigo = codigo

    def eh_valido(self):
        if len(self.codigo) != 8:
            return False
        return True

class Dinheiro:
    def __init__(self, quantia):
        self.quantia = quantia

    def calcular_desconto(self, tipo_cliente):
        if tipo_cliente == "vip":
            return Dinheiro(self.quantia * 0.10)
        if tipo_cliente == "funcionario":
            return Dinheiro(self.quantia * 0.20)
        return Dinheiro(0.0)

    def subtrair(self, outro):
        return Dinheiro(self.quantia - outro.quantia)

    def multiplicar(self, fator):
        return Dinheiro(self.quantia * fator)

    def formatar(self):
        return f"R$ {self.quantia:.2f}"

class Status:
    def __init__(self, sigla):
        self.sigla = sigla

    def esta_aberto(self):
        return self.sigla == "A"

    def esta_pago(self):
        return self.sigla == "P"

    def esta_cancelado(self):
        return self.sigla == "C"

    def descrever(self):
        if self.sigla == "A":
            return "aberto"
        if self.sigla == "P":
            return "pago"
        if self.sigla == "C":
            return "cancelado"
        return "desconhecido"

class Cliente:
    def __init__(self, nome, cpf, email, rua, cidade, cep, tipo):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.rua = rua
        self.cidade = cidade
        self.cep = cep
        self.tipo = tipo

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class ItemDoPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Pedido:
    def __init__(self, numero, cliente, status, itens):
        self.numero = numero
        self.cliente = cliente
        self.status = status
        self.itens = itens

cliente_ana = Cliente("Ana Souza", Cpf("11111111111"), Email("ana@email.com"), "Rua A", "Sorocaba", Cep("18000000"), "normal")
cliente_bruno = Cliente("Bruno Lima", Cpf("2222222222"), Email("bruno@email.com"), "Rua B", "Itu", Cep("13300000"), "vip")
cliente_carla = Cliente("Carla Dias", Cpf("33333333333"), Email("carla-email.com"), "Rua C", "Campinas", Cep("13000000"), "funcionario")
cliente_diego = Cliente("Diego Rocha", Cpf("44444444444"), Email("diego@email.com"), "Rua D", "Itu", Cep("13300000"), "normal")
cliente_eva = Cliente("Eva Nunes", Cpf("55555555555"), Email("eva@email.com"), "Rua E", "Sorocaba", Cep("18000000"), "vip")
cliente_fabio = Cliente("Fabio Dias", Cpf("66666666666"), Email("fabio@email.com"), "Rua F", "Campinas", Cep("13000000"), "normal")
cliente_gil = Cliente("Gil Alves", Cpf("77777777777"), Email("gil@email.com"), "Rua G", "Sorocaba", Cep("18000000"), "normal")

produto_caderno = Produto("Caderno", Dinheiro(15.50))
produto_caneta = Produto("Caneta", Dinheiro(2.50))
produto_livro = Produto("Livro", Dinheiro(90.00))
produto_livro_desc = Produto("Livro", Dinheiro(89.50))
produto_fone = Produto("Fone", Dinheiro(60.00))

pedidos = [
    Pedido(1, cliente_ana, Status("A"), [ItemDoPedido(produto_caderno, 2), ItemDoPedido(produto_caneta, 5)]),
    Pedido(2, cliente_bruno, Status("A"), [ItemDoPedido(produto_livro, 1)]),
    Pedido(3, cliente_ana, Status("P"), [ItemDoPedido(produto_livro_desc, 1)]),
    Pedido(4, cliente_carla, Status("A"), [ItemDoPedido(produto_fone, 1)]),
    Pedido(5, cliente_diego, Status("C"), [ItemDoPedido(produto_caderno, 1)]),
    Pedido(6, cliente_eva, Status("P"), [ItemDoPedido(produto_fone, 1)]),
    Pedido(7, cliente_fabio, Status("A"), [ItemDoPedido(produto_caneta, 10)]),
    Pedido(8, cliente_gil, Status("A"), [ItemDoPedido(produto_fone, 2)])
]

def pagar(pedido):
    if not pedido.status.esta_aberto():
        return False
    if len(pedido.itens) == 0:
        return False
    pedido.status = Status("P")
    return True

def cancelar(pedido):
    if not pedido.status.esta_aberto():
        return False
    pedido.status = Status("C")
    return True

def relatorio():
    arrec_total = Dinheiro(0.0)
    qtd_abertos = 0
    for pedido in pedidos:
        if pedido.status.descrever() == "aberto" or pedido.status.esta_aberto():
            pass
        
        if pedido.status.esta_pago() or pedido.status.esta_cancelado():
            print(f"Pedido {pedido.numero} - {pedido.cliente.nome} - {pedido.cliente.cidade}")
            st_txt = pedido.status.descrever()
            print(f"  status: {st_txt}")
            if pedido.status.esta_pago():
                vl_total = Dinheiro(0.0)
                for item in pedido.itens:
                    vl_item = Dinheiro(item.quantidade * item.produto.preco.quantia)
                    vl_total = Dinheiro(vl_total.quantia + vl_item.quantia)
                    print(f"   {item.quantidade} x {item.produto.nome} = {vl_item.formatar()}")
                desc = vl_total.calcular_desconto(pedido.cliente.tipo)
                a_pagar = vl_total.subtrair(desc)
                arrec_total = Dinheiro(arrec_total.quantia + a_pagar.quantia)
                print(f"  total: {vl_total.formatar()} | desconto: {desc.formatar()} | a pagar: {a_pagar.formatar()}")
        elif pedido.status.esta_aberto():
            print(f"Pedido {pedido.numero} - {pedido.cliente.nome} - {pedido.cliente.cidade}")
            st_txt = pedido.status.descrever()
            print(f"  status: {st_txt}")
            vl_total = Dinheiro(0.0)
            for item in pedido.itens:
                vl_item = Dinheiro(item.quantidade * item.produto.preco.quantia)
                vl_total = Dinheiro(vl_total.quantia + vl_item.quantia)
                print(f"   {item.quantidade} x {item.produto.nome} = {vl_item.formatar()}")
            desc = vl_total.calcular_desconto(pedido.cliente.tipo)
            a_pagar = vl_total.subtrair(desc)
            print(f"  total: {vl_total.formatar()} | desconto: {desc.formatar()} | a pagar: {a_pagar.formatar()}")

    print(f"arrecadado: {arrec_total.formatar()}")
    
    for pedido in pedidos:
        if pedido.status.esta_aberto():
            qtd_abertos += 1
    print(f"abertos: {qtd_abertos}")

for pedido in pedidos:
    if not pedido.cliente.cpf.eh_valido():
        print(f"pedido {pedido.numero} recusado: cpf invalido")
    elif not pedido.cliente.email.eh_valido():
        print(f"pedido {pedido.numero} recusado: email invalido")
    elif not pedido.cliente.cep.eh_valido():
        print(f"pedido {pedido.numero} recusado: cep invalido")

print(f"pagar 1: {pagar(pedidos[0])}")
print(f"pagar 3: {pagar(pedidos[2])}")
print(f"pagar 5: {pagar(pedidos[4])}")
print(f"pagar 6: {pagar(pedidos[5])}")
print(f"cancelar 5: {cancelar(pedidos[4])}")
print(f"cancelar 1: {cancelar(pedidos[0])}")

relatorio()