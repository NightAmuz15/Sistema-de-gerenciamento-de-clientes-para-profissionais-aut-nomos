




# -*- coding: utf-8 -*-
"""Sistema de Gerenciamento de Clientes para Autônomos em Teresina-PI"""


import json
import os
import platform
from typing import List, Dict, Optional

class SistemaClientes:
    ARQUIVO_DADOS = 'clientes.json'

    def __init__(self):
        "Inicializa o sistema carregando os dados existentes."
        self.clientes: List[Dict] = []
        self.proximo_id: int = 1
        self.carregar_dados()

    def limpar_tela(self):
        """Limpa o terminal para melhor visualização."""
        sistema = platform.system()
        if sistema == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def salvar_dados(self):
        """Salva a lista de clientes e o contador de ID em arquivo JSON."""
        dados = {
            'clientes': self.clientes,
            'proximo_id': self.proximo_id
        }
        try:
            with open(self.ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Erro ao salvar dados: {e}")

    def carregar_dados(self):
        """Carrega os dados do arquivo JSON se existir."""
        if not os.path.exists(self.ARQUIVO_DADOS):
            return

        try:
            with open(self.ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                self.clientes = dados.get('clientes', [])
                self.proximo_id = dados.get('proximo_id', 1)
        except (json.JSONDecodeError, IOError):
            print("Arquivo de dados corrompido ou ilegível. Iniciando novo banco de dados.")
            self.clientes = []
            self.proximo_id = 1

    def validar_telefone(self, telefone: str) -> bool:
        """Valida se o telefone tem apenas números e tamanho mínimo (DDD + número)."""
        return telefone.isdigit() and len(telefone) >= 10

    def solicitar_entrada(self, mensagem: str, obrigatorio: bool = True) -> str:
        """Função auxiliar para capturar inputs do usuário."""
        while True:
            entrada = input(mensagem).strip()
            if not obrigatorio:
                return entrada
            if entrada:
                return entrada
            print(">> Este campo é obrigatório. Tente novamente.")

    def cadastrar_cliente(self):
        """Realiza o cadastro de um novo cliente."""
        print("\n--- Cadastrar Cliente ---")

        nome = self.solicitar_entrada("Nome do cliente: ")

        while True:
            telefone = self.solicitar_entrada("Telefone (apenas números, ex: 86999999999): ")
            if self.validar_telefone(telefone):
                break
            print(">> Telefone inválido. Digite sem espaço ou símbolos. (mínimo 10 dígitos com DDD).")

        servico = self.solicitar_entrada("Serviço contratado (ex: Manicure, Pedreiro): ")

        novo_cliente = {
            "id": self.proximo_id,
            "nome": nome,
            "telefone": telefone,
            "servico": servico
        }

        self.clientes.append(novo_cliente)
        print(f"\n✅ Cliente cadastrado com sucesso! [ID: {self.proximo_id}]")
        self.proximo_id += 1
        self.salvar_dados()
        input("Pressione Enter para continuar...")

    def listar_clientes(self):
        """Exibe todos os clientes cadastrados."""
        print("\n--- Lista de Clientes ---")
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            print(f"{'ID':<5} | {'Nome':<25} | {'Telefone':<15} | {'Serviço'}")
            print("-" * 60)
            for c in self.clientes:
                print(f"{c['id']:<5} | {c['nome']:<25} | {c['telefone']:<15} | {c['servico']}")
        input("\nPressione Enter para continuar...")

    def buscar_cliente_por_id(self, id_cliente: int) -> Optional[Dict]:
        """Busca um cliente pelo ID e retorna o dicionário ou None."""
        for cliente in self.clientes:
            if cliente['id'] == id_cliente:
                return cliente
        return None

    def atualizar_cliente(self):
        """Atualiza dados de um cliente existente."""
        print("\n--- Atualizar Cliente ---")
        if not self.clientes:
            print("Nenhum cliente para atualizar.")
            input("Pressione Enter para voltar.")
            return

        try:
            id_busca = int(input("Digite o ID do cliente: "))
        except ValueError:
            print(">> ID inválido.")
            return

        cliente = self.buscar_cliente_por_id(id_busca)

        if not cliente:
            print(">> Cliente não encontrado.")
        else:
            print(f"Editando: {cliente['nome']}")

            novo_nome = self.solicitar_entrada("Novo nome (Enter para manter): ", obrigatorio=False)
            if novo_nome:
                cliente['nome'] = novo_nome

            while True:
                novo_tel = self.solicitar_entrada("Novo telefone (Enter para manter): ", obrigatorio=False)
                if not novo_tel:
                    break
                if self.validar_telefone(novo_tel):
                    cliente['telefone'] = novo_tel
                    break
                print(">> Telefone inválido.")

            novo_servico = self.solicitar_entrada("Novo serviço (Enter para manter): ", obrigatorio=False)
            if novo_servico:
                cliente['servico'] = novo_servico

            self.salvar_dados()
            print("\n✅ Dados atualizados com sucesso!")

        input("Pressione Enter para continuar...")

    def remover_cliente(self):
        """Remove um cliente da lista."""
        print("\n--- Remover Cliente ---")
        if not self.clientes:
            print("Nenhum cliente para remover.")
            input("Pressione Enter para voltar.")
            return

        try:
            id_remover = int(input("Digite o ID do cliente para remover: "))
        except ValueError:
            print(">> ID inválido.")
            return

        cliente = self.buscar_cliente_por_id(id_remover)

        if cliente:
            confirmacao = input(f"Tem certeza que deseja remover {cliente['nome']}? (S/N): ").lower()
            if confirmacao == 's':
                self.clientes.remove(cliente)
                self.salvar_dados()
                print("\n✅ Cliente removido com sucesso.")
            else:
                print("\nOperação cancelada.")
        else:
            print(">> Cliente não encontrado.")

        input("Pressione Enter para continuar...")

    def gerar_relatorio(self):
        """Gera um relatório estatístico simples."""
        print("\n--- Relatório Gerencial ---")
        total = len(self.clientes)
        if total == 0:
            print("Sem dados para gerar relatório.")
        else:
            print(f"Total de Clientes: {total}")
            print("\nDistribuição por Serviço:")
            contagem = {}
            for c in self.clientes:
                servico = c['servico']
                contagem[servico] = contagem.get(servico, 0) + 1

            for servico, qtd in contagem.items():
                print(f"- {servico}: {qtd} cliente(s)")

        input("\nPressione Enter para continuar...")

    def buscar_cliente(self):
        """Busca textual por nome ou telefone."""
        print("\n--- Buscar Cliente ---")
        termo = input("Digite nome ou telefone para buscar: ").strip().lower()

        encontrados = [
            c for c in self.clientes
            if termo in c['nome'].lower() or termo in c['telefone']
        ]

        if encontrados:
            print(f"\n{len(encontrados)} cliente(s) encontrado(s):")
            for c in encontrados:
                print(f"ID: {c['id']} | {c['nome']} | Tel: {c['telefone']} | {c['servico']}")
        else:
            print(">> Nenhum registro encontrado.")

        input("\nPressione Enter para continuar...")

    def menu(self):
        """Loop principal do menu."""
        while True:
            self.limpar_tela()
            print("====== GESTÃO DE CLIENTES (Teresina-PI) ======")
            print("1. Cadastrar Cliente")
            print("2. Listar Clientes")
            print("3. Atualizar Cliente")
            print("4. Remover Cliente")
            print("5. Buscar Cliente")
            print("6. Relatório Gerencial")
            print("7. Sair")
            print("==============================================")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                self.cadastrar_cliente()
            elif opcao == '2':
                self.listar_clientes()
            elif opcao == '3':
                self.atualizar_cliente()
            elif opcao == '4':
                self.remover_cliente()
            elif opcao == '5':
                self.buscar_cliente()
            elif opcao == '6':
                self.gerar_relatorio()
            elif opcao == '7':
                self.salvar_dados()
                print("\nSaindo do sistema... Até logo!")
                break
            else:
                input("Opção inválida. Pressione Enter para tentar novamente.")

if __name__ == "__main__":
    app = SistemaClientes()
    app.menu()