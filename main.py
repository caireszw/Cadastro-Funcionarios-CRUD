import requests # type: ignore
from time import sleep
import consultas
import interface

while True:
    interface.menu('ADICIONAR PRODUTO','LISTA DE PEDIDOS','BUSCAR PEDIDOS','ATUALIZAR PEDIDO','REMOVER PEDIDO','SAIR DO PROGRAMA')
    opc1 = interface.selecionar_opcao('Digite a opção desejada: ')
    if opc1 == 1:
        consultas.adicionar_produto()
    if opc1 == 2:
        consultas.lista_pedidos()
    elif opc1 == 3:
        consultas.buscar_pedido()
    elif opc1 == 4:
        consultas.atualizar_status()
    elif opc1 == 5:
        consultas.apagar_ordem()
    elif opc1 == 6:
        print('FIM DO SISTEMA OBRIGADO!')
        break
    elif opc1 > 6:
        print('Opção Invalida!')   
    sleep(2)