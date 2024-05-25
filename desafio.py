import os
from getmac import get_mac_address

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[c] Cadastrar Cliente
[a] Cadastrar Conta
[l] Alterar Limite de Saque
[p] Cadastro de Chave Pix
[m] Cadastrar Computador
[u] Autorizar Computador
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
CUSTO_MENSAL_10_SAQUES = 29.90
CUSTO_MENSAL_20_SAQUES = 39.90
CUSTO_MENSAL_50_SAQUES = 49.90

class ContaCorrente:
    def __init__(self, usuario, saldo_inicial=0):
        self.usuario = usuario
        self.saldo = saldo_inicial
        self.limite_saque = limite
        self.limite_saques = LIMITE_SAQUES
        self.pix_chaves = []
        self.computadores = []
        self.autorizacoes = {}
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R$ {valor:.2f} realizado com sucesso."
        else:
            return "Valor de depósito inválido."
    
    def sacar(self, valor, mac_address):
        if valor > self.saldo:
            return "Saldo insuficiente."
        if valor > self.limite_saque:
            return "Valor do saque excede o limite."
        if self.usuario.numero_saques >= self.limite_saques:
            return "Número máximo de saques excedido."
        if mac_address not in self.computadores:
            return "Computador não autorizado para transações."
        
        self.saldo -= valor
        self.usuario.numero_saques += 1
        return f"Saque de R$ {valor:.2f} realizado com sucesso."
    
    def extrato(self):
        return f"Saldo atual: R$ {self.saldo:.2f}"

    def alterar_limite_saque(self, novo_limite):
        self.limite_saque = novo_limite
        return f"Limite de saque alterado para R$ {novo_limite:.2f}."

    def alterar_limite_saques_diarios(self, novo_limite_saques):
        self.limite_saques = novo_limite_saques
        return f"Limite de saques diários alterado para {novo_limite_saques}."

    def cadastrar_pix(self, tipo, valor):
        self.pix_chaves.append({'tipo': tipo, 'valor': valor})
        return f"Chave Pix do tipo {tipo} cadastrada com sucesso."

    def cadastrar_computador(self):
        mac_address = get_mac_address()
        self.computadores.append(mac_address)
        return f"Computador com MAC Address {mac_address} cadastrado com sucesso."

    def autorizar_computador(self, mac_address):
        self.autorizacoes[mac_address] = True
        return f"Computador com MAC Address {mac_address} autorizado com sucesso."

    def verificar_computador(self, mac_address):
        return mac_address in self.autorizacoes

class Usuario:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.conta = None
        self.numero_saques = 0
    
    def criar_conta(self, saldo_inicial=0):
        self.conta = ContaCorrente(self, saldo_inicial)
        return self.conta

usuarios = []

