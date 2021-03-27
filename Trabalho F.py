def Ord_Sel():
    def ordenacao_selecao(a):
        n = len(a)
        for i in range(n):
            minimo = i
            for b in range(i + 1, n):
                if a[minimo] > a[b]:
                    minimo = b
            a[i], a[minimo] = a[minimo], a[i]

    a = eval('[' + input("Digite sua lista: ") + ']')
    
    arquivo = open('lista.txt', 'w')
    
    arquivo.write("===Ordenação por Seleção === \n\n\n"+"Arranjo original (não ordenado): \n"  + str(a) + "\n"+" Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    ordenacao_selecao(a)

    with open('lista.txt', 'a') as arquivo1:
        
        for valor1 in a:
            arquivo1.write( str(valor1) + ',')


#---------------------------------------------------------------------------------------------------
def Ord_In():
    def ordenacao_incercao(c):
        n = len(c)

        for d in range(1,n):
            chave = c[d]
            i = d-1

            while i >= 0 and c[i]> chave:
                c[i + 1] = c[i]
                i = i - 1
            c[i+1] = chave

    c = eval('[' + input("Digite sua lista: ") + ']')
    arquivo = open('lista.txt', 'w')
    arquivo.write("=== Ordenação por Ircerção === \n\n\n"+"Arranjo original (não ordenado): \n" + str(c) +"\n" + " Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    ordenacao_incercao(c)

    with open('lista.txt', 'a') as arquivo2:
        
        for valor2 in c:
            arquivo2.write( str(valor2) + ',')
#---------------------------------------------------------------------------------------------------
def Ord_Bol():
    def ordenacao_bolha(e):
        n = len(e)

        for i in range(n):
            for f in range(0, n-1):
                if(e[f]>e[f+1]):
                    temp = e[f]
                    e[f] = e[f+1]
                    e[f+1] = temp

    e = eval('[' + input("Digite sua lista: ") + ']')
    arquivo = open('lista.txt', 'w')
    arquivo.write("Ordenação em bolha" + '/n')
    arquivo.write("=== Ordenação por Bolha === \n\n\n"+"Arranjo original (não ordenado): \n"  + str(e) +"\n"+ " Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    ordenacao_bolha(e)

    with open('lista.txt', 'a') as arquivo3:
        
        for valor3 in e:
            arquivo3.write( str(valor3) + ',')
#---------------------------------------------------------------------------------------------------
menu=True
while menu:
    opcao=int(input('''
        ====================== Menu Principal ======================
    	  Escolha um programa
            ~>1 - Ordenação por Seleção
            ~>2 - Ordenação por Incersão
            ~>3 - Ordenação em Bolha
            ~>0 - Fechar Menu 
            Escolha uma opção:  '''))
    if opcao == 1:
        Ord_Sel()
    elif opcao == 2:
        Ord_In()
    elif opcao == 3:
        Ord_Bol()
    elif opcao == 0:
        print("Programa Finalizado.\n")
        break
    else:
        print("Este número não está nas alternativas, tente novamente :D.\n")
        