
lista = []

while True:
    print('Selecione uma opcao')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()
# opcao 'i' para abrir o adicionador
    if opcao == 'i':
        # aqui fica onde adicionar a tarefa.
        tarefa = input('Adicionar nova tarefa: ').lower().strip()
        lista.append(tarefa)# a tarefa que foi cadastrada entrou na nova_tarefa
        print('Nova tarefa cadastrada')# mostrar que a tarefa foi cadastrada

# opcao 'a' diz que o usuario que apagar a tarefa cadastrada.
    elif opcao == 'a':

        if len(lista) == 0: # isso faz que leia a lista e diz se tem tarefa.
            print('Nao a tarefa pra excluir')
            continue

        else:
            print('Tarefas')
        for i, item in enumerate(lista, start=1): #Aqui ele mostra as tarefas cadastrada
            print(i, '-', item)

        # excluir tarefa 
        excluir = input('digite a tarefa que deseja: ').lower().strip()
        if excluir in lista:
            lista.remove(excluir)# aqui ele faz a remoção da tarefa que escolheu
            print('Tarefa removida.')
        else:
            print('Palavra nao encontrada.')# aqui e caso degite errado

    elif opcao == 'l':
        
        if len(lista) == 0: # aqui mostra a lista
            print('lista vazia')
        for i, item in enumerate(lista, start=1): # aqui ele ver quantas coisas tem na lista
            print(i, '-', item)

    elif opcao == 's':
        print('Fechado')
        break
    
