import requests # type: ignore
from rich import print # type: ignore
from rich.panel import Panel # type: ignore

def lin():
    print('-'*140)


def adicionar_produto():
    while True:
        try:
            cliente = str(input('Digite o nome do cliente: '))
            produto = str(input('Digite o nome do produto: '))
            quantidade= int(input('Digite a quantidade: '))
            valor = float(input('Digite o valor da unitario: '))
            status = int(input('Digite o Status do pedido [1-PENDENTE] [2- EM ROTA] [3-ENTREGUE]'))
            if status == 1:
                status = 'PENDENTE'
                break
            elif status == 2:
                status = 'EM ROTA'
                break
            elif status == 3:
                status = 'ENTREGUE'
                break
            else:
                print('OPÇÃO INVALIDA')
        except (ValueError,TypeError):
            print('OPÇÃO INVALIDA')
    

    dados = {
        'Cliente': cliente,
        'Produto': produto, 
        'Quantidade': quantidade,
        'Valor_Unitario': valor,
        'Status': status
    }
    link_api = 'https://6a1f6ebfb79eec0d6cf0c2c9.mockapi.io/api/pedidos/SistemaPedido'
    requisicao_api = requests.post(link_api,json= dados)
    if requisicao_api.status_code == 201:
        print(f'Pedido Inserido!')
    else:
        print(f'ERRO DE REQUISIÇÂO NA API! CODIGO: {requisicao_api.status_code}')
        
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
    else:
        print('ERRO DE REQUISIÇÂO NA API')

def buscar_pedido():
    buscar = int(input('Digite o numero de ordem:  '))
    link_api = f'https://6a1f6ebfb79eec0d6cf0c2c9.mockapi.io/api/pedidos/SistemaPedido/{buscar}'
    requisicao_api = requests.get(link_api)
    if requisicao_api.status_code == 200:
        dados = requisicao_api.json()
        print(f'Numero da ordem: {dados["id"]}  | Cliente: {dados["Cliente"]} | Produto: {dados["Produto"]} | Valor Unitario R${dados["Valor_Unitario"]} | Status Do Pedido: {dados["Status"]}')
    elif requisicao_api.status_code == 404:
        print(f'[red]ERRO: ORDEM NAO ENCONTRADA NO SiSTEMA CODIGO {requisicao_api.status_code}[/]')
    else:
        print(f'ERRO DE REQUISIÇÂO NA API! CODIGO: {requisicao_api.status_code}')
   

def apagar_ordem():
    buscar = int(input('Digite o numero de ordem que deseja remover:  '))
    link_api = f'https://6a1f6ebfb79eec0d6cf0c2c9.mockapi.io/api/pedidos/SistemaPedido/{buscar}'
    requisicao_api = requests.delete(link_api)
    if requisicao_api.status_code == 200:
        print(f'A ordem {buscar} foi apagada com sucesso')
    elif requisicao_api.status_code == 404:
        print(f'[red]ERRO: ORDEM NAO ENCONTRADA NO SiSTEMA CODIGO {requisicao_api.status_code}[/]')    
    else:
        print(f'ERRO NA API! CODIGO:{requisicao_api.status_code}')



def atualizar_pedido():
    buscar = int(input('Digite o numero de ordem que deseja alterar:  '))
    linkapi = f'https://6a1f6ebfb79eec0d6cf0c2c9.mockapi.io/api/pedidos/SistemaPedido/{buscar}'
    resp = int(input('Digite o campo que deseja alterar [1 - CLIENTE] [2 - PRODUTO] [3 - QUANTIDADE] [4 - VALOR UNITARIO] [5 - STATUS]'))
    if resp == 1:
        resp = 'Cliente'
        escolha = str(input('Digite o novo nome: '))
        parametros = {
            'Cliente': escolha
        }
    elif resp == 2:
        escolha = str(input('Digite o novo produto: '))
        parametros = {
            'Produto': escolha
        }
    elif resp ==3:
        escolha = int(input('Digite a nova quantidade: '))
        parametros = {
            'Quantidade': escolha
        }
    elif resp == 4:
        escolha = float(input('Digite a novo valor: '))
        parametros = {
            'Valor_Unitario': escolha
        }
    elif resp == 5:
        while True:
            try:
                att = int(input('Novo status da ordem [1-PENDENTE] [2- EM ROTA] [3-ENTREGUE]'))        
                if att == 1:
                    att = 'PENDENTE'
                    parametros = {
                    'Status': att
                        }
                    break
                elif att == 2:
                    att = 'EM ROTA'
                    parametros = {
                    'Status': att
                        }
                    break
                elif att == 3:
                    att = 'ENTREGUE'
                    parametros = {
                    'Status': att
                        }
                    break
                else:
                    print('OPÇÃO INVALIDA')
                
            except ValueError:
                print('OPÇÃO INVALIDA!')
    else:
        print('OPÇÃO INVALIDA!')
    
        
    
    requisicao_api = requests.patch(linkapi,json=parametros)
    if requisicao_api.status_code == 200:
        print('[green]PEDIDO ALTERADO[/]')
    elif requisicao_api.status_code == 404:
        print(f'[red]ERRO: ORDEM NAO ENCONTRADA NO SiSTEMA CODIGO {requisicao_api.status_code}[/]')
    else:
        print(f'ERRO DE API! CODIGO:{requisicao_api.status_code}')


