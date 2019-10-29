def initGame():
    return "Inicio do Jogo da Velha seja bem vindo!"

def showRules():
    return "Para jogar escolha onde colocar a peça. A peça não pode ser sobreescrita"

def initList():
    listGame = []
    for i in range(0,3,1):
        listGame.append([])
        for k in range(0,3,1):
            listGame[i].append("O")
    return listGame

def showGame(game):
    a = ""
    print ("   C1 C2 C3")
    for i in range(0,3,1):
        for k in range(0,3,1):
            if(i == 0) and (k == 0):
                a = "L1 "
            elif(i ==1 ) and ( k ==0):
                a = "L2 "
            elif(i==2) and (k==0):
                a= "L3 "

            a+=" "+game[i][k]
        print(a)
        
def doMoviment(game, comand, simbol):

    if(comand[0]== "C1"):
        coluna = 0
    elif(comand[0] == "C2"):
        coluna = 1
    else:
        coluna =2

    if(comand[1] == "L1"):
        linha = 0
    elif(comand[1]=="L2"):
        linha = 1
    else:
        linha = 2
    if(game[linha][coluna] == "O"):
        game[linha][coluna]= simbol
        return game
    return []

def canWin(game, simbol):
    cond= False
    cont = 0
    index= 0

    for i in game:
        for k in i:
            if(k == simbol):
                cont+=1
        if(cont==3):
            return True
        else:
            cont = 0

    for i in range(0,3,1):

        for k in range(0,3,1):
            if(game[k][index]==simbol):
                cont+=1
            else:
                cont =0
                index+=1
                break
        if(cont == 3 ):
            return True
        else:
            cont = 0
            
    for i in range(0,3,1):
        if(game[i][i] == simbol):
            cont+=1
        else:
            break
    if(cont==3):
        return True
    cont = 0

    for i in range(2,0,-1):
        if(game[i][i]== simbol):
            cont+=1
        else:
            break
    if(cont == 3):
        return True
    return False;
        
    
    
print(initGame())
print(showRules())

cond = True
cont = 0
jogadores = []
contJogador =0
inGame = True

while(cond):

    j1=(str(input("Name player %i => "%(cont+1))))
    j2=(str(input("Name player %i => "%(cont+1))))

    if(j1 != j2):
        jogadores.append(j1)
        jogadores.append(j2)
        cond= False

jogo = initList()
accepted = ["C1", "L1", "C2", "L2", "C3", "L3"]


while(inGame):

    print("Vez do jogador %s" %jogadores[cont])
    showGame(jogo)
    comand = str(input("\nEscolha local para jogar: "))
    comand = comand.split("/")

    if(comand[0] in accepted) and (comand[1] in accepted):
        if(cont == 0):
            if(doMoviment(jogo,comand,"X")==[]):
                print("Comando invalido")
                continue
            else:
                game= doMoviment(jogo,comand,"X")
                if(canWin(jogo,"X")):
                    print(" JOGADOR %s É O GANHADOR." %jogadores[cont])
                    inGame = False
                    teste = int(input("Deseja continuar? [s][n] : "))
                    if(teste==s):
                        jogo = iniList()
                        cont= 0
                cont+=1
        else:
            if(doMoviment(jogo,comand,"C")==[]):
               print("comando invalido")
               continue
            else:
                game= doMoviment(jogo,comand,"C")
                if(canWin(jogo,"C")):
                    print(" JOGADOR %s É O GANHADOR." %jogadores[cont])
                    inGame= False
                    teste = int(input("Deseja continuar? [s][n] : "))
                    if(teste==s):
                        jogo = iniList()
                        cont= 0
                cont-=1
                
    if ("O" in jogo[0]) or("O" in jogo[1]) or ("O" in jogo[2]) :
        continue
    else:
        print("IH, deu velha")
        inGame= False
        teste = int(input("Deseja continuar? [s][n] : "))
        if(teste==s):
            jogo = iniList()
            cont= 0
            inGame= True;
print("Jogo finalizado")
