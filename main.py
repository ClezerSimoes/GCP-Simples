"""
 Objetivo, criar um sistema de cadastro de clientes e pedidos capaz de:

 - Cadastrar clientes/pedidos
 - Consultar clientes/pedidos
 - Editar clientes/pedidos
 - Excluir clientes/pedidos
 - Emitir relatórios de pedidos

"""
import os 

class Cliente():
    lista_cliente = []
    contador_id = 1

    def __init__(self, nome, documento, telefone, email, endereco, codigo_id):
        self.nome = nome
        self.doc = documento
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.codigo_id = codigo_id

    # Imprime as informações do cliente.
    def info_cliente(self):
        print ("\nInformações do cliente: ") 
        print (f"Código de identificação (ID): {self.codigo_id}")
        print (f"Nome: {self.nome}")
        print (f"Documento (RG, CPF/CNPJ): {self.doc}")
        print (f"Telefone: {self.telefone}")
        print (f"E-mail: {self.email}")
        print (f"Endereço: {self.endereco}")

    # Realiza o cadastro de clientes.
    @classmethod
    def cadastro(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        nome = input ("Digite o nome do cliente: ").strip().upper()
        doc = input ("Digite o documento de identificação do cliente: ").strip().upper()
        telefone = input ("Digite o telefone do cliente: ").strip().upper()
        email = input ("Digite o e-mail do cliente: ").strip().upper()
        endereco = input ("Digite o endereço do cliente: ").strip().upper()

        cliente = cls(nome, doc, telefone, email, endereco, Cliente.contador_id)
        Cliente.lista_cliente.append(cliente)
        Cliente.contador_id += 1

    # Edita clientes cadastrados (Precisa terminar)
    def edit_cliente():
        try: 
            edit_exclude = int(input("Selecione para editar ou excluir um contato \n1 - Editar \n2 - Excluir \n3 - Voltar\n"))

            if edit_exclude < 1 or edit_exclude > 3:
                print ("Você precisa selecionar entre uma das opções disponíveis.")
                input ("Pressione Enter para continuar...")
                return

            elif edit_exclude == 1:
                os.system('cls' if os.name == 'nt' else 'clear') 
                busca_cliente = input("Digite o nome ou o ID do cliente que deseja editar:").strip().upper()

                cliente_encontrado = None
                for cliente in Cliente.lista_cliente:
                    if busca_cliente == cliente.nome or (busca_cliente.isdigit() and int(busca_cliente) == cliente.codigo_id):
                        cliente_encontrado = cliente
                        break
                if cliente_encontrado:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print ("\n Cliente encontrado: ")
                    cliente_encontrado.info_cliente()

                    print ("Qual dado deseja editar?")
                    print ( "1 - Nome"
                            "\n2 - Documento"
                            "\n3 - Telefone"
                            "\n4 - E-mail"
                            "\n5 - Endereço"
                            "\n6 - Cancelar" 
                    )

                    opcao = input("Digite o nome da opção desejada: ")

                    if opcao == "1":
                        cliente_encontrado.nome = input("Novo nome: ").strip().upper()
                    elif opcao == "2":
                        cliente_encontrado.doc = input("Novo documento: ").strip().upper()
                    elif opcao == "3":
                        cliente_encontrado.telefone = input("Novo telefone: ").strip().upper()
                    elif opcao == "4":
                        cliente_encontrado.email = input("Novo e-mail: ").strip().upper()
                    elif opcao == "5":
                        cliente_encontrado.endereco = input("Novo endereço: ").strip().upper()
                    elif opcao == "6":
                        print ("Edição cancelada.")
                    else:
                        print("Opção inválida")
                        

                    print ("\nDados atualizados: ")
                    cliente_encontrado.info_cliente()
                    input ("Pressione enter para continuar...")

                else:
                    print ("Cliente não encontrado")
                    input ("pressione enter para continuar...")


            elif edit_exclude == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                busca_cliente = input("Digite o nome ou o ID do cliente que deseja excluir:").strip().upper()

                for cliente in Cliente.lista_cliente:
                    if busca_cliente == cliente.nome or (busca_cliente.isdigit() and int(busca_cliente) == cliente.codigo_id):
                        Cliente.lista_cliente.remove(cliente)
                        print ("Cliente excluído com sucesso!")
                        input ("pressione enter para continuar...")
                        return

                print ("Cliente não encontrado")
                input ("pressione enter para continuar...")
            
            else:
                print ("voltando ao menu principal")
                input ("Pressione Enter para continuar...")

        except ValueError:
            print ("Entrada Inválida, digite um numero intero dentre as opções disponíveis.")
            input ("Pressione Enter para continuar...")


class Pedidos():
    lista_pedido = []
    num_pedido = 1

    def __init__(self, numero_pedido, itens_pedido, data_pedido, prazo_pedido, valor_pedido, status_pedido):
        self.numero_pedido = numero_pedido
        self.itens_pedido = itens_pedido
        self.data_pedido = data_pedido
        self.prazo_pedido = prazo_pedido
        self.valor_pedido = valor_pedido
        self.status_pedido = status_pedido

    
    # Função para imprimir as informações de determinado pedido
    def info_pedido(self):
        print ("\n\nInformações do pedido:\n")
        print (f"Numero (ID) do pedido: {self.numero_pedido}")
        print (f"Itens do pedido: {self.itens_pedido}")
        print (f"Data do pedido: {self.data_pedido}")
        print (f"Prazo do pedido: {self.prazo_pedido}")
        print (f"Valor do pedido: {self.valor_pedido}")
        print (f"status do pedido: {self.status_pedido}")

    # Função para cadastrar pedidos
    @classmethod
    def cadastro(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Novo pedido: ")
        itens = input("\nDigite os itens do pedido: ")
        data = input("Digite data do pedido: ")
        prazo = input("Digite o prazo do pedido: ")
        valor = input("Digite o valor do pedido: ")
        status = input("Digite o status do pedido: ")

        pedido = cls(Pedidos.num_pedido, itens, data, prazo, valor, status)
        Pedidos.lista_pedido.append(pedido)
        Pedidos.num_pedido += 1

    # Função para editar ou excluir os pedidos
    def edit_pedido():
        try:
            print ("Deseja editar um pedido, excluir um pedido ou voltar ao menu principal?  ")
            print ("1 - Editar")
            print ("2 - Excluir") 
            print ("3 - Voltar")
            opcao_pedido = int(input())

            if opcao_pedido < 1 or opcao_pedido >3:
                print ("Selecione uma opção dentre as disponíveis.")
                print ("Pressione enter para continuar...")
                return
            
            elif opcao_pedido == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                buscar_pedido = int(input("Digite o numero (ID) do pedido que deseja editar: "))

                pedido_encontrado = None
                for pedido in Pedidos.lista_pedido:
                    if buscar_pedido == pedido.numero_pedido:
                        pedido_encontrado = pedido
                        break
                if pedido_encontrado:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print ("Pedido encontrado: ")
                    pedido_encontrado.info_pedido()

                    print ("Qual dado deseja editar:")
                    print ("1 - Itens")
                    print ("2 - Prazo")
                    print ("3 - Valor")
                    print ("4 - Status")
                    print ("5 - Cancelar")
                    opcao_editar_pedido = input("Digite a opção desejada: ")

                    if opcao_editar_pedido == "1":
                        pedido_encontrado.itens_pedido = input ("Novo(s) iten(s): ")
                    elif opcao_editar_pedido == "2":
                        pedido_encontrado.prazo_pedido = input ("Novo prazo: ")
                    elif opcao_editar_pedido == "3":
                        pedido_encontrado.valor_pedido = input ("Novo valor: ")
                    elif opcao_editar_pedido == "4":
                        pedido_encontrado.status_pedido = input ("Novo status: ")
                    elif opcao_editar_pedido == "5":
                        print ("Cancelando...")
                        input ("Pressione enter para continuar...")
                    else: 
                        print ("Opção inválida.")
                    
                    print ("\nDados atualizados:")
                    pedido_encontrado.info_pedido()
                    input ("Pressione enter para continuar...")
                
            elif opcao_pedido == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                buscar_pedido = int(input("Digite o numero (ID) do pedido que deseja excluir: "))

                for pedido in Pedidos.lista_pedido:
                    if buscar_pedido == pedido.numero_pedido:
                        Pedidos.lista_pedido.remove(pedido)
                        print ("Pedido excluido com sucesso!")
                        input ("Pressione enter para continuar...")
                        return
                print ("Pedido não encontrado")
                input ("Pressione enter para continuar...")
            elif opcao_pedido == 3:
                print ("voltando ao menu principal.")
                input ("Pressione enter para continuar...")
            else:
                print ("opção inválida!")
                input ("Pressione enter para continuar...")

        except ValueError:
            print ("Entrada Inválida, digite um numero intero dentre as opções disponíveis.")
            input ("Pressione Enter para continuar...")

    # Função para exibir os todos pedidos, opção de filtrar por status
    def relatorio_pedidos():
        print ("Relatório de pedidos:")
        print ("1 - Todos pedidos")
        print ("2 - Pedidos abertos")
        print ("3 - Pedidos concluídos")
        print ("4 - Pedidos cancelados")
        print ("5 - Voltar")
        
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            if not Pedidos.lista_pedido:
                print ("Nenhum pedido cadastrado.")
                input("Pressione Enter para continuar...")
            else:
                for pedido in Pedidos.lista_pedido:
                    pedido.info_pedido()
                
                input("pressione enter para continuar...")

        elif opcao == "2":
            print ("Pedidos em Aberto:")
            for pedido in Pedidos.lista_pedido:
                if pedido.status_pedido.strip().lower() == "aberto":
                    pedido.info_pedido()
                    
            else:
                print ("Não há pedidos abertos.")
                input("pressione enter para continuar...")

        elif opcao == "3":
            print ("Pedidos concluídos:")
            for pedido in Pedidos.lista_pedido:
                if pedido.status_pedido.strip().lower() == "concluído" or pedido.status_pedido.strip().lower() == "concluido":
                    pedido.info_pedido()
                    
            else:
                print ("Não há pedidos concluídos.")
                input("pressione enter para continuar...")

        elif opcao == "4":
            print ("Pedidos cancelados:")
            for pedido in Pedidos.lista_pedido:
                if pedido.status_pedido.strip().lower() == "cancelado":
                    pedido.info_pedido()
                    
            else:
                print ("Não há pedidos cancelados.")
                input("pressione enter para continuar...")
        
        elif opcao == "5":
            print ("Voltando ao menu principal.")
            input ("Pressione enter par continuar...")
        
        else:
            print ("Entrada inválida")
            input ("Pressione enter par continuar...")    

# Função para exibir o menu.
def menu():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Sistema para Gerenciamento de Clientes e Pedidos")
            print ("Selecione uma opção para continuar\n\n"
            "1 - Consultar Clientes Cadastrados\n"
            "2 - Cadastrar Novo Cliente\n"
            "3 - Editar ou Excluir Cliente Cadastrado\n"
            "4 - Consultar Pedidos cadastrados\n"
            "5 - Cadastrar Novo Pedido\n"
            "6 - Editar ou Excluir Pedido Cadastrado\n"
            "7 - Sair"
            )
            escolha_menu = int(input())

            if escolha_menu < 1 or escolha_menu >7:
                print ("Você precisa selecionar entre uma das opções disponíveis.")
                input ("Pressione Enter para continuar...")

            elif escolha_menu == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                if not Cliente.lista_cliente:
                    print ("Nenhum cliente cadastrado...")
                    input("Pressione Enter para continuar...")
                else:
                    for cliente in Cliente.lista_cliente:
                        cliente.info_cliente()
                    input("Pressione Enter para continuar...")

            elif escolha_menu == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                Cliente.cadastro()

            elif escolha_menu == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                Cliente.edit_cliente()

            elif escolha_menu == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                Pedidos.relatorio_pedidos()

            elif escolha_menu == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                Pedidos.cadastro()

            elif escolha_menu == 6:
                os.system('cls' if os.name == 'nt' else 'clear')
                Pedidos.edit_pedido()

            elif escolha_menu == 7:
                print ("Saindo...")
                break
                
            else:
                print ("Entrada Inválida, digite um numero intero dentre as opções disponíveis.")
                input("Pressione Enter para continuar...")

        except ValueError:
            print ("Entrada Inválida, digite apenas um numero intero dentre as opções disponíveis.")
            input ("Pressione Enter para continuar...")
    
# rodar App:
if __name__ == "__main__":
    menu()