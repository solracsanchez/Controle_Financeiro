import tkinter as tk
import base


class ControleFinanceiroGUI:
    def __init__(self, master):
        self.master = master
        master.title("Controle Financeiro")

        self.data_label = tk.Label(master, text="Data:")
        self.data_label.grid(row=0, column=0)

        self.data_entry = tk.Entry(master)
        self.data_entry.grid(row=0, column=1)

        self.valor_label = tk.Label(master, text="Valor:")
        self.valor_label.grid(row=1, column=0)

        self.valor_entry = tk.Entry(master)
        self.valor_entry.grid(row=1, column=1)

        self.descricao_label = tk.Label(master, text="Descrição:")
        self.descricao_label.grid(row=2, column=0)

        self.descricao_entry = tk.Entry(master)
        self.descricao_entry.grid(row=2, column=1)

        self.categoria_label = tk.Label(master, text="Categoria:")
        self.categoria_label.grid(row=3, column=0)

        self.categoria_entry = tk.Entry(master)
        self.categoria_entry.grid(row=3, column=1)

        self.tipo_label = tk.Label(master, text="Tipo:")
        self.tipo_label.grid(row=4, column=0)

        self.tipo_var = tk.StringVar(value="Receita")
        self.tipo_receita_radio = tk.Radiobutton(master, text="Receita", variable=self.tipo_var, value="Receita")
        self.tipo_receita_radio.grid(row=4, column=1)

        self.tipo_despesa_radio = tk.Radiobutton(master, text="Despesa", variable=self.tipo_var, value="Despesa")
        self.tipo_despesa_radio.grid(row=4, column=2)

        self.adicionar_button = tk.Button(master, text="Adicionar", command=self.adicionar_transacao)
        self.adicionar_button.grid(row=5, column=0)

        self.resumo_button = tk.Button(master, text="Exibir Resumo", command=self.exibir_resumo)
        self.resumo_button.grid(row=5, column=1)

        self.saldo_label = tk.Label(master, text="")
        self.saldo_label.grid(row=5, column=0, columnspan=2)

    def adicionar_transacao(self):
        data = self.data_entry.get()
        valor = float(self.valor_entry.get())
        descricao = self.descricao_entry.get()
        categoria = self.categoria_entry.get()
        tipo = self.tipo_var.get()
        base.adicionar_transacao(data, valor, descricao, categoria, conta, tipo=tipo)

        self.data_entry.delete(0, tk.END)
        self.valor_entry.delete(0, tk.END)
        self.descricao_entry.delete(0, tk.END)
        self.categoria_entry.delete(0, tk.END)

    def exibir_resumo(self):
        resumo = base.exibir_resumo()
        self.saldo_label.config(text=f"Saldo: R$ {resumo['saldo']:.2f}")
        # código para exibir o resumo em uma janela de diálogo ou na própria interface gráfica


root = tk.Tk()
gui = ControleFinanceiroGUI(root)
root.mainloop()
