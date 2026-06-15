import requests

def lin():
    print('-'*140)


def adicionar_produto():
    cliente = str(input('Digite o nome do cliente: '))
    produto = str(input('Digite o nome do produto: '))
    quantidade= int(input('Digite a quantidade: '))
    valor = float(input('Digite o valor da unitario: '))
    status = str(input('Digite o Status do pedido: '))

    dados = {
        'Cliente': cliente,
        'Produto': produto, 
        'Quantidade': quantidade,
        'Valor_Unitario': valor,
        'Status': status
    }
    link_api = 'https://6a1f6ebfb79eec0d6cf0c2c9.mockapi.io/api/pedidos/SistemaPedido'
    requests.post(link_api,json= dados)
    
    print(f'Pedido Inserido!')
   
def lista_pedidos():
    link_api = 'https://6a1f6ebfb79eec0d6cf0c2c9.mockapi.io/api/pedidos/SistemaPedido'
    requisicao_api = requests.get(link_api)
    if requisicao_api.status_code == 200:
        dados = requisicao_api.json()
        lin()
        print('LISTA DE PEDIDOS')
        print('')
        for item in dados:
            print(f'Numero da ordem: {item["id"]}  | Cliente: {item["Cliente"]} | Produto: {item["Produto"]} | Valor Unitario R${item["Valor_Unitario"]} | Status Do Pedido: {item["Status"]}')
        lin()


def buscar_pedido():
    buscar = int(input('Digite o numero de ordem:  '))
    link_api = f'https://6a1f6ebfb79eec0d6cf0c2c9.mockapi.io/api/pedidos/SistemaPedido/{buscar}'
    requisicao_api = requests.get(link_api)
    if requisicao_api.status_code == 200:
        dados = requisicao_api.json()
        print(f'Numero da ordem: {dados["id"]}  | Cliente: {dados["Cliente"]} | Produto: {dados["Produto"]} | Valor Unitario R${dados["Valor_Unitario"]} | Status Do Pedido: {dados["Status"]}')
   
def atualizar_status():
    buscar = int(input('Digite o numero de ordem:  '))
    att = str(input('Novo status da ordem:'))
    link_api = f'https://6a1f6ebfb79eec0d6cf0c2c9.mockapi.io/api/pedidos/SistemaPedido/{buscar}'
    dados = {
        'Status': att
    }
    requisicao_api = requests.patch(link_api,json=dados)
    print('Status Atualizado!')

def apagar_ordem():
    buscar = int(input('Digite o numero de ordem que deseja remover:  '))
    link_api = f'https://6a1f6ebfb79eec0d6cf0c2c9.mockapi.io/api/pedidos/SistemaPedido/{buscar}'
    requisicao_api = requests.delete(link_api)
    print(f'A ordem {buscar} foi apagada com sucesso')    

# buscar_pedido()
# lista_pedidos()
# adicionar_produto()
# atualizar_status()
# apagar_ordem()
