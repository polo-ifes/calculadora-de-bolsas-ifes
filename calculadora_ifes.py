# calculadora_de_bolsas_ifes.py
# Copyright (c) 2025 Anderson Pereira Martins e Victor Gianordoli
# Licenciado sob MIT License. Veja LICENSE.md para detalhes.
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.font import Font
import csv
from datetime import datetime
import json

class CalculadoraBolsasIfes:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Bolsas IFES - Resolução 239/2024")
        self.root.geometry("900x650")
        self.root.configure(bg='#f0f0f0')
        
        # Configurações de estilo
        self.fonte_titulo = Font(family="Arial", size=14, weight="bold")
        self.fonte_normal = Font(family="Arial", size=10)
        self.fonte_destaque = Font(family="Arial", size=11, weight="bold")
        
        self.cor_fundo = '#f0f0f0'
        self.cor_botao = '#4CAF50'  # Verde
        self.cor_botao_sec = '#f44336'  # Vermelho
        self.cor_botao_terc = '#2196F3'  # Azul
        self.cor_botao_import = '#FF9800'  # Laranja
        
        self.equipe = []
        self.modalidades = []
        
        self.carregar_dados_completos()
        self.criar_interface()

    def carregar_dados_completos(self):
        """Carrega todas as modalidades de bolsa conforme Resolução 239/2024"""
        self.modalidades = [
            # Pesquisador
            {"Modalidade": "Pesquisador - Doutor", "Sigla": "PEQ-A", "Valor R$": 1500.00, "Teto (x)": 3.0},
            {"Modalidade": "Pesquisador - Mestre", "Sigla": "PEQ-B", "Valor R$": 1400.00, "Teto (x)": 3.0},
            {"Modalidade": "Pesquisador - Especialista", "Sigla": "PEQ-C", "Valor R$": 1300.00, "Teto (x)": 3.0},
            {"Modalidade": "Pesquisador - Graduado", "Sigla": "PEQ-D", "Valor R$": 1200.00, "Teto (x)": 3.0},
            {"Modalidade": "Pesquisador - Técnico", "Sigla": "PEQ-E", "Valor R$": 1100.00, "Teto (x)": 3.0},
            {"Modalidade": "Pesquisador - Qualificado/Experiente", "Sigla": "PEQ-F", "Valor R$": 1100.00, "Teto (x)": 3.0},
            
            # Extensionista
            {"Modalidade": "Extensionista - Doutor", "Sigla": "EXT-A", "Valor R$": 1500.00, "Teto (x)": 3.0},
            {"Modalidade": "Extensionista - Mestre", "Sigla": "EXT-B", "Valor R$": 1400.00, "Teto (x)": 3.0},
            {"Modalidade": "Extensionista - Especialista", "Sigla": "EXT-C", "Valor R$": 1400.00, "Teto (x)": 3.0},
            {"Modalidade": "Extensionista - Graduado", "Sigla": "EXT-D", "Valor R$": 1300.00, "Teto (x)": 3.0},
            {"Modalidade": "Extensionista - Técnico", "Sigla": "EXT-E", "Valor R$": 1100.00, "Teto (x)": 3.0},
            {"Modalidade": "Extensionista - Qualificado/Experiente", "Sigla": "EXT-F", "Valor R$": 1100.00, "Teto (x)": 3.0},
            
            # Gestor
            {"Modalidade": "Gestor de Programa - Doutor", "Sigla": "GPO-A", "Valor R$": 1500.00, "Teto (x)": 8.0},
            {"Modalidade": "Gestor de Programa - Mestre", "Sigla": "GPO-B", "Valor R$": 1400.00, "Teto (x)": 7.0},
            {"Modalidade": "Gestor de Programa - Especialista", "Sigla": "GPO-C", "Valor R$": 1300.00, "Teto (x)": 6.0},
            {"Modalidade": "Gestor de Programa - Graduado", "Sigla": "GPO-D", "Valor R$": 1200.00, "Teto (x)": 5.0},
            {"Modalidade": "Gestor de Projeto - Doutor", "Sigla": "GPR-A", "Valor R$": 1500.00, "Teto (x)": 8.0},
            {"Modalidade": "Gestor de Projeto - Mestre", "Sigla": "GPR-B", "Valor R$": 1400.00, "Teto (x)": 7.0},
            {"Modalidade": "Gestor de Projeto - Especialista", "Sigla": "GPR-C", "Valor R$": 1300.00, "Teto (x)": 6.0},
            {"Modalidade": "Gestor de Projeto - Graduado", "Sigla": "GPR-D", "Valor R$": 1200.00, "Teto (x)": 5.0},
            
            # Coordenador
            {"Modalidade": "Coordenador de Programa - Doutor", "Sigla": "CPO-A", "Valor R$": 1500.00, "Teto (x)": 8.0},
            {"Modalidade": "Coordenador de Programa - Mestre", "Sigla": "CPO-B", "Valor R$": 1400.00, "Teto (x)": 7.0},
            {"Modalidade": "Coordenador de Programa - Especialista", "Sigla": "CPO-C", "Valor R$": 1300.00, "Teto (x)": 6.0},
            {"Modalidade": "Coordenador de Programa - Graduado", "Sigla": "CPO-D", "Valor R$": 1200.00, "Teto (x)": 5.0},
            {"Modalidade": "Coordenador de Projeto - Doutor", "Sigla": "CPR-A", "Valor R$": 1500.00, "Teto (x)": 8.0},
            {"Modalidade": "Coordenador de Projeto - Mestre", "Sigla": "CPR-B", "Valor R$": 1400.00, "Teto (x)": 7.0},
            {"Modalidade": "Coordenador de Projeto - Especialista", "Sigla": "CPR-C", "Valor R$": 1300.00, "Teto (x)": 6.0},
            {"Modalidade": "Coordenador de Projeto - Graduado", "Sigla": "CPR-D", "Valor R$": 1200.00, "Teto (x)": 5.0},
            
            # Colaborador Externo
            {"Modalidade": "Colaborador Externo - Doutor", "Sigla": "CLE-D", "Valor R$": 1500.00, "Teto (x)": 8.0},
            {"Modalidade": "Colaborador Externo - Mestre", "Sigla": "CLE-M", "Valor R$": 1400.00, "Teto (x)": 7.0},
            {"Modalidade": "Colaborador Externo - Especialista", "Sigla": "CLE-E", "Valor R$": 1300.00, "Teto (x)": 5.0},
            {"Modalidade": "Colaborador Externo - Graduado", "Sigla": "CLE-G", "Valor R$": 1200.00, "Teto (x)": 4.0},
            {"Modalidade": "Colaborador Externo - Técnico", "Sigla": "CLE-T", "Valor R$": 1100.00, "Teto (x)": 3.0},
            {"Modalidade": "Colaborador Externo - Qualificado/Experiente", "Sigla": "CLE-Q", "Valor R$": 1100.00, "Teto (x)": 2.0},
            
            # Estudante
            {"Modalidade": "Estudante de Doutorado", "Sigla": "EST-D", "Valor R$": 3100.00, "Teto (x)": 3.0},
            {"Modalidade": "Estudante de Mestrado", "Sigla": "EST-M", "Valor R$": 2100.00, "Teto (x)": 3.0},
            {"Modalidade": "Estudante de Pós-graduação lato sensu", "Sigla": "EST-LS", "Valor R$": 2100.00, "Teto (x)": 2.0},
            {"Modalidade": "Estudante de Aperfeiçoamento", "Sigla": "EST-A", "Valor R$": 2100.00, "Teto (x)": 2.0},
            {"Modalidade": "Estudante de Graduação", "Sigla": "EST-G", "Valor R$": 700.00, "Teto (x)": 3.0},
            {"Modalidade": "Estudante de Curso Técnico", "Sigla": "EST-CT", "Valor R$": 300.00, "Teto (x)": 3.0},
            {"Modalidade": "Estudante de Especialização Técnica", "Sigla": "EST-ET", "Valor R$": 300.00, "Teto (x)": 3.0},
            {"Modalidade": "Estudante de Curso FIC", "Sigla": "EST-CF", "Valor R$": 300.00, "Teto (x)": 3.0},
            
            # Empreendedor
            {"Modalidade": "Empreendedor Júnior", "Sigla": "EMP-JR", "Valor R$": 1100.00, "Teto (x)": 10.0},
            {"Modalidade": "Empreendedor Sênior", "Sigla": "EMP-SE", "Valor R$": 3100.00, "Teto (x)": 5.0},
            
            # Bolsas de Iniciação Tecnológica
            {"Modalidade": "Iniciação Tecnológica - Nível Superior", "Sigla": "ITEC-S", "Valor R$": 800.00, "Teto (x)": 3.0},
            {"Modalidade": "Iniciação Tecnológica - Nível Médio", "Sigla": "ITEC-M", "Valor R$": 400.00, "Teto (x)": 3.0},
            
            # Bolsas de Apoio Técnico
            {"Modalidade": "Apoio Técnico - Nível Superior", "Sigla": "APOIO-S", "Valor R$": 1000.00, "Teto (x)": 3.0},
            {"Modalidade": "Apoio Técnico - Nível Médio", "Sigla": "APOIO-M", "Valor R$": 600.00, "Teto (x)": 3.0}
        ]

    def criar_interface(self):
        """Cria a interface gráfica principal"""
        main_frame = tk.Frame(self.root, bg=self.cor_fundo)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(main_frame, text="Calculadora de Bolsas IFES - Resolução 239/2024", 
                font=self.fonte_titulo, bg=self.cor_fundo).pack(pady=(0, 20))
        
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        self.criar_aba_equipe()
        self.criar_aba_lista()

    def criar_aba_equipe(self):
        """Cria a aba de cálculo por equipe"""
        frame = tk.Frame(self.notebook, bg=self.cor_fundo)
        self.notebook.add(frame, text="Cálculo de Equipe")
        
        # Tabela
        table_frame = tk.Frame(frame, bg=self.cor_fundo)
        table_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        self.tree = ttk.Treeview(table_frame, columns=("Modalidade", "CHS", "Fator X", "Valor"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        
        self.tree.column("Modalidade", width=350)
        self.tree.column("CHS", width=70, anchor='center')
        self.tree.column("Fator X", width=80, anchor='center')
        self.tree.column("Valor", width=120, anchor='e')
        
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Botões
        btn_frame = tk.Frame(frame, bg=self.cor_fundo)
        btn_frame.pack(fill=tk.X, pady=(10, 20))
        
        # Botões da esquerda
        left_btn_frame = tk.Frame(btn_frame, bg=self.cor_fundo)
        left_btn_frame.pack(side=tk.LEFT)
        
        tk.Button(left_btn_frame, text="Adicionar Membro", command=self.adicionar_membro,
                bg=self.cor_botao, fg='white', font=self.fonte_normal).pack(side=tk.LEFT, padx=5)
        
        tk.Button(left_btn_frame, text="Remover Selecionado", command=self.remover_membro,
                bg=self.cor_botao_sec, fg='white', font=self.fonte_normal).pack(side=tk.LEFT, padx=5)
        
        tk.Button(left_btn_frame, text="Limpar Equipe", command=self.limpar_equipe,
                font=self.fonte_normal).pack(side=tk.LEFT, padx=5)
        
        # Botões da direita
        right_btn_frame = tk.Frame(btn_frame, bg=self.cor_fundo)
        right_btn_frame.pack(side=tk.RIGHT)
        
        tk.Button(right_btn_frame, text="Importar Equipe", command=self.importar_equipe,
                bg=self.cor_botao_import, fg='white', font=self.fonte_normal).pack(side=tk.LEFT, padx=5)
        
        tk.Button(right_btn_frame, text="Exportar Equipe", command=self.exportar_equipe,
                bg=self.cor_botao_terc, fg='white', font=self.fonte_normal).pack(side=tk.LEFT, padx=5)
        
        # Total
        total_frame = tk.Frame(frame, bg='white', bd=1, relief=tk.SOLID)
        total_frame.pack(fill=tk.X)
        
        tk.Label(total_frame, text="Total da Equipe:", 
                font=self.fonte_destaque, bg='white').pack(side=tk.LEFT, padx=10, pady=10)
        
        self.total_var = tk.StringVar(value="R$ 0,00")
        tk.Label(total_frame, textvariable=self.total_var, 
                font=self.fonte_destaque, bg='white', fg='green').pack(side=tk.RIGHT, padx=10)

    def criar_aba_lista(self):
        """Cria a aba com lista completa de modalidades"""
        frame = tk.Frame(self.notebook, bg=self.cor_fundo)
        self.notebook.add(frame, text="Lista Completa")
        
        tree = ttk.Treeview(frame, columns=("Modalidade", "Sigla", "Valor Base", "Teto"), show="headings")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        
        tree.column("Modalidade", width=400)
        tree.column("Sigla", width=100, anchor='center')
        tree.column("Valor Base", width=120, anchor='e')
        tree.column("Teto", width=80, anchor='center')
        
        for modalidade in self.modalidades:
            tree.insert("", "end", values=(
                modalidade["Modalidade"],
                modalidade["Sigla"],
                f"{modalidade['Valor R$']:,.2f}".replace(".", ","),
                modalidade["Teto (x)"]
            ))
        
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    def adicionar_membro(self):
        """Janela para adicionar novo membro à equipe"""
        popup = tk.Toplevel(self.root)
        popup.title("Adicionar Membro")
        popup.geometry("500x400")
        popup.resizable(False, False)
        
        # Widgets
        tk.Label(popup, text="Modalidade:", font=self.fonte_normal).pack(pady=(10, 5))
        modalidade_var = tk.StringVar()
        cb = ttk.Combobox(popup, textvariable=modalidade_var, 
                         values=[m["Modalidade"] for m in self.modalidades],
                         state="readonly", font=self.fonte_normal)
        cb.pack(fill=tk.X, padx=20, pady=5)
        
        tk.Label(popup, text="Detalhes:", font=self.fonte_normal).pack(pady=(10, 5))
        detalhes_text = tk.Text(popup, height=5, font=self.fonte_normal, state="disabled")
        detalhes_text.pack(fill=tk.X, padx=20, pady=5)
        
        tk.Label(popup, text="Carga Horária Semanal (CHS):", font=self.fonte_normal).pack(pady=(10, 5))
        chs_var = tk.DoubleVar(value=8.0)
        tk.Entry(popup, textvariable=chs_var, font=self.fonte_normal).pack(fill=tk.X, padx=20, pady=5)
        
        tk.Label(popup, text="Fator X:", font=self.fonte_normal).pack(pady=(10, 5))
        fator_x_var = tk.DoubleVar(value=1.0)
        tk.Entry(popup, textvariable=fator_x_var, font=self.fonte_normal).pack(fill=tk.X, padx=20, pady=5)
        
        def atualizar_detalhes(event=None):
            modalidade = modalidade_var.get()
            if not modalidade:
                return
            
            dados = next((m for m in self.modalidades if m["Modalidade"] == modalidade), None)
            if dados:
                detalhes_text.config(state="normal")
                detalhes_text.delete(1.0, tk.END)
                detalhes_text.insert(tk.END, 
                    f"Sigla: {dados['Sigla']}\n"
                    f"Valor Base: R$ {dados['Valor R$']:,.2f}\n"
                    f"Teto Máximo: {dados['Teto (x)']}")
                detalhes_text.config(state="disabled")
                fator_x_var.set(1.0)
        
        cb.bind("<<ComboboxSelected>>", atualizar_detalhes)
        
        def confirmar():
            try:
                modalidade = modalidade_var.get()
                if not modalidade:
                    messagebox.showwarning("Aviso", "Selecione uma modalidade!")
                    return
                
                chs = chs_var.get()
                if chs <= 0:
                    messagebox.showwarning("Aviso", "A CHS deve ser maior que zero!")
                    return
                
                fator_x = fator_x_var.get()
                if fator_x < 1.0:
                    messagebox.showwarning("Aviso", "O Fator X não pode ser menor que 1.0!")
                    return
                
                dados = next((m for m in self.modalidades if m["Modalidade"] == modalidade), None)
                if not dados:
                    messagebox.showerror("Erro", "Modalidade não encontrada!")
                    return
                
                if fator_x > dados["Teto (x)"]:
                    messagebox.showwarning("Aviso", 
                        f"Fator X não pode ser maior que {dados['Teto (x)']} para esta modalidade!")
                    return
                
                valor = (dados["Valor R$"] * chs / 10) * fator_x
                
                self.equipe.append({
                    "Modalidade": modalidade,
                    "CHS": chs,
                    "Fator X": fator_x,
                    "Valor": valor
                })
                
                self.atualizar_tabela()
                popup.destroy()
            
            except ValueError:
                messagebox.showerror("Erro", "Valores inválidos! Use números válidos.")
        
        tk.Button(popup, text="Confirmar", command=confirmar,
                bg=self.cor_botao, fg='white', font=self.fonte_normal).pack(pady=20)

    def remover_membro(self):
        """Remove o membro selecionado da equipe"""
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um membro para remover!")
            return
        
        index = int(self.tree.index(selecionado[0]))
        self.equipe.pop(index)
        self.atualizar_tabela()

    def limpar_equipe(self):
        """Remove todos os membros da equipe"""
        if not self.equipe:
            return
        
        if messagebox.askyesno("Confirmar", "Deseja realmente limpar toda a equipe?"):
            self.equipe = []
            self.atualizar_tabela()

    def atualizar_tabela(self):
        """Atualiza a tabela com os membros da equipe"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for membro in self.equipe:
            self.tree.insert("", "end", values=(
                membro["Modalidade"],
                membro["CHS"],
                membro["Fator X"],
                f"{membro['Valor']:,.2f}".replace(".", ",")
            ))
        
        total = sum(m["Valor"] for m in self.equipe)
        self.total_var.set(f"R$ {total:,.2f}".replace(".", ","))

    def importar_equipe(self):
        """Importa uma equipe salva anteriormente"""
        arquivo = filedialog.askopenfilename(
            filetypes=[("Arquivos JSON", "*.json"), ("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*")],
            title="Selecione o arquivo para importar"
        )
        
        if not arquivo:
            return
        
        try:
            if arquivo.endswith('.json'):
                with open(arquivo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    self.equipe = dados['equipe']
            elif arquivo.endswith('.csv'):
                with open(arquivo, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f, delimiter=';')
                    self.equipe = []
                    for row in reader:
                        if row['Modalidade']:
                            self.equipe.append({
                                "Modalidade": row['Modalidade'],
                                "CHS": float(row['CHS']),
                                "Fator X": float(row['Fator X']),
                                "Valor": float(row['Valor (R$)'].replace(',', '.'))
                            })
            else:
                raise ValueError("Formato de arquivo não suportado")
            
            self.atualizar_tabela()
            messagebox.showinfo("Sucesso", "Equipe importada com sucesso!")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao importar equipe:\n{str(e)}")

    def exportar_equipe(self):
        """Exporta a equipe atual para arquivo"""
        if not self.equipe:
            messagebox.showwarning("Aviso", "A equipe está vazia. Não há dados para exportar!")
            return
        
        arquivo = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Arquivos JSON", "*.json"), ("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*")],
            title="Salvar equipe como"
        )
        
        if not arquivo:
            return
        
        try:
            if arquivo.endswith('.json'):
                with open(arquivo, 'w', encoding='utf-8') as f:
                    json.dump({
                        "equipe": self.equipe,
                        "total": sum(m["Valor"] for m in self.equipe),
                        "data_exportacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    }, f, indent=2, ensure_ascii=False)
            else:
                with open(arquivo, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f, delimiter=';')
                    writer.writerow(["Modalidade", "CHS", "Fator X", "Valor (R$)"])
                    for membro in self.equipe:
                        writer.writerow([
                            membro["Modalidade"],
                            membro["CHS"],
                            membro["Fator X"],
                            f"{membro['Valor']:.2f}".replace(".", ",")
                        ])
                    writer.writerow([])
                    writer.writerow(["Total da Equipe:", "", "", f"{sum(m['Valor'] for m in self.equipe):.2f}".replace(".", ",")])
            
            messagebox.showinfo("Sucesso", f"Equipe exportada com sucesso:\n{arquivo}")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao exportar equipe:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraBolsasIfes(root)
    root.mainloop()
