import random

# Variáveis globais
valor_giro = 0.25
saldo = 0.0

# Retorna o saldo formatado
def get_saldo():
    global saldo
    return f"Saldo: R$ {saldo:.2f}"

# Adiciona saldo ao jogador
def adicionar_saldo(valor):
    global saldo
    if valor > 0:
        saldo += valor
        return True
    return False

# Gira a máquina e aplica lógica de vitória com premiação fixa
def realizar_giro():
    global saldo, valor_giro
    if saldo >= valor_giro:
        saldo -= valor_giro
        n1 = random.randint(1, 3)
        n2 = random.randint(1, 3)
        n3 = random.randint(1, 3)
        vencedor = (n1 == n2 == n3)
        ganho = 0
        if vencedor:
            ganho = valor_giro * 4  
            saldo += ganho
        return n1, n2, n3, vencedor, ganho, saldo
    else:
        return None
