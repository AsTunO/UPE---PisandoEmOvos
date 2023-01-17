config = {

    "maxArmadilhas": 3,
    "jogadorArmador": 0,
    "jogadorAndarilho": 0,
    "pontacaoJogadorArmador": 0,
    "pontacaoJogadorAndarilho": 0,

}

terreno = []
for i in range (7):
    linha = []
    for j in range (7):
        linha.append("A")
    terreno.append(linha)

def redefinirTerreno():

    terreno = []
    for i in range (7):
        linha = []
        for j in range (7):
            linha.append("A")
        terreno.append(linha)

def validador(x):
    if(x == 1 or x == 2):
        return True
    else:
        return False

def imprimirTerreno():
    for i in range(8):
        print("")
        for j in range(8):
            if(i == 0):
                print(j, end=" ")
            elif(j == 0):
                print(i, end=" ")
            else:
                print(terreno[i-1][j-1], end=" ")
        

def plantarArmadilhas():

    print("\nJogador [{}] , você pode esconder até 3 ovos podres por linha do terreno.".format(config["jogadorArmador"]))

    
    for i in range (7):
        count = 0
        for j in range (3):
            ovoPosi = int(input("Em qual coluna da linha {} você quer esconder ovos podres? [1 a 7]\n".format(i+1)))
            while(ovoPosi < 1 or ovoPosi > 7):
                ovoPosi = int(input("Coluna inválida, tente novamente. [1 a 7]\n"))
            while(terreno[i][ovoPosi-1] != "A"):
                ovoPosi = int(input("Coluna já ocupada, tente novamente. [1 a 7]\n"))
            terreno[i][ovoPosi-1] = "O"
            count += 1
            if(count == 3):
                break
            else:
                aux = int(input("Deseja esconder mais um ovo podre nesta linha? [1 ou 2]\n"))
                while(validador(aux) == False):
                    aux = int(input("Opção inválida, tente novamente. [1 ou 2]\n"))
                if(aux == 1):
                    continue
                else:
                    break

def caminharAndarilho():
    print("""
São válidos os espaços: [1, 2, 3, 4, 5, 6, 7]
Escolha sabiamente um dos espaços válidos
    """)

    passo = int(input())

    while(passo < 1 or passo > 7):
        passo = int(input("Espaço inválido, tente novamente. [1, 2, 3, 4, 5, 6, 7]\n"))
    
    for i in range (7):
        if(terreno[i][passo - 1] == "O"):
            print("Eca! Você pisou em um ovo podre e perdeu")
            config["pontacaoJogadorArmador"] += 1
            redefinirTerreno()
            break
        else:
            passo = int(input("Escolha seu proximo passo, são validos os valores [{}]\n".format(espacosValidos(passo))))
            while((passo < passo - 1) or (passo > passo + 1)):
                passo = int(input("Espaço não disponivel! Escolha seu proximo passo, são validos os valores [{}]\n".format(espacosValidos(passo))))
        if(i == 6 and terreno[i][passo - 1] != "O"):
            print("Você atravessou o terreno sem cair em nenhuma armadilha! Parabéns!!!!")
            config["pontacaoJogadorAndarilho"] += 1
            redefinirTerreno()
            break

def espacosValidos(posicao):
    listEspacosValidos = []

    if(posicao == 7):
        listEspacosValidos.append(posicao - 1)
        listEspacosValidos.append(posicao)
    elif(posicao == 0):
        listEspacosValidos.append(posicao)
        listEspacosValidos.append(posicao + 1)
    else:
        listEspacosValidos.append(posicao - 1)
        listEspacosValidos.append(posicao)
        listEspacosValidos.append(posicao + 1)

    return listEspacosValidos

def menu():
    print("""
Opções:
1 - Definir Armador
2 - Plantar Armadilhas
3 - Iniciar com Andarilho
4 - Mostrar o placar
0 - Finalizar o Jogo
    """)

def definirArmador():
    x = int(input("Qual jogador plantará as armadilhas? [1 ou 2]\n"))
    if(validador(x) == True):
        if(x == 1):
            config["jogadorArmador"] = 1
            config["jogadorAndarilho"] = 2
        else:
            config["jogadorArmador"] = 2
            config["jogadorAndarilho"] = 1

        print("""
O armador é o jogador: {}
O andarilho é o jogador: {}
        """.format(config["jogadorArmador"], config["jogadorAndarilho"]))

    else:
        print("Jogador inválido")
        definirArmador()

while True:
    menu()
    opcaoMenu = int(input())
    while(opcaoMenu < 0 or opcaoMenu > 4):
        opcaoMenu = int(input("Opção inválida, tente novamente. [0 a 4]\n"))
    if(opcaoMenu == 0): 
        break

    elif(opcaoMenu == 1):
        definirArmador()

    elif(opcaoMenu == 2):

        if(config["jogadorArmador"] != 1 and config["jogadorArmador"] != 2):
            print("Defina o armador primeiro")
            definirArmador()

        imprimirTerreno()
        plantarArmadilhas()
        imprimirTerreno()

    elif(opcaoMenu == 3):
        if(config["jogadorArmador"] != 1 and config["jogadorArmador"] != 2):
            print("Defina o armador primeiro")
            definirArmador()

        for i in range(100):
            print("=" * i)

        caminharAndarilho()

    elif(opcaoMenu == 4):

        if(config["jogadorArmador"] == 1 ):
            print("""
Pontuação do jogador 1: {}
Pontuação do jogador 2: {}
            """.format(config["pontacaoJogadorArmador"], config["pontacaoJogadorAndarilho"]))
        else:
            print("""
Pontuação do jogador 1: {}
Pontuação do jogador 2: {}
            """.format(config["pontacaoJogadorAndarilho"], config["pontacaoJogadorArmador"]))
