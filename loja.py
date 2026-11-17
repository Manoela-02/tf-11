ped = [
    [1, "Ana Souza", "11111111111", "ana@email.com", "Rua A", "Sorocaba", "18000000", "normal", "A", [["Caderno", 2, 15.50], ["Caneta", 5, 2.50]]],
    [2, "Bruno Lima", "2222222222", "bruno@email.com", "Rua B", "Itu", "13300000", "vip", "A", [["Livro", 1, 90.00]]],
    [3, "Ana Souza", "11111111111", "ana@email.com", "Rua A", "Sorocaba", "18000000", "normal", "P", [["Livro", 1, 89.50]]],
    [4, "Carla Dias", "33333333333", "carla-email.com", "Rua C", "Campinas", "13000000", "funcionario", "A", [["Fone", 1, 60.00]]],
    [5, "Diego Rocha", "44444444444", "diego@email.com", "Rua D", "Itu", "13300000", "normal", "C", [["Caderno", 1, 15.50]]],
    [6, "Eva Nunes", "55555555555", "eva@email.com", "Rua E", "Sorocaba", "18000000", "vip", "P", [["Fone", 1, 60.00]]],
    [7, "Fabio Dias", "66666666666", "fabio@email.com", "Rua F", "Campinas", "13000000", "normal", "A", [["Caneta", 10, 2.50]]],
    [8, "Gil Alves", "77777777777", "gil@email.com", "Rua G", "Sorocaba", "18000000", "normal", "A", [["Fone", 2, 60.00]]]
]

def validar_cpf(c):
    if len(c) != 11:
        return False
    return True

def validar_email(e):
    if "@" not in e:
        return False
    if e == "":
        return False
    return True

def validar_cep(cep):
    if len(cep) != 8:
        return False
    return True

def calcular_desconto(tp, vl):
    if tp == "vip":
        return vl * 0.10
    if tp == "funcionario":
        return vl * 0.20
    return 0.0

def calcular_valor_a_pagar(vl, desc):
    return vl - desc

def descrever_status(st):
    if st == "A":
        return "aberto"
    if st == "P":
        return "pago"
    if st == "C":
        return "cancelado"
    return "desconhecido"

def pagar(p):
    if p[8] != "A":
        return False
    if len(p[9]) == 0:
        return False
    p[8] = "P"
    return True

def cancelar(p):
    if p[8] != "A":
        return False
    p[8] = "C"
    return True

def relatorio():
    arrec_total = 0.0
    qtd_abertos = 0
    for p in ped:
        if p[8] == "aberto" or p[8] == "A":
            pass
        
        if p[8] == "P" or p[8] == "C":
            print(f"Pedido {p[0]} - {p[1]} - {p[5]}")
            st_txt = descrever_status(p[8])
            print(f"  status: {st_txt}")
            if p[8] == "P":
                vl_total = 0.0
                for i in p[9]:
                    vl_item = i[1] * i[2]
                    vl_total += vl_item
                    print(f"   {i[1]} x {i[0]} = R$ {vl_item:.2f}")
                desc = calcular_desconto(p[7], vl_total)
                a_pagar = calcular_valor_a_pagar(vl_total, desc)
                arrec_total += a_pagar
                print(f"  total: R$ {vl_total:.2f} | desconto: R$ {desc:.2f} | a pagar: R$ {a_pagar:.2f}")
        elif p[8] == "A":
            print(f"Pedido {p[0]} - {p[1]} - {p[5]}")
            st_txt = descrever_status(p[8])
            print(f"  status: {st_txt}")
            vl_total = 0.0
            for i in p[9]:
                vl_item = i[1] * i[2]
                vl_total += vl_item
                print(f"   {i[1]} x {i[0]} = R$ {vl_item:.2f}")
            desc = calcular_desconto(p[7], vl_total)
            a_pagar = calcular_valor_a_pagar(vl_total, desc)
            print(f"  total: R$ {vl_total:.2f} | desconto: R$ {desc:.2f} | a pagar: R$ {a_pagar:.2f}")

    print(f"arrecadado: R$ {arrec_total:.2f}")
    
    for p in ped:
        if p[8] == "A":
            qtd_abertos += 1
    print(f"abertos: {qtd_abertos}")

for p in ped:
    if not validar_cpf(p[2]):
        print(f"pedido {p[0]} recusado: cpf invalido")
    elif not validar_email(p[3]):
        print(f"pedido {p[0]} recusado: email invalido")
    elif not validar_cep(p[6]):
        print(f"pedido {p[0]} recusado: cep invalido")

print(f"pagar 1: {pagar(ped[0])}")
print(f"pagar 3: {pagar(ped[2])}")
print(f"pagar 5: {pagar(ped[4])}")
print(f"pagar 6: {pagar(ped[5])}")
print(f"cancelar 5: {cancelar(ped[4])}")
print(f"cancelar 1: {cancelar(ped[0])}")

relatorio()