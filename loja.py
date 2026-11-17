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

cliente_ana = Cliente("Ana Souza", "11111111111", "ana@email.com", "Rua A", "Sorocaba", "18000000", "normal")
cliente_bruno = Cliente("Bruno Lima", "2222222222", "bruno@email.com", "Rua B", "Itu", "13300000", "vip")
cliente_carla = Cliente("Carla Dias", "33333333333", "carla-email.com", "Rua C", "Campinas", "13000000", "funcionario")
cliente_diego = Cliente("Diego Rocha", "44444444444", "diego@email.com", "Rua D", "Itu", "13300000", "normal")
cliente_eva = Cliente("Eva Nunes", "55555555555", "eva@email.com", "Rua E", "Sorocaba", "18000000", "vip")
cliente_fabio = Cliente("Fabio Dias", "66666666666", "fabio@email.com", "Rua F", "Campinas", "13000000", "normal")
cliente_gil = Cliente("Gil Alves", "77777777777", "gil@email.com", "Rua G", "Sorocaba", "18000000", "normal")

produto_caderno = Produto("Caderno", 15.50)
produto_caneta = Produto("Caneta", 2.50)
produto_livro = Produto("Livro", 90.00)
produto_livro_desc = Produto("Livro", 89.50)
produto_fone = Produto("Fone", 60.00)

pedidos = [
    Pedido(1, cliente_ana, "A", [ItemDoPedido(produto_caderno, 2), ItemDoPedido(produto_caneta, 5)]),
    Pedido(2, cliente_bruno, "A", [ItemDoPedido(produto_livro, 1)]),
    Pedido(3, cliente_ana, "P", [ItemDoPedido(produto_livro_desc, 1)]),
    Pedido(4, cliente_carla, "A", [ItemDoPedido(produto_fone, 1)]),
    Pedido(5, cliente_diego, "C", [ItemDoPedido(produto_caderno, 1)]),
    Pedido(6, cliente_eva, "P", [ItemDoPedido(produto_fone, 1)]),
    Pedido(7, cliente_fabio, "A", [ItemDoPedido(produto_caneta, 10)]),
    Pedido(8, cliente_gil, "A", [ItemDoPedido(produto_fone, 2)])
]

def validar_cpf(cpf):
    if len(cpf) != 11:
        return False
    return True

def validar_email(email):
    if "@" not in email:
        return False
    if email == "":
        return False
    return True

def validar_cep(cep):
    if len(cep) != 8:
        return False
    return True

def calcular_desconto(tipo, valor):
    if tipo == "vip":
        return valor * 0.10
    if tipo == "funcionario":
        return valor * 0.20
    return 0.0

def calcular_valor_a_pagar(valor, desconto):
    return valor - desconto

def descrever_status(status):
    if status == "A":
        return "aberto"
    if status == "P":
        return "pago"
    if status == "C":
        return "cancelado"
    return "desconhecido"

def pagar(pedido):
    if pedido.status != "A":
        return False
    if len(pedido.itens) == 0:
        return False
    pedido.status = "P"
    return True

def cancelar(pedido):
    if pedido.status != "A":
        return False
    pedido.status = "C"
    return True

def relatorio():
    arrec_total = 0.0
    qtd_abertos = 0
    for pedido in pedidos:
        if pedido.status == "aberto" or pedido.status == "A":
            pass
        
        if pedido.status == "P" or pedido.status == "C":
            print(f"Pedido {pedido.numero} - {pedido.cliente.nome} - {pedido.cliente.cidade}")
            st_txt = descrever_status(pedido.status)
            print(f"  status: {st_txt}")
            if pedido.status == "P":
                vl_total = 0.0
                for item in pedido.itens:
                    vl_item = item.quantidade * item.produto.preco
                    vl_total += vl_item
                    print(f"   {item.quantidade} x {item.produto.nome} = R$ {vl_item:.2f}")
                desc = calcular_desconto(pedido.cliente.tipo, vl_total)
                a_pagar = calcular_valor_a_pagar(vl_total, desc)
                arrec_total += a_pagar
                print(f"  total: R$ {vl_total:.2f} | desconto: R$ {desc:.2f} | a pagar: R$ {a_pagar:.2f}")
        elif pedido.status == "A":
            print(f"Pedido {pedido.numero} - {pedido.cliente.nome} - {pedido.cliente.cidade}")
            st_txt = descrever_status(pedido.status)
            print(f"  status: {st_txt}")
            vl_total = 0.0
            for item in pedido.itens:
                vl_item = item.quantidade * item.produto.preco
                vl_total += vl_item
                print(f"   {item.quantidade} x {item.produto.nome} = R$ {vl_item:.2f}")
            desc = calcular_desconto(pedido.cliente.tipo, vl_total)
            a_pagar = calcular_valor_a_pagar(vl_total, desc)
            print(f"  total: R$ {vl_total:.2f} | desconto: R$ {desc:.2f} | a pagar: R$ {a_pagar:.2f}")

    print(f"arrecadado: R$ {arrec_total:.2f}")
    
    for pedido in pedidos:
        if pedido.status == "A":
            qtd_abertos += 1
    print(f"abertos: {qtd_abertos}")

for pedido in pedidos:
    if not validar_cpf(pedido.cliente.cpf):
        print(f"pedido {pedido.numero} recusado: cpf invalido")
    elif not validar_email(pedido.cliente.email):
        print(f"pedido {pedido.numero} recusado: email invalido")
    elif not validar_cep(pedido.cliente.cep):
        print(f"pedido {pedido.numero} recusado: cep invalido")

print(f"pagar 1: {pagar(pedidos[0])}")
print(f"pagar 3: {pagar(pedidos[2])}")
print(f"pagar 5: {pagar(pedidos[4])}")
print(f"pagar 6: {pagar(pedidos[5])}")
print(f"cancelar 5: {cancelar(pedidos[4])}")
print(f"cancelar 1: {cancelar(pedidos[0])}")

relatorio()