def buscar_id():
    while True:
        try:
            busca_por_id = int(input('Digite o numero de ordem que deseja buscar: '))
            link_api = f'https://6a1f6ebfb79eec0d6cf0c2c9.mockapi.io/api/pedidos/SistemaPedido/{busca_por_id}'
            requisicao_api = requests.get(link_api)
            if requisicao_api.status_code == 200:
                dados = requisicao_api.json()
                print(Panel(f'RESULTADO DA BUSCA: {busca_por_id} | CLIENTE: {dados["Cliente"]} | PRODUTO: {dados["Produto"]} | QUANTIDADE: {dados["Quantidade"]} | VALOR UNIDADE {dados["Valor_Unitario"]}R$'))
                break
            elif requisicao_api.status_code == 404:
                print(f'[red]ERRO: ORDEM NAO ENCONTRADA NO SiSTEMA CODIGO {requisicao_api.status_code}[/]')    
                break
            else:
                print(f'ERRO NA API! CODIGO:{requisicao_api.status_code}')
                break
        except ValueError:
            print('[red]OPÇÂO INVALIDA[/]')
  
   
def buscar_por_cliente():       
        cliente = str(input('Digite o nome do cliente: '))
        link_api = f'https://6a1f6ebfb79eec0d6cf0c2c9.mockapi.io/api/pedidos/SistemaPedido'
        requisicao_api = requests.get(link_api)
        if requisicao_api.status_code == 200:
            dados = requisicao_api.json()
            print('-'*45,'RESULTADO DA BUSCA','-'*45)
            for item in dados:
                if cliente in item["Cliente"]:
                    print(f'CLIENTE: {item["Cliente"]} | PRODUTO: {item["Produto"]} | QUANTIDADE: {item["Quantidade"]} | VALOR UNIDADE {item["Valor_Unitario"]}R$')
            print('-'*110)
        elif requisicao_api.status_code == 404:
            print(f'[red]ERRO: ORDEM NAO ENCONTRADA NO SiSTEMA CODIGO {requisicao_api.status_code}[/]')    
                
        else:
            print(f'ERRO NA API! CODIGO:{requisicao_api.status_code}')
                
        
   
   
def buscar_status():
    while True:
            try:
                status = int(input('Digite o status que deseja procurar [1-PENDENTE] [2- EM ROTA] [3-ENTREGUE]'))        
                if status == 1:
                    status = 'PENDENTE'
                    break
                elif status == 2:
                    status = 'EM ROTA'
                    break
                elif status == 3:
                    status = 'ENTREGUE'
                    break
                else:
                    print('OPÇÃO INVALIDA')
                
            except ValueError:
                print('OPÇÃO INVALIDA!')
    link_api = f'https://6a1f6ebfb79eec0d6cf0c2c9.mockapi.io/api/pedidos/SistemaPedido'
    requisicao_api = requests.get(link_api)
    if requisicao_api.status_code == 200:
        dados = requisicao_api.json()
        print('-'*45,'RESULTADO DA BUSCA','-'*45)       
        for item in dados:
            if status in item["Status"]:
                print(f'CLIENTE: {item["Cliente"]} | PRODUTO: {item["Produto"]} | QUANTIDADE: {item["Quantidade"]} | VALOR UNIDADE {item["Valor_Unitario"]}R$')
        print('-'*110)   
    else:
        print(f'ERRO NA API! CODIGO:{requisicao_api.status_code}')

