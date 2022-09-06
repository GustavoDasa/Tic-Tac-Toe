from colorama import Fore
import os, random

e = {1:1,2:2,3:3,4:10,5:20,6:30,7:100,8:200,9:300}
eb = {1:1,2:2,3:3,10:4,20:5,30:6,100:7,200:8,300:9}

k = {6:[3,4,5],60:[30,40,50],600:[300,400,500],111:[11,101,110],222:[22,202,220],333:[33,303,330],123:[120,103,23],321:[21,301,320]}


def Humano():
    global j, possiveis, jogador, jog,p
    print(f'\n {j[1]} | {j[2]} | {j[3]}\n---+---+---\n {j[4]} | {j[5]} | {j[6]}\n---+---+---\n {j[7]} | {j[8]} | {j[9]}\n')
    while True:
        try:
            x = int(input('Insira a casa que deseja jogar: '))
            if x in possiveis:
                j[x] = Fore.BLUE + "X" + Fore.RESET
                p[x] = -1
                jogador.append(x)
                jog.append(e[x])
                possiveis[x - 1] = 0
                Perdeu()
            else:
                continue
            break
        except:
            print('\nInsira um valor válido\n')


def Perdeu():
    global g

    teta = f'\n {j[1]} | {j[2]} | {j[3]}\n---+---+---\n {j[4]} | {j[5]} | {j[6]}\n---+---+---\n {j[7]} | {j[8]} | {j[9]}\n'
    ganhador = {-3: Fore.BLUE + "\nVocê venceu!!" + Fore.RESET ,3: Fore.RED +"\nVocê perdeu!!"+Fore.RESET}
    for i in [-3,3]:
        if sum([p[1],p[2],p[3]]) == i:
            print(ganhador[i])
            g = True
            print(teta)
            break
        elif sum([p[4],p[5],p[6]]) == i:
            print(ganhador[i])
            g = True
            print(teta)
            break
        elif sum([p[7],p[8],p[9]]) == i:
            print(ganhador[i])
            g = True
            print(teta)
            break
        elif sum([p[1],p[4],p[7]]) == i:
            print(ganhador[i])
            g = True
            print(teta)
            break
        elif sum([p[2],p[5],p[8]]) == i:
            print(ganhador[i])
            g = True
            print(teta)
            break
        elif sum([p[3],p[6],p[9]]) == i:
            print(ganhador[i])
            g = True
            print(teta)
            break
        elif sum([p[1],p[5],p[9]]) == i:
            print(ganhador[i])
            g = True
            print(teta)
            break
        elif sum([p[7],p[5],p[3]]) == i:
            print(ganhador[i])
            g = True
            print(teta)
            break
    if sum(possiveis)==0 and g== False:
        g = True
        print(Fore.YELLOW + '\nDeu Velha' + Fore.RESET)
        print(teta)


def Bordas():
    global j, r, possiveis, maq, maquina, o,p

    for i in [1, 3, 7, 9]:
        if i in possiveis:
            o = i
            maq.append(e[i])
            maquina.append(i)
            possiveis[i - 1] = 0
            j[i] = Fore.RED + "O" + Fore.RESET
            r[i] = 1
            p[i] = 1
            break


def Robo():
    global j, r, possiveis, maq, maquina, o,p,g
    if g == False:
        lance = False
        if len(jogador) == 1:
            Bordas()
        else:
            if len(jogador)>2:
                jog.pop(0)
            for i in k:
                if sum(jog) in k[i] and possiveis[eb[i - sum(jog)] - 1] != 0:
                    o = eb[i - sum(jog)]
                    maq.append(e[o])
                    maquina.append(o)
                    possiveis[o - 1] = 0
                    j[o] = Fore.RED + "O" + Fore.RESET
                    r[o] = 1
                    p[o] = 1
                    lance = True
                    break
            if lance == False:
                poss=[]
                for i in possiveis:
                    if i!=0:
                        poss.append(i)
                o = random.choice(poss)
                maq.append(e[o])
                maquina.append(o)
                possiveis[o - 1] = 0
                j[o] = Fore.RED + "O" + Fore.RESET
                r[o] = 1
                p[o] = 1
        Perdeu()




def Jogo1():
    'Começa o humano, se jogar no meio, robo joga na bordo, e vice-versa'
    Humano()
    if 5 in jogador:
        Bordas()
    else:
        maquina.append(5)
        maq.append(20)
        possiveis[5 - 1] = 0
        j[5] = Fore.RED + "O" + Fore.RESET
        r[5] = 1
        p[5] = 1
    while g == False:
        Humano()
        Robo()


def Jogo2():
    'Começa robo, joga nas bordas '
    Bordas()
    while g == False:
        Humano()
        Robo()



while True:
    try:
        # os.system("cls")
        j = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
        r = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        p = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        possiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        jogador = []
        jog = []
        maquina = []
        maq = []
        g = False

        if int(input('\n1 - Você começa:\n2 - Robô começa:\n')) == 1:
          Jogo1()
        else:
          Jogo2()
        input('\nTecle ENTER para continuar')
    except:
        print('\nInsira um valor válido!\n')


# Executa o programa
if __name__ == "__main__":
	main()
