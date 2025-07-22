import tkinter as tk
from index import get_saldo, adicionar_saldo, realizar_giro

# Funções da interface
def atualizar_saldo():
    label_saldo.config(text=get_saldo())

def apostar():
    try:
        valor = float(entry_aposta.get())
        if adicionar_saldo(valor):
            atualizar_saldo()
            label_status.config(text="💰 Aposta adicionada!")
            entry_aposta.delete(0, tk.END)
        else:
            label_status.config(text="⚠️ Valor inválido!")
    except ValueError:
        label_status.config(text="⚠️ Digite um número válido!")

def girar():
    resultado = realizar_giro()
    if resultado:
        n1, n2, n3, vencedor, ganho, _ = resultado
        label_resultado.config(text=f"{n1} | {n2} | {n3}")
        if vencedor:
            label_status.config(text=f"🟢 VENCEDOR! Você ganhou R$ {ganho:.2f}!")
        else:
            label_status.config(text="🔴 PERDEDOR")
        atualizar_saldo()
    else:
        label_status.config(text="⚠️ Saldo insuficiente para girar!")

# Interface Tkinter
janela = tk.Tk()
janela.title("🎰 Caça-níqueis")

# Widgets
label_titulo = tk.Label(janela, text="Faça sua aposta!", font=("Arial", 14))
label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

entry_aposta = tk.Entry(janela)
entry_aposta.grid(row=1, column=0)

botao_apostar = tk.Button(janela, text="Apostar", command=apostar)
botao_apostar.grid(row=1, column=1)

label_saldo = tk.Label(janela, text=get_saldo(), font=("Arial", 12))
label_saldo.grid(row=2, column=0, columnspan=2, pady=5)

botao_girar = tk.Button(janela, text="Girar", command=girar)
botao_girar.grid(row=3, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(janela, text="-- | -- | --", font=("Courier", 16))
label_resultado.grid(row=4, column=0, columnspan=2)

label_status = tk.Label(janela, text="", font=("Arial", 12))
label_status.grid(row=5, column=0, columnspan=2, pady=5)

janela.mainloop()
