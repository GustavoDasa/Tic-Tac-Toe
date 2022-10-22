from colorama import Fore
import os

wins=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[7,5,3]]

def Humano():
    global jogo, possiveis, jogador,todo
    Board()
    while True:
        try:
            x = int(input('Jogador ' +Fore.BLUE + "X" + Fore.RESET+'\nInsira a casa que deseja jogar: '))
            if x in possiveis:
                jogo[x] = Fore.BLUE + "X" + Fore.RESET
                todo[x] = -1
                jogador.append(x)
                possiveis[x - 1] = 0
                poss.remove(x)
                Perdeu()
            else:
                continue
            break
        except:
            print('\nInsira um valor válido\n')

def Humano2():
    global jogo, possiveis, jogador,todo
    Board()
    while True:
        try:
            x = int(input('Jogador '+Fore.RED + "O" + Fore.RESET + '\nInsira a casa que deseja jogar: '))
            if x in possiveis:
                jogo[x] = Fore.RED + "O" + Fore.RESET
                todo[x] = 1
                maquina.append(x)
                possiveis[x - 1] = 0
                poss.remove(x)
                Perdeu()
            else:
                continue
            break
        except:
            print('\nInsira um valor válido\n')

def Perdeu():
    global g,vench
    winner = {-3:jogador,3:maquina}
    ganhador = {-3: Fore.BLUE + "\nVocê venceu!!" + Fore.RESET ,3: Fore.RED +"\nVocê perdeu!!"+Fore.RESET}
    for i in [-3,3]:
        for winn in wins:
            if len(set(winn) & set(winner[i]))==3:
                print(ganhador[i])
                vench = ganhador[i]
                g = True
                Board()
                break
        if g == True:
            break
    if sum(possiveis)==0 and g== False:
        g = True
        print(Fore.YELLOW + '\nDeu Velha' + Fore.RESET)
        Board()

def Bloq():
    global lance,o

  # Ataca pra vencer
    for i in wins:
      for j in possiveis:
          if len(set(i) & set([j] + maquina)) == 3:
              o = j
              lance = True
              break
      if lance == True:
          break

  # Bloqueia oponente
    if lance == False:
      for i in wins:
        for j in possiveis:
          if len(set(i) & set([j]+jogador))==3:
            o = j
            lance = True
            break
        if lance==True:
          break

def Bordas():
    global jogo, possiveis, maquina,todo,o
    for i in [1, 3, 7, 9]:
        if i in possiveis:
            o = i
            maquina.append(i)
            possiveis[i - 1] = 0
            jogo[i] = Fore.RED + "O" + Fore.RESET
            todo[i] = 1
            poss.remove(o)
            break

def Robo():
    global jogo, robo, possiveis, maquina,todo,g,lance,o

    if g == False:
        lance = False
        Bloq()
        if lance == True:
            maquina.append(o)
            possiveis[o - 1] = 0
            jogo[o] = Fore.RED + "O" + Fore.RESET
            todo[o] = 1
            poss.remove(o)
        else:
            for i in wins:
                if len(set(i) & set(poss + [o])) == 3:
                    alpha = list(set(i)-set([o]))
                    o = alpha[0]
                    lance = True
                    break
            if lance==False:
                o = poss[0]
            maquina.append(o)
            possiveis[o - 1] = 0
            jogo[o] = Fore.RED + "O" + Fore.RESET
            todo[o] = 1
            poss.remove(o)
        Perdeu()

def Jogo1():
    global o
    'Começa o humano, se jogar no meio, robo joga na bordo, e vice-versa'
    Humano()
    if 5 in jogador:
        Bordas()
    else:
        o = 5
        maquina.append(o)
        possiveis[o - 1] = 0
        jogo[o] = Fore.RED + "O" + Fore.RESET
        todo[o] = 1
        poss.remove(o)
    while g == False:
        Humano()
        Robo()

def Jogo2():
    'Começa robo, joga nas bordas '
    Bordas()
    while g == False:
        Humano()
        Robo()

def Jogo3():
    'Começa jogador 1 vs jogador 2'
    while g == False:
        Humano()
        if g == True:
          break
        Humano2()

def Board():
  print(f'\n {jogo[1]} | {jogo[2]} | {jogo[3]}\n---+---+---\n {jogo[4]} | {jogo[5]} | {jogo[6]}\n---+---+---\n {jogo[7]} | {jogo[8]} | {jogo[9]}\n')


while True:
    try:
        # os.system("cls")
        poss = [1,2,3,4,5,6,7,8,9]
        jogo = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
        todo = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        possiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        jogador = []
        maquina = []
        g = False
        y = int(input('\n1 - Você vs Máquina:\n2 - Máquina vs Você:\n3 - Você vs Outro:\n'))
        if y == 1:
          Jogo1()
        elif y==2:
          Jogo2()
        elif y ==3:
          Jogo3()
        input('\nTecle ENTER para continuar')
    except:
        print('\nInsira um valor válido!\n')


# Executa o programa
# if __name__ == "__main__":
# 	main()
