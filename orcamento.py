from time import sleep
print('-----------------painting budget--------------------')
print('Bem-vindo ao PAINTING BUDGET')
print('Orçamento automatizado para a pintura de obras')
print('Para dar início, tenha todas as metragens das áreas que serão pintadas e também de portas e janelas.')
sleep(1)
print('Tudo em mãos?')
sleep(1)
print('VAMOS LÁ!')
sleep(1)
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
print('----------------------------------------------------')
print('ATENÇÃO! Caso não haja portas ou janelas, digite o valor 0. Caso haja mais de uma janela ou porta, some-os.')
porta_alt = float(input('Altura da porta: '))
porta_larg = float(input('Largura da porta: '))
janela_alt = float(input('Altura da janela: '))
janela_larg = float(input('Largura da janela: '))

#cálculo das metragens das paredes, portas e janelas.
porta = porta_alt * porta_larg
janela = janela_alt * janela_larg
porta_janela = janela + porta
area = larg * alt
areareal = area - porta_janela
print('Sua parede tem {:.2f}m2 de área total desconsiderando portas e janelas.'.format(areareal))
m2_tinta = 27
qtd_tinta = areareal / m2_tinta 
print('-----------------------------------------------------')
print('Para pintar esta área, você precisara de {:.2f}L de tinta'.format(qtd_tinta))
print('-----------------------------------------------------')

#Valores de tintas
tinta_suvinil = 30
tinta_coral = 12
tinta_eucatex = 19
tinta_quartzolit = 8

#Opçoes
while True:
    print('    MARCA    |   CÓDIGO  ')
    print('   Suvinil   |    [su]   ')
    print('    Coral    |    [co]   ')
    print('   Eucatex   |    [eu]   ')
    print('  Quartzolit |    [qu]   ')
    opcao_tinta = input('Tinta escolhida: ')
    total = 0
    if opcao_tinta == 'su': 
        total = tinta_suvinil*areareal + areareal*12
        print('O valor da mão de obra é:R${:.2f}'.format(areareal*12))
        print('Valor total da obra:R${:.2f}'.format(total))
        break
    elif opcao_tinta == 'co': 
        total = tinta_coral*areareal + areareal*12
        print('O valor da mão de obra é:R${:.2f}'.format(areareal*12))
        print('Valor total da obra:R${:.2f}'.format(total))
        break
    elif opcao_tinta == 'eu': 
        total = tinta_eucatex*areareal + areareal*12
        print('O valor da mão de obra é:R${:.2f}'.format(areareal*12))
        print('Valor total da obra:R${:.2f}'.format(total))
        break
    elif opcao_tinta == 'qu': 
        total = tinta_quartzolit*areareal + areareal*12
        print('O valor da mão de obra é:R${:.2f}'.format(areareal*12))
        print('Valor total da obra:R${:.2f}'.format(total))
        break
    else:   
        print('Opção Inválida')
        continue
print('-------------------------------------------------------------------------')
print('Desconto de 5% para pagamento a vista e em até 6x sem juros no cartão')
pagamento = int(input('Forma de pagamento: Vista[1]/Parcelado[2]: '))
if pagamento == 1:
    print('Desconto de 5%')
    calc_desc = ((5/100) * total) 
    desc = total - calc_desc
    print(' Desconto aplicado para pagamento a vista. Valor total R${:.2f}'.format(desc))
elif pagamento == 2:
    parc_x = int(input('Quantidade de parcelas: '))
    if parc_x == 2:
       parcela = total/2
       print('2X sem juros de R${:.2f}'.format(parcela))
    elif parc_x == 3:
        parcela = total/3
        print('3X sem juros de R${:.2f}'.format(parcela))
    elif parc_x == 4:
        parcela = total/4
        print('4X sem juros de R${:.2f}'.format(parcela))
    elif parc_x == 5:
        parcela = total/5
        print('5X sem juros de R${:.2f}'.format(parcela))
    elif parc_x == 6:
        parcela = total/6
        print('6X sem juros de R${:.2f}'.format(parcela))
    else:
        print('Pagamento até 6X sem juros')
print('-----------------------------------------------------------------')
print('---------------- R.PAIVA INTELLIGENCE BUSINESS ------------------')
print('-----------------------------------------------------------------')
