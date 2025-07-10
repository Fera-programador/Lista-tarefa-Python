import tkinter as tk
from tkinter import ttk, messagebox

# Lista de dados das tarefas...
tarefas = []

# Funções...
def atualizar_lista():
    tree.delete(*tree.get_children())
    for tarefa in tarefas:
        tree.insert('', 'end', values=(tarefa,))

def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa:
        tarefas.append(tarefa)
        atualizar_lista()
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa para adicioná-la.")

def remover_tarefa():
    selecionada = tree.selection()
    if selecionada:
        for item in selecionada:
            valor = tree.item(item, 'values')[0]
            tarefas.remove(valor)
        atualizar_lista()
    else:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para removê-la.")

def limpar_lista():
    if messagebox.askyesno("Confirmação", "Você tem certeza que deseja limpar a lista?"):
        tarefas.clear()
        atualizar_lista()

# Janela principal...
janela = tk.Tk()
janela.title("Lista de Tarefas em Python")
janela.geometry("500x400")
janela.resizable(True, True)

# Estilo moderno...
estilo = ttk.Style(janela)
estilo.theme_use("clam")

# Entrada...
entrada = ttk.Entry(janela, width=40)
entrada.pack(pady=10)

# Botões...
frame_botoes = ttk.Frame(janela)
frame_botoes.pack(pady=10)

ttk.Button(frame_botoes, text="Adicionar", command=adicionar_tarefa).grid(row=0, column=0, padx=5)
ttk.Button(frame_botoes, text="Remover", command=remover_tarefa).grid(row=0, column=1, padx=5)
ttk.Button(frame_botoes, text="Limpar", command=limpar_lista).grid(row=0, column=2, padx=5)

# Lista de tarefas (Treeview)...
tree = ttk.Treeview(janela, columns=("Tarefa",), show="headings")
tree.heading("Tarefa", text="Tarefa")
tree.pack(expand=True, fill=tk.BOTH, pady=10)

# Inicia a janela...
janela.mainloop()

# Fim do código
# Este é um exemplo simples de uma lista de tarefas usando tkinter.