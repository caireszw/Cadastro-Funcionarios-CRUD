import requests # type: ignore
from time import sleep
import consultas
import interface

while True:
    interface.menu('ADICIONAR PRODUTO','LISTA DE PEDIDOS','BUSCAR PEDIDOS','ATUALIZAR PEDIDO','REMOVER PEDIDO','SAIR DO PROGRAMA')
    opc1 = interface.selecionar_opcao('Digite a opção desejada: ')
    if opc1 == 1:
        consultas.adicionar_produto()
    elif opc1 == 2:
        consultas.lista_pedidos()
    elif opc1 == 3:
        interface.menu_buscar('BUSCAR POR ID', 'BUSCAR POR CLIENTE', 'BUSCAR POR STATUS', 'VOLTAR')
        opc2 = interface.selecionar_opcao('Digite a opção desejada: ')
        if opc2 == 1:
            consultas.buscar_id()
        elif opc2 == 2:
            consultas.buscar_por_cliente()
        elif opc2 == 3:
            consultas.buscar_status()
        elif opc2 == 4:
            print('VOLTAR')
        else:
            print('OPÇÃO INVALIDA!')
    elif opc1 == 4:
        consultas.atualizar_pedido()
    elif opc1 == 5:
        while True:
            try:
                opc2 = int(input('DESEJA APAGAR UMA ORDEM: [1 - SIM] [2 - RETORNAR AO MENU] '))
                if opc2 == 1:
                    consultas.apagar_ordem()
                    break
                elif opc2 == 2:
                    print('RETORNANDO AO MENU')
                    break
                else:
                    print('OPÇÃO INVALIDA')
            except ValueError:
                print('OPÇÂO INVALIDA')
    elif opc1 == 6:
        print('FIM DO SISTEMA OBRIGADO!')
        break
    elif opc1 > 6:
        print('Opção Invalida!')   
    sleep(2)