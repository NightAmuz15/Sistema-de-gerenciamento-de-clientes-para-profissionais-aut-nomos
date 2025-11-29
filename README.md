# Sistema-de-gerenciamento-de-clientes-para-profissionais-aut-nomos
O sistema desenvolvido em python tem como principal função realizar o cadastro de clientes e auxiliar o seu gerenciamento. 
## Sistema de Gerenciamento de Clientes 

Este é um sistema simples de gerenciamento de clientes, desenvolvido em Python, ideal para autônomos e pequenos prestadores de serviço que precisam de uma ferramenta leve e eficaz para organizar seus cadastros.



# Funcionalidades Principais

O sistema é operado via Terminal/Prompt de Comando e oferece as seguintes opções:

1.  **Cadastrar Cliente:** Adiciona um novo cliente com nome, telefone e serviço contratado.
2.  **Listar Clientes:** Exibe todos os clientes em formato tabular organizado por ID.
3.  **Atualizar Cliente:** Permite modificar os dados (nome, telefone, serviço) de um cliente existente usando seu ID.
4.  **Remover Cliente:** Exclui um cliente permanentemente, usando seu ID.
5.  **Buscar Cliente:** Realiza uma busca textual por nome ou telefone.
6.  **Relatório Gerencial:** Gera estatísticas básicas, como o total de clientes e a contagem de clientes por tipo de serviço.
7.  **Sair:** Salva os dados e encerra o programa.



# Persistência de Dados

O sistema garante que os dados não sejam perdidos ao fechar o programa:

  * **Arquivo de Dados:** Os clientes são salvos automaticamente em um arquivo chamado **`clientes.json`** na mesma pasta do script.
  * **Salvamento Automático:** O salvamento ocorre após cada operação de escrita (Cadastro, Atualização, Remoção) e, crucialmente, ao selecionar a opção **"Sair"** do menu.
  * **Carregamento:** Ao iniciar o script, ele verifica e carrega os dados do `clientes.json`, se o arquivo existir.



# Como Usar

# Pré-requisitos

Você precisa ter o **Python 3** instalado em sua máquina.

# Instalação e Execução

1.  **Salve o Código:** Salve todo o código-fonte em um arquivo chamado **`sistema_clientes.py`**.

2.  **Abra o Terminal:** Navegue até a pasta onde você salvou o arquivo.

3.  **Execute o Script:** Use o seguinte comando para iniciar o sistema:

    ```bash
    python sistema_clientes.py
    ```

# Estrutura do Projeto

O projeto é composto por um único arquivo principal:

| Arquivo | Descrição |
| :--- | :--- |
| `sistema_clientes.py` | Contém toda a lógica do programa, a classe `SistemaClientes`, e o menu principal. |
| `clientes.json` | Arquivo gerado automaticamente para salvar os dados. **(Não edite manualmente se o programa estiver em execução)** |



## Estrutura do Código (OOP)

O código é construído em torno de uma classe principal:

  * **`class SistemaClientes`:** Contém todo o estado do sistema (`self.clientes`, `self.proximo_id`) e todos os métodos de operação (CRUD).
  * **Encapsulamento:** Elimina o uso de variáveis globais, tornando o código mais limpo e seguro.
  * **Funções Auxiliares:** Possui métodos como `limpar_tela()`, `validar_telefone()` e `salvar_dados()` para garantir o bom funcionamento e a experiência do usuário.