def encontrar_usuario(nome, sobrenome):
    for usuario in usuarios:
        if usuario.nome.lower() == nome.lower() and usuario.sobrenome.lower() == sobrenome.lower():
            return usuario
    return None

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        nome = input("Digite o nome do cliente: ").strip()
        sobrenome = input("Digite o sobrenome do cliente: ").strip()
        usuario = encontrar_usuario(nome, sobrenome)
        if usuario and usuario.conta:
            valor = float(input("Digite o valor do depósito: "))
            print(usuario.conta.depositar(valor))
        else:
            print("Usuário ou conta não encontrados.")
    
    elif opcao == "s":
        nome = input("Digite o nome do cliente: ").strip()
        sobrenome = input("Digite o sobrenome do cliente: ").strip()
        usuario = encontrar_usuario(nome, sobrenome)
        if usuario and usuario.conta:
            valor = float(input("Digite o valor do saque: "))
            mac_address = get_mac_address()
            print(usuario.conta.sacar(valor, mac_address))
        else:
            print("Usuário ou conta não encontrados.")
    
    elif opcao == "e":
        nome = input("Digite o nome do cliente: ").strip()
        sobrenome = input("Digite o sobrenome do cliente: ").strip()
        usuario = encontrar_usuario(nome, sobrenome)
        if usuario and usuario.conta:
            print("\n================ EXTRATO ================")
            print(usuario.conta.extrato())
            print("==========================================")
        else:
            print("Usuário ou conta não encontrados.")
    
    elif opcao == "c":
        nome = input("Digite o nome do cliente: ").strip()
        sobrenome = input("Digite o sobrenome do cliente: ").strip()
        if encontrar_usuario(nome, sobrenome):
            print("Usuário já cadastrado.")
        else:
            usuarios.append(Usuario(nome, sobrenome))
            print("Usuário cadastrado com sucesso.")
    
    elif opcao == "a":
        nome = input("Digite o nome do cliente: ").strip()
        sobrenome = input("Digite o sobrenome do cliente: ").strip()
        usuario = encontrar_usuario(nome, sobrenome)
        if usuario:
            if usuario.conta:
                print("Usuário já possui uma conta.")
            else:
                saldo_inicial = float(input("Digite o saldo inicial da conta: "))
                usuario.criar_conta(saldo_inicial)
                print("Conta criada com sucesso.")
        else:
            print("Usuário não encontrado.")

    elif opcao == "l":
        nome = input("Digite o nome do cliente: ").strip()
        sobrenome = input("Digite o sobrenome do cliente: ").strip()
        usuario = encontrar_usuario(nome, sobrenome)
        if usuario and usuario.conta:
            novo_limite = float(input("Digite o novo limite de saque: "))
            print(usuario.conta.alterar_limite_saque(novo_limite))
        else:
            print("Usuário ou conta não encontrados.")

        opcao_plano = input("Deseja alterar o plano de limite de saques? (s/n): ").strip().lower()
        if opcao_plano == 's':
            print("\nPlanos disponíveis:")
            print("1. 10 saques por R$ 29,90")
            print("2. 20 saques por R$ 39,90")
            print("3. 50 saques por R$ 49,90")
            plano = input("Selecione o plano desejado (1, 2 ou 3): ").strip()
            if plano == '1':
                print(usuario.conta.alterar_limite_saques_diarios(10))
                print(f"Custo mensal: R$ {CUSTO_MENSAL_10_SAQUES:.2f}")
            elif plano == '2':
                print(usuario.conta.alterar_limite_saques_diarios(20))
                print(f"Custo mensal: R$ {CUSTO_MENSAL_20_SAQUES:.2f}")
            elif plano == '3':
                print(usuario.conta.alterar_limite_saques_diarios(50))
                print(f"Custo mensal: R$ {CUSTO_MENSAL_50_SAQUES:.2f}")
            else:
                print("Plano inválido.")

    elif opcao == "p":
        nome = input("Digite o nome do cliente: ").strip()
        sobrenome = input("Digite o sobrenome do cliente: ").strip()
        usuario = encontrar_usuario(nome, sobrenome)
        if usuario and usuario.conta:
            tipo = input("Digite o tipo de chave Pix (email, telefone, cpf, chave_aleatoria): ").strip().lower()
            valor = input("Digite o valor da chave Pix: ").strip()
            print(usuario.conta.cadastrar_pix(tipo, valor))
        else:
            print("Usuário ou conta não encontrados.")

    elif opcao == "m":
        nome = input("Digite o nome do cliente: ").strip()
        sobrenome = input("Digite o sobrenome do cliente: ").strip()
        usuario = encontrar_usuario(nome, sobrenome)
        if usuario and usuario.conta:
            print(usuario.conta.cadastrar_computador())
        else:
            print("Usuário ou conta não encontrados.")

    elif opcao == "u":
        nome = input("Digite o nome do cliente: ").strip()
        sobrenome = input("Digite o sobrenome do cliente: ").strip()
        usuario = encontrar_usuario(nome, sobrenome)
        if usuario and usuario.conta:
            mac_address = input("Digite o MAC Address do computador a autorizar: ").strip()
            print(usuario.conta.autorizar_computador(mac_address))
        else:
            print("Usuário ou conta não encontrados.")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